from pithy import *
import serial
import numpy
from time import sleep
import pandas as pd
import timeit


#Guide here http://www.batronix.com/pdf/Rigol/ProgrammingGuide/DS1000DE_ProgrammingGuide_EN.pdf


ser = serial.Serial( 
port='/dev/tty.usbserial-AI0252YA', 
baudrate=38400,
parity=serial.PARITY_NONE, 
stopbits=serial.STOPBITS_ONE, 
bytesize=serial.EIGHTBITS,
timeout=1
) 

def ask(cmd):
    ser.write(cmd+'\n')
    time.sleep(.3)
    return ser.readline()
    
def awrite(cmd):
    ser.write(cmd+'\n')
    time.sleep(.3)
    ser.readline()
    
    
# fildir = '/Users/akim/pithy/files/STIM300/'


def rawread(chan,run=True):
    channel = "CHAN"+str(chan)
    rawdata = ask(":WAV:DATA? "+channel)
    data = numpy.frombuffer(rawdata, 'B')[10:-2]
    return data

awrite(":WAV:POIN:MODE RAW")
time.sleep(.3)
print ask(':WAV:POIN:MODE?')
time.sleep(1)

awrite(':STOP')
data = rawread(1)
plot(data)
showme()

# print ask(':ACQuire:TYPE?')
# awrite(':ACQuire:TYPE AVER')

# tstart = time.time()
# n=10
# #10 times 1.8

# allreads=[]
# for i in range(n):
#     # rawread(1)
#     allreads.append(rawread(1))
#     # sleep(.1)
# print n, ' times took',  time.time()-tstart, 'secs'
