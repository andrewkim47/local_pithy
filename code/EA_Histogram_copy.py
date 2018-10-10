from Histogram_Band import *
bins = range(256)
numband = 5

fdir = '/Users/andrewkim/Documents/AA_Discharge/TIFFS/'

fidir1 = fdir+'EA_B1_C_WT_TIFF/Histogram/'
ndata1,adata1,bands = getBandHist(fidir1)
zband1 = mergeBand(ndata1,5,27,numband)
mband1 = mergeBand(ndata1,30,46,numband)

fidir2 = fdir+'EA_B1_D_WT_TIFF/Histogram/'
ndata2,adata2,bands = getBandHist(fidir2)
zband2 = mergeBand(ndata2,5,26,numband) 
mband2 = mergeBand(ndata2,29,46,numband) 

fidir3 = fdir+'EA_C1_C_RT_TIFF/Histogram/'
ndata3,adata3,bands = getBandHist(fidir3)
zband3 = mergeBand(ndata3,6,27,numband,norm=True)
mband3 = mergeBand(ndata3,30,46,numband,norm=True)

fidir4  = fdir+'EA_C1_D_RT_TIFF/Histogram/'
ndata4,adata4,bands = getBandHist(fidir4)
zband4 = mergeBand(ndata4,5,25,numband,norm=True)
mband4 = mergeBand(ndata4,28,46,numband,norm=True)

fidir5 = fdir+'EA_C1R_C_CT_TIFF/Histogram/'
ndata5,adata5,bands = getBandHist(fidir5)
zband5 = mergeBand(ndata5,6,27,numband,norm=True)
mband5 = mergeBand(ndata5,30,46,numband,norm=True)

fidir6 = fdir+'EA_C1R_D_CT_TIFF/Histogram/'
ndata6,adata6,bands = getBandHist(fidir6)
zband6 = mergeBand(ndata6,7,25,numband,norm=True)
mband6 = mergeBand(ndata6,27,46,numband,norm=True)


#####
#####
subplot(211)
title('EcoAdvanced Warm Charged Zn')
for i in range(numband):
    plot(zband1[i],label=i)
    legend()
xlabel('Pixel Value')    
ylabel('Relative Counts')
xlim(-5,260)
subplot(212)
title('EcoAdvanced Warm Discharged Zn')
for i in range(numband):
    plot(zband2[i],label=i)
    legend()
xlabel('Pixel Value')    
ylabel('Relative Counts')
xlim(-5,260)
tight_layout()
showme()
clf()

subplot(211)
title('EcoAdvanced Warm Charged Mn')
for i in range(numband):
    plot(mband1[i],label=i)
    legend()
xlabel('Pixel Value')    
ylabel('Relative Counts')
xlim(-5,260)
subplot(212)
title('EcoAdvanced Warm Discharged Mn')
for i in range(numband):
    plot(mband2[i],label=i)
    legend()
xlabel('Pixel Value')    
ylabel('Relative Counts')
xlim(-5,260)
tight_layout()
showme()
clf()

#####
#####
subplot(211)
title('EcoAdvanced Room Charged Zn')
for i in range(numband):
    plot(zband3[i],label=i)
    legend()
xlabel('Pixel Value')    
ylabel('Relative Counts')
xlim(-5,260)
subplot(212)
title('EcoAdvanced Room Discharged Zn')
for i in range(numband):
    plot(zband4[i],label=i)
    legend()
xlabel('Pixel Value')    
ylabel('Relative Counts')
xlim(-5,260)
tight_layout()
showme()
clf()

subplot(211)
title('EcoAdvanced Room Charged Mn')
for i in range(numband):
    plot(mband3[i],label=i)
    legend()
xlabel('Pixel Value')    
ylabel('Relative Counts')
xlim(-5,260)
subplot(212)
title('EcoAdvanced Room Discharged Mn')
for i in range(numband):
    plot(mband4[i],label=i)
    legend()
xlabel('Pixel Value')    
ylabel('Relative Counts')
xlim(-5,260)
tight_layout()
showme()
clf()

#####
#####
subplot(211)
title('EcoAdvanced Cold Charged Zn')
for i in range(numband):
    plot(zband5[i],label=i)
    legend()
xlabel('Pixel Value')    
ylabel('Relative Counts')
xlim(-5,260)
subplot(212)
title('EcoAdvanced Cold Discharged Zn')
for i in range(numband):
    plot(zband6[i],label=i)
    legend()
xlabel('Pixel Value')    
ylabel('Relative Counts')
xlim(-5,260)
tight_layout()
showme()
clf()

subplot(211)
title('EcoAdvanced Cold Charged Mn')
for i in range(numband):
    plot(mband5[i],label=i)
    legend()
xlabel('Pixel Value')    
ylabel('Relative Counts')
xlim(-5,260)
subplot(212)
title('EcoAdvanced Cold Discharged Mn')
for i in range(numband):
    plot(mband6[i],label=i)
    legend()
xlabel('Pixel Value')    
ylabel('Relative Counts')
xlim(-5,260)
tight_layout()
showme()
clf()

