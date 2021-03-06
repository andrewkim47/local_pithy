from numpy import *
import time
from urllib import urlopen as uo
from struct import pack
import requests
import json

class SIUI():
    def __init__(self,site):
        self.site = site
        self.dec = {}
        self.dec['range'] = {'start': 28,'bytes': 4,'type':float32}
        self.dec['gain']  = {'start': 48,'bytes': 4,'type':int32}
        self.dec['prf']   = {'start':184,'bytes': 2,'type':int16} #SIUI was wrong here
        self.dec['delay'] = {'start': 44,'bytes': 4,'type':float32}
        self.dec['vel']   = {'start':168,'bytes': 4,'type':float32}
        self.dec['vel2']  = {'start': 56,'bytes': 2,'type':uint16 }
        self.dec['wave']  = {'start':400,'bytes':800,'type':uint16}
        self.base = self.getBaseline()
        self.gbase = self.getGainBaseline()
        self.rects = ['pos','neg','full','filter','rf']
        self.volts = range(50,550,50)
        self.freqs = ['1_4MHz','0.5_10MHz','2_20MHz','1MHz','2.5MHz','4MHz','5MHz','10MHz','13MHz','15MHz','20MHz']
        #defaults for param setting
        self.vset=50
        self.rng=30.0
        self.mode='PE'
        self.vel=2450
        self.pw = 200
        self.prf = 200
        self.damp = 0
        self.rect = 'full'
        self.power = 0
        self.freq = '1_4MHz'
        self.gain = 30.0
    
    def getBaseline(self):
        a = uo(self.site+"/getBaseline").read()
        base =  json.loads(a)
        return [item for sublist in base for item in sublist] 

    def getGainBaseline(self):
        a = uo(self.site+"/getGainBaseline").read()
        base =  json.loads(a)
        return [item for sublist in base for item in sublist] 

    
    def rawData(self):
        site = self.site
        data = uo(site+"/data/").read()
        ata = []
        for d in data.split(","):
            try:
                ata.append(int(d))
            except Exception as err:
                off = "on"

        return array(ata).T
    
    
    def setGain(self):
        #return uo(site+"/setGain/%f" % self.gain).read()
            #vel
        a = self.gbase
        gains = []
        for i in pack('i',self.gain*10): gains.append(ord(i))
        a[48:52] = gains

                #send bundle off
        cc = 0
        aout = []
        while cc < len(a):
            aout.append(a[cc:cc+1460])
            cc+=1460
        return self.sendMass({'data':aout})   


    def setParams(self):
        a = self.base
    
        #unpack sets and set things like TR,Voltage, etc
        rsets = a[80:84]
        foo = []
        for j in rsets:
            for i in range(8): 
                foo.append((j >> i) & 1)

        #set driving potential    
        sets = range(50,550,50)
        try: food = sets.index(self.vset)
        except: food = 0
        d = bin(food).replace("0b","").rjust(4,"0")
        volts = []
        for b in d: volts.append(int(b))
        volts.reverse()
        foo[25:29] = volts
        
        #set pulse width    
        food = self.pw/10
        d = bin(food).replace("0b","").rjust(7,"0")
        pws = []
        for b in d: pws.append(int(b))
        pws.reverse()
        foo[18:25] = pws

        #set rect    
        food = self.rects.index(self.rect)
        d = bin(food).replace("0b","").rjust(4,"0")
        pws = []
        for b in d: pws.append(int(b))
        pws.reverse()
        foo[8:12] = pws

        #set freq
        food = self.freqs.index(self.freq)
        d = bin(food).replace("0b","").rjust(4,"0")
        pws = []
        for b in d: pws.append(int(b))
        pws.reverse()
        foo[4:8] = pws

        #set power
        food = self.power
        d = bin(food).replace("0b","").rjust(4,"0")
        pws = []
        for b in d: pws.append(int(b))
        pws.reverse()
        foo[0:4] = pws


        #set PE/TR Mode
        if self.mode == 'TR': foo[16] = 1
        else: foo[16] = 0

        #set damping
        foo[17] = self.damp

        #repack bits to bytes for settings
        count = 0
        sets = []
        while count < len(foo):
            temp = ""
            for f in foo[count:count+8]: temp+=str(f)
            count += 8
            temp = temp[::-1]
            sets.append(int(temp,2))
        a[80:84] = sets
    
        #set range
        rngs = []
        for i in pack('f',self.rng): rngs.append(ord(i))
        a[28:32] = rngs

        #vel
        vels = []
        for i in pack('f',self.vel): vels.append(ord(i))
        # print self.vel
        # print vels
        a[168:168+4] = vels
        

        vels = []
        for i in pack('h',self.vel): vels.append(ord(i))
        # print self.vel
        # print vels
        a[56:56+2] = vels


        #prf
        prfs = []
        for i in pack('h',self.prf): prfs.append(ord(i))
        a[184:184+2] = prfs

        #send bundle off
        cc = 0
        aout = []
        while cc < len(a):
            aout.append(a[cc:cc+1460])
            cc+=1460
        return self.sendMass({'data':aout})    
    
    
    
    def processData(self,d):
        out = {}

        #do what we can automagically
        for k in self.dec.keys():
            out[k] = self.convert(k,d)
            if len(out[k]) == 1: out[k] = out[k][0]
        out['x'] = linspace(0,out['range'],len(out['wave']))
        
        #bit manip
        rsets = d[80:84]
        out['sets'] =[]
        for s in rsets:
            for i in range(8): 
                out['sets'].append((s >> i) & 1)
        
        out['gain'] = out['gain']/10.
        #get mode
        if out['sets'][16] == 0: out['mode'] = 'PE'
        else: out['mode'] = 'TR'

        #get damping
        out['damp'] = out['sets'][17]

        #get power
        temp = out['sets'][0:4]
        b = ""
        for t in temp: b+=str(t)
        b = b[::-1]
        out['power'] = int(b,2)

        #get driving potential
        sets = range(50,550,50)
        temp = out['sets'][25:29]
        b = ""
        for t in temp: b+=str(t)
        b = b[::-1]
        out['volt'] = sets[int(b,2)]
        
        #get rectification
        temp = out['sets'][8:12]
        b = ""
        for t in temp: b+=str(t)
        b = b[::-1]
        out['rect'] = self.rects[int(b,2)]
        
        #get freqs
        temp = out['sets'][4:8]
        b = ""
        for t in temp: b+=str(t)
        b = b[::-1]
        out['freq'] = self.freqs[int(b,2)]

        #get pulse width
        temp = out['sets'][18:25]
        b = ""
        for t in temp: b+=str(t)
        b = b[::-1]
        out['pw'] = int(b,2)*10
        
        return out
    
    def sendCommand(self,c):
        return uo(site+"/sendCmd/%s" % c).read()


    def sendMass(self,s):
        payload = s
        r = requests.post(self.site+"/toSIUI", json=payload)
        return r.text
        
    #thanks stack http://stackoverflow.com/a/2577487/565514
    def getData(self):
        d = self.rawData()
        return self.processData(d)

    def convert(self,k,arr):
        temp = ""
        s = self.dec[k]['start']
        l = self.dec[k]['bytes']
        for i in arr[s:s+l]:
            temp += chr(int(i))
            # if k == "vel": print int(i),
        return fromstring(temp,dtype=self.dec[k]['type'])

    
    def setGetCheck(self):
        self.setGain()
        time.sleep(.2)
        self.setParams()
        set1 = [1]
        set2 = [2]
        while set1 != set2:        
            self.setGain()
            time.sleep(.2)
            self.setParams()
            time.sleep(.8)
            a = self.getData()
            set1 = [self.gain,self.mode,self.rng  ,self.freq,self.vset,self.rect]
            set2 = [a['gain'],a['mode'],a['range'],a['freq'],a['volt'],a['rect']]
        return a

