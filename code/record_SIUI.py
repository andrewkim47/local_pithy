from pithy import *
from libSIUI import SIUI
from urllib import urlopen
from pithy import *
from time import time,sleep
# import json
import pandas
import pickle
import os

# print sys.path
site = 'http://localhost:9008'
s = SIUI(site)

def gainSet(gain):
    return urlopen(site+"/setGain/%f" % gain).read()

# #Set initial parameters
# s.vset = 400
# s.gain = 34
# s.rng = 30
# s.pw = 500
# s.rect = 'rf'
# s.prf = 100
# s.freq= '0.5_10MHz'
# s.mode = 'TR'
# s.vel = 4000
# s.setGetCheck()
# s.gain = 40
# data2 = s.setGetCheck()

#Transmit on the right (anode bottom)
# urlopen(site+"/setGain/%f" % 30).read()
# gainSet(20)

#84dB
#barcode towards ceiling = 0, + up, - down (towards me), clockwise
filename = 'files/Sameness_Check/S6_360.pickle'
if os.path.isfile(filename):
    print 'Name exists!'
else:
    data=s.getData()
    plot(data['x'],data['wave'])
    showme()
    with open(filename, 'wb') as handle:
      pickle.dump(data, handle)
    
    # with open(filename, 'wb') as handle:
    #   data = pickle.load(data, handle)

    