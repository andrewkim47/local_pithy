from Histogram_Band import *

fdir = '/Users/andrewkim/Documents/AA_Discharge/TIFFS/CP_B1_C_WT_TIFF/Histogram/'
bins = range(256)
datas,ndatas,bands = getBandHist(fdir)

band = mergeBand(datas,5,26,5)
plot(band[0],label=0)
plot(band[1],label=1)
plot(band[2],label=2)
plot(band[3],label=3)
plot(band[4],label=4)
legend()
showme()
clf()