if __name__ == "__main__":
    from pithy import *
    site = 'http://localhost:9008'
    s = SIUI(site)
    
    # fils = glob("/Users/lab/serveSIUI/*.scmd")
    # fils = sorted(fils,key = lambda k: os.path.getmtime(k))
    # fils.reverse()
    # #for f in fils: print f
    # print fils[0]
    # for i in [0,1,2,3,4]:
    #     stuff = open(fils[i]).read()
    #     data = json.loads(stuff)
    #     #data = [item for sublist in data for item in sublist]
    #     subplot(2,1,1)
    #     plot(data[0],'.')
    #     temp = chr(data[0][56])+chr(data[0][57])
    #     print data[0][56],data[0][57],fromstring(temp,dtype=uint16)
    #     subplot(2,1,2)
    #     plot(data[0],'.')
    # subplot(2,1,1)
    # xlim([50,60])
    # subplot(2,1,2)
    # xlim([150,200])
    # showme()
    # clf()
    
    #specify parameters
    s.vset = 200
    s.gain = 25
    s.rng = 100
    s.pw = 444 
    s.rect = 'filter'
    s.freq = '2.5MHz'
    s.prf = 100
    #s.mode = 'TR'
    s.vel = 4000
    # data = s.setGetCheck()
    # #data = s.getData()
    # print data['vel'],data['vel2']
    # #data = s.getData()
    # plot(data['x'],data['wave'],label=s.pw)

    # xlabel('range (mm)')
    # #ylim([0,65600])
    # legend()
    # showme()
    # clf()
    
 
    
