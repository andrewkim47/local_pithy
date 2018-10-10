##Mothership = True
##Author: Dan Steingart
##Date Started: 20160731
##Notes: libEASI with built in time correction.

from pithy import *
from pymongo import MongoClient as mc
import pandas as pd

offsite="spike.princeton.edu"
offsite2 = "192.81.219.77"
class EASILIST():
    def __init__(self,ts=None,te=None,site=offsite,col='acoustic_data'):
        self.client = mc(site,27017)
        self.db = self.client.test_db
        self.ad = self.db[col]
        q = {}
        q['_id'] = {}
        if ts != None: q['_id']['$gt'] = ts
        if te != None: q['_id']['$lt'] = te
        elif (te == ts): q = {}

        self.parts = list(self.ad.find(q).distinct("run"))

class EASI():
    def __init__(self,run,q=None,site=offsite,col='acoustic_data',debug = False):
        self.run = run
        dts = time.time()
        cols = col.split("||")
        runs = run.split("||")
        self.raw = []
        qq = q
        for oo in range(len(runs)):
            if qq == None: q = {'run':runs[oo]}
            if debug: print "q = ",q
            self.client = mc(site,27017)
            self.db = self.client.test_db
            self.col = self.db[cols[oo]]
            self.cursor = self.col.find(q)
            if debug: print "got cursors (",self.cursor.count(),")",time.time()-dts
            self.cursor.sort('_id',1)
            if debug: print "sorted cursors",time.time()-dts
        
            raw = pd.DataFrame(list(self.cursor))
            
            if debug: print "got dataframe",time.time()-dts

            #Thanks Stack!
            if debug: print "initial df len:",len(raw)

            raw = raw[raw['amp'].map(len) == 495].copy()
            self.cursor.rewind()
            self.meta = self.cursor[self.cursor.count()-1]
            if debug: 
                for k in self.meta.keys(): print k
            self.raw.append(raw)
        self.raw = pd.concat(self.raw)
        if debug: print "df len:",len(self.raw)
        #backwards compatibility
        self.times = array(self.raw['_id'])
        self.out_NR = array(list(self.raw['amp']))
        self.count = len(self.times)
        self.out = abs(self.out_NR-128)
        self.tots = sum(self.out,axis=1)
        try: self.tofs = array(self.raw['t_shift'])
        except: tofo = None
        if debug: print "made arrays",time.time()-dts


    def time_correct(self,thresh=None,tstart=None,tend=None,toff=None,points=None):
        #Rather than fill blanks and pad, let's figure out the ROI we care about, and choose data that is as close to well space as possible.  Let's say that if a data point doesn't exist with a some bounds of that data point, we'll insert a shim.
        
        #We'll consider a few things.  
        #First: The average screen is ~1500 pixels across.  So we want to bound our solution to ~1500 slices.  Anything more is wasted info generally.  
        
        #Second: We'll use the available echem data to bound the range.  Start to end / 1500.  This will give us our target times.  In the abscence of echem data use the total acoustic time
        
        if (tstart == None) or (tend == None):
            tstart = self.times[0]
            tend = self.times[-1]
        
        cc = self.count
        if points == None:
            if cc > 1500: cc = 1500
        elif points == 'all':
            cc = self.count
        else: cc = points

        #get time spacing
        dt = linspace(tstart,tend,cc)
        
        diffs = []
        inds = []
        
        for i in dt:
            sub = abs(self.times-i)
            diffs.append(sub.min())
            inds.append(sub.argmin())
            
        nout    = []
        ntrt    = []
        nout_NR = []
        #make pands array
        pads = array([0 for i in range(495)])

        #Third: We'll do a recusive minimization search across the target times to find the closest data points.  Depending on the density of data we'll change the shimming threshold automatically.
        
        #set thresh to .01% of the data set seconds
        if thresh == None: 
            thresh= (tend-tstart)*.001
            if thresh < 300: thresh = 300

        
        for i in range(len(inds)):
            if diffs[i] > thresh: 
                push = pads
                push_NR = pads
            else: 
                push    = self.out[inds[i]]
                push_NR = self.out_NR[inds[i]]
            nout.append(push)
            nout_NR.append(push_NR)
            ntrt.append(sum(push))
        
        self.toff = toff
        self.ntimes = dt
        self.ntots = array(ntrt)
        self.nout = array(nout).T #our fixed array
        self.nout_NR = array(nout_NR).T #our fixed array

    def plot_intensity(self):
            if self.toff != None:
                t0 = self.toff
            else:
                t0 = self.ntimes[0]
            ta = (self.ntimes-t0)/3600
            plot(ta,self.ntots,'k')
            yticks([])
            ylabel("Total Amplitude")
            xlim(ta[0],ta[-1])
            xlabel("Time (h)")
            try:
                nmn = min([self.ntots[ii] for ii in self.ntots.nonzero()[0]])
                nmx = max([self.ntots[ii] for ii in self.ntots.nonzero()[0]])
                ylim(nmn,nmx)
            except Exception as E: 
                #print E
                nomin = True


    def tof_map(self,ccm=cm.jet,transpose=False,rectify=True,vminval=0,vmaxval=255,doplot=True,interp='nearest'):
        #find key that smells like delay
        keys = self.meta.keys()
        delay = 0
        for k in keys: 
            if k.lower().find("delay") >-1:
                delay = int(self.meta[k])
                break

        y_init = range(0,len(self.nout),len(self.nout)/5)
        y_init.append(len(self.nout))
        y_out  = delay+(array(y_init)*float(self.meta['dtus'])).round(1)

        #get test time limits
        x_init = range(0,len(self.ntimes),len(self.ntimes)/5)
        
        if (float(x_init[-1])/len(self.ntimes)) < .9:
            x_init.append(len(self.ntimes))
        x_out = mean(diff(self.ntimes))*array(x_init)
        x_out = (x_out/3600).round(1)
        
        #Decide whether to transpose and rectify
        if (transpose==False) and (rectify==False):
            thing_to_plot = self.nout
        
        elif (transpose==False) and (rectify==True):
            thing_to_plot = self.nout_NR
            
        elif (transpose==True) and (rectify==False):
            thing_to_plot = self.nout.T
            
        elif (transpose==True) and (rectify==True):
            thing_to_plot = self.nout_NR.T
            
        #Plot it   
        if doplot:
            imshow(thing_to_plot,aspect="auto",interpolation=interp,extent=[x_out[0],x_out[-1],y_out[-1],y_out[0]],cmap=ccm,vmin=vminval,vmax=vmaxval)
            # yticks(y_init,y_out)
            ylabel("Time of Flight (us)")
            # xticks(x_init,x_out)
            xlabel("Test Time (hr)")
            # print y_init
            # print y_out
        
        self.plotimg = thing_to_plot    



# if __name__ == "__main__":

#     print "Uncompensated Data"
#     run = "20160711_P_LCO_1500_2C_12_g3a_6_PE"
    
#     d = EASI(run,debug=True)

#     print d.cursor.count()



#     imshow(list(d.raw['amp']),aspect="auto")
#     showme()
#     clf()
    
#     print d.meta.keys()
#     print "Compensated Data"
#     d.time_correct()
#     d.tof_map() #imshow(d.nout,aspect="auto")
#     showme()
#     clf()

#     print "Compensated Data"
#     d.time_correct()
#     d.tof_map(ccm=cm.gray) #imshow(d.nout,aspect="auto")
#     showme()
#     clf()


#     print "Compensated Insentisy Plot"
#     plot(d.ntots)
#     nmn = min([d.ntots[ii] for ii in d.ntots.nonzero()[0]])
#     nmx = max([d.ntots[ii] for ii in d.ntots.nonzero()[0]])
#     ylim(nmn,nmx)
#     #xlim(0,len(d.tc['nout'].iloc[-1]))
#     showme()
#     clf()