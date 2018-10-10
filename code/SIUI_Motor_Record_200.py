from pithy import *
from urllib import urlopen as uo
from libSIUI import SIUI
from time import sleep,time,strftime
import ast
import json
import os

site = 'http://localhost:9004'
Uno = "http://localhost:9002" #needs NF

s1 = SIUI(site)
s2 = SIUI(site)

def gainSet(gain):
    return uo(site+"/setGain/%f" % gain).read()

#write to serial port (expects 0 to 255)
def awrite(val):
    uo(Uno+"/writecf/"+str(val)).read()
    sleep(.5)

def aread():
    return uo(Uno+"/read/").read()
    
def runMotor(motor,direction,style,spd,steps):
    outstring = "M"+str(motor)+str(direction)+str(style)+str(speed).zfill(4)+str(steps).zfill(5)
    # print "Running Motor"
    # print "Mot: ", str(motor)
    # print "Dir: ", str(direction)
    # print "Sty: ", str(style)
    # print "Spd: ", str(speed).zfill(4)
    # print "Stp: ", str(steps).zfill(5)
    # print "\n"
    # print outstring
    awrite(outstring)
    sleep(0.5)

mot = 3 #1 or 3
style = 1 #1 single, 2 double, 3 interleaved, 4 micros
speed = 10 
dirx = 2 #1 Left / 2 Right
# steps = 200
#right side = Transmit

s1.vset = 400
s1.gain = 78
s1.rng = 100
s1.pw = 200
s1.rect = 'rf'
s1.prf = 100
s1.freq= '0.5_10MHz'
s1.mode = 'TR'
s1.vel = 4000

data = s1.setGetCheck()


numpoints = 601
steps = [int(i) for i in linspace(0,numpoints-1,numpoints)]
diffsteps = diff(steps)

# try:
for j in range(numpoints):
    step = steps[j]
    
    #Get Data
    data = s1.getData()
    
    #Please the picky json interperator 
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
    
    #Save Data
    filedir = 'files/SIUITest/ClemSpring/188-1/'
    fname = '188-1_ClemSpring_'+str(step).zfill(3)+'_'+str(time())+'.json'
    filename = filedir+fname
    with open(filename,'w') as ofile:
        json.dump(datatowrite,ofile)
    
    
    #Move motor unless it's the last point

    
    if j==numpoints-1:
        print 'done'
    else:
        delta = diffsteps[j]
        runMotor(mot,dirx,style,speed,delta)
        print step,
        if mod(step,20)==19: print 
            
# except Exception as E:
#     print E

