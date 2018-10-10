from pithy import *
from libSIUI import SIUI
from urllib import urlopen
from pithy import *
from time import time,sleep
# import json
import pandas
import pickle

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


# urlopen(site+"/setGain/%f" % 30).read()
# gainSet(20)

data=s.getData()
plot(data['x'],data['wave'])
showme()

#18650: + on top, - on bottom, angle is clockwise
#0 degrees: barcode on the left transducer
#180: barcode on right transducer
filename = 'files/SIUI/NoBattery.pickle'

with open(filename, 'wb') as handle:
  pickle.dump(data, handle)

