from pithy import *
from sseclient import SSEClient
import json
import datetime
import time
from urllib import urlopen as uo
import pandas

def getdata(m):
    data = json.loads(m)
    try:
        data['data'] = json.loads(data['data'].replace("nan","-1"))
    #     data['data']['time'] = time.time()
    except Exception as E:
        print E
    return data
    

token = '626ae69cc7d2b9830b78c420058e560d670660ec'
messages = SSEClient('https://api.particle.io/v1/events/CrazyFridgeStuff?access_token=%s' %(token) )


today = str(datetime.datetime.now()).replace(' ','-')
today = today.replace(':','_')

celltype = 'Haier_Fridge_3'
Tempdir = 'files/Temperature/'
Tempname = str(today)+ '-' + celltype + '-Spark-Temperature'
fn = Tempdir + Tempname + '.csv'



for msg in messages:
    try:
        data = getdata(msg.data)
        #print data    
        now = datetime.datetime.now()
        keys = data['data'].keys()
        header = keys.sort()

        # fn = drop_pre + "KimRandom/%s.csv" % (today)

        out = ""
        h = ""
        for k in keys:
            h += "%s," % k 
            out+="%f," % data['data'][k]
        
        out = out[:-1]+"\n"
        h = h[:-1]+"\n"
        
        try:
            doof = open(fn,'r')
            open(fn,'a').write(out)
        except:
            print 'new file'
            open(fn,'a').write(h+out)
            
            

    except Exception as E:
        oof = E
        #print oof




#1331073 turn on fridge        

