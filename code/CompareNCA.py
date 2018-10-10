from pithy import *
from libSIUI import SIUI
from urllib import urlopen
from pithy import *
from time import time,sleep
# import json
import pandas
import pickle
import glob

# files = sorted(glob.glob('files/4NCA/*.pickle'))
# names = [i.split('/')[-1].split('.')[0] for i in files]
# print files
# for i in range(len(files)):
#     with open(files[i], 'rb') as handle:
#       data = pickle.load(handle)
#       plot(data['x'],data['wave'],label=names[i])
# legend()
# showme()
# clf()

#NCR (green)
#A7 
#B3
#C2 

#NMC's (blue)
#D1 
#E10
#F4
#G10
#E5(delay) 



files = [
# 'files/4NCA/A7.pickle',
# 'files/4NCA/B3.pickle',
# 'files/4NCA/C2.pickle',

# 'files/4NCA/D1.pickle',
# 'files/4NCA/E11.pickle',
'files/4NCA/F4.pickle',
# 'files/4NCA/G5.pickle',
'files/4NCA/G9.pickle',
# 'files/4NCA/G10.pickle',
# 'files/4NCA/D1.pickle',

]
names = [i.split('/')[-1].split('.')[0] for i in files]
datas=dict()
for i in range(len(files)):
    with open(files[i], 'rb') as handle:
        data = pickle.load(handle)
        datas[i] = data
        # plot(data['x'],data['wave'],label=names[i])
# xlabel('Range mm')
# ylabel('Bits')
# title('NMC')
# legend()
# showme()
# clf()

plot(datas[0]['x'],datas[0]['wave'],label=names[0])
plot(datas[1]['x']-1,datas[1]['wave'],label=names[1])
# plot(datas[2]['x'],datas[2]['wave'],label=names[2])
# title('NCA')
title('NMC')
xlabel('Range mm')
ylabel('Bits')

legend()
showme()
clf()
