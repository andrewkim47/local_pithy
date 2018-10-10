from pithy import *
import serial

shh= [7.76655496e-04,2.73964154e-04,7.22722438e-08]

def R2T(r,shh=shh):
    tinv = shh[0] + shh[1] * log(r) + shh[2] * (log(r)**3)
    return (1.0/tinv)-273

def rval(aval):
    return 9960 * (1024./aval-1)
    
def rval2(aval):
    return 9960 * (4096./aval-1)
    
# s = serial.Serial('/dev/tty.usbmodem1421',57600)
# val = float(s.readline())


# val = 450#610
# r = rval(val)

# print val
# print rval(val)
# print R2T(r)

# val = 472#610
# r = rval(val)

# print val
# print rval(val)
# print R2T(r)
482332,1252,1237,1217,1889,1386,1141


val = 1889#610
r = rval2(val)

print val
print rval(val)
print R2T(r)




