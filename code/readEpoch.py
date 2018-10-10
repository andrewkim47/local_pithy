from pithy import *
from urllib import urlopen as uo
import ast
from time import sleep,time,strftime

NF = "http://localhost:9004" #needs NF

#write to serial port (expects 0 to 255)
def Nwrite(val):
    uo(NF+"/writecf/"+str(val)).read()
    sleep(.5)

def Nread():
    return uo(NF+"/read/").read()
    

# Nwrite('param_WaveForm?')
# Nwrite('BRDTEMP?')
data = Nread().split('\r\n')

print data[-3]

