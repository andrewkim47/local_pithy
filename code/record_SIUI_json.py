from pithy import *
from libSIUI import SIUI
from urllib import urlopen
from pithy import *
from time import time,sleep

import json
# import simplejson as json
# import pandas
import pickle
import os

# print sys.path
site = 'http://localhost:9008'
s1 = SIUI(site)
s2 = SIUI(site)

def gainSet(gain):
    return urlopen(site+"/setGain/%f" % gain).read()

s1.vset = 400
s1.gain = 34
s1.rng = 30
s1.pw = 200
s1.rect = 'rf'
s1.prf = 100
s1.freq= '0.5_10MHz'
s1.mode = 'TR'
s1.vel = 4000

s2.vset = 400
s2.gain = 68
s2.rng = 30
s2.pw = 200
s2.rect = 'rf'
s2.prf = 100
s2.freq= '0.5_10MHz'
s2.mode = 'PE'
s2.vel = 4000
# s2.setGetCheck()

tests =[
    s1,
    s2
    ]
try:
    for test in tests:
        data = test.setGetCheck()
        # print data

        # data=test.getData()
        filedir = 'files/SIUITest/'
        fname = 'test'+str(time())+'.json'
        filename = filedir+fname
        
        #Please json interperator 
        datatowrite = dict()
        datatowrite['prf'] = int(data['prf'])
        datatowrite['pw'] = int(data['pw'])
        datatowrite['power'] = int(data['power'])
        datatowrite['freq'] = data['freq']
        datatowrite['damp'] = int(data['damp'])
        datatowrite['wave'] = list([int(i) for i in data['wave']])
        datatowrite['delay'] = float(data['delay'])
        datatowrite['volt'] = int(data['volt'])
        datatowrite['range'] = float(data['range'])
        datatowrite['gain'] = float(data['gain'])
        datatowrite['sets'] = list(data['sets'])
        datatowrite['x'] = list(data['x'])
        datatowrite['vel'] = int(data['vel'])
        datatowrite['vel2'] = int(data['vel2'])
        datatowrite['rect'] = data['rect']
        datatowrite['mode'] = data['mode']
        
        with open(filename,'w') as ofile:
            json.dump(datatowrite,ofile)
        sleep(3)
except Exception as E:
    print E