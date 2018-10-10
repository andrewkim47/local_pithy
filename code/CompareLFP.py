from pithy import *
from libSIUI import SIUI
from urllib import urlopen
from pithy import *
from time import time,sleep
# import json
import pandas
import pickle
import glob


files = glob.glob('files/Sameness_Check/*_0.pickle')
print files
datas=dict()
for i in range(len(files)):
    with open(files[i], 'rb') as handle:
        data = pickle.load(handle)
        datas[i] = data
        plot(data['x'],data['wave'],label=files[i])
# xlabel('Range mm')
# ylabel('Bits')
# title('NMC')
legend()
showme()
clf()

files = glob.glob('files/Sameness_Check/*_180.pickle')
print files
datas=dict()
for i in range(len(files)):
    with open(files[i], 'rb') as handle:
        data = pickle.load(handle)
        datas[i] = data
        plot(data['x'],data['wave'],label=files[i])
# xlabel('Range mm')
# ylabel('Bits')
# title('NMC')
legend()
showme()
clf()

files = glob.glob('files/Sameness_Check/*_360.pickle')
print files
datas=dict()
for i in range(len(files)):
    with open(files[i], 'rb') as handle:
        data = pickle.load(handle)
        datas[i] = data
        plot(data['x'],data['wave'],label=files[i])
# xlabel('Range mm')
# ylabel('Bits')
# title('NMC')
legend()
showme()
clf()