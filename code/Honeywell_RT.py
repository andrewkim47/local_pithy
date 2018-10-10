from pithy import *
import pandas as pd
from scipy.optimize import curve_fit
# # https://www.mouser.com/catalog/additional/Honeywell_135-103FAD-J01%20R_T.pdf
# fil = '/Users/andrewkim/Documents/HoneywellThermistor.txt'
# dat = pd.read_csv(fil,sep=',')
# R = array(dat['rnom'])
# T = array(dat['Temp'])+273.

# # #steinhart hart
# def SHH(r, a, b, c):
#     return a + b * log(r) + c * (log(r)**3)
  
# def R2T(r,shh):
#     tinv = shh[0] + shh[1] * log(r) + shh[2] * (log(r)**3)
#     return 1.0/tinv
    
# popt, pcov = curve_fit(SHH, R, 1.0/T)
# # print popt
# xs = linspace(532.50,40700.0)

# plot(T-273,R,'bo')
# plot(R2T(xs,popt)-273,xs,'r')
# showme()
# clf()


shh= [7.76655496e-04,2.73964154e-04,7.22722438e-08]

def R2T(r,shh=shh):
    tinv = shh[0] + shh[1] * log(r) + shh[2] * (log(r)**3)
    return 1.0/tinv

print R2T(442)-273