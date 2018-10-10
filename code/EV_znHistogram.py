from Histogram_Band import *
bins = range(256)
numband = 5

fdir = '/Users/andrewkim/Documents/AA_Discharge/TIFFS/'


kees = [
    'ER_C_CT',    
    'ER_C_RT',    
    'ER_C_WT',    
    'ER_D_CT',    
    'ER_D_RT',    
    'ER_D_WT',    
]

for key in sorted(kees):
    code = datas[key]['code']
    folder = fdir + code + '/Histogram/'
    endp = datas[key]['endpoint']
    ndata,adata,bands = getBandHist(folder)
    # datas[code]['ndata'] = ndata
    # datas[code]['adata'] = adata
    datas[key]['zband'] = mergeBand(ndata,endp[0],endp[1],numband)
    datas[key]['mband'] = mergeBand(ndata,endp[2],endp[3],numband)
    
    datas[key]['Zband'] = mergeBand(ndata,endp[0],endp[1],numband,norm=False) #raw value
    datas[key]['aband'] = mergeBand(ndata,endp[0],endp[1],1,norm=True) #raw value

fdir2 = '/Users/andrewkim/Documents/AA_Discharge/data/'

# datas[key]['zband'][0].to_csv(fdir2+'ER_Zn_Region0_Norm.csv')
# datas[key]['zband'][1].to_csv(fdir2+'ER_Zn_Region1_Norm.csv')
# datas[key]['zband'][2].to_csv(fdir2+'ER_Zn_Region2_Norm.csv')
# datas[key]['zband'][3].to_csv(fdir2+'ER_Zn_Region3_Norm.csv')
# datas[key]['zband'][4].to_csv(fdir2+'ER_Zn_Region4_Norm.csv')
# datas[key]['Zband'][0].to_csv(fdir2+'ER_Zn_RegionAll_Norm.csv')
# datas[key]['Aband'][0].to_csv(fdir2+'ER_Zn_RegionAll_Raw.csv')

#####
#####
figure(figsize=(6.4*3,4.8*2))
key = 'ER_C_CT'
subplot(231)
title(key+' Zn')
for i in range(numband):
    plot(datas[key]['zband'][i],label=i)
plot(datas[key]['aband'][0],lw=3,c='k',label='all')    
legend(loc='best')
xlabel('Pixel Value')    
ylabel('Relative Counts')
xlim(-5,260)

key = 'ER_C_RT'
subplot(232)
title(key+' Zn')
for i in range(numband):
    plot(datas[key]['zband'][i],label=i)
plot(datas[key]['aband'][0],lw=3,c='k',label='all')    
legend(loc='best')
xlabel('Pixel Value')    
ylabel('Relative Counts')
xlim(-5,260)

key = 'ER_C_WT'
subplot(233)
title(key+' Zn')
for i in range(numband):
    plot(datas[key]['zband'][i],label=i)
plot(datas[key]['aband'][0],lw=3,c='k',label='all')    
legend(loc='best')
xlabel('Pixel Value')    
ylabel('Relative Counts')
xlim(-5,260)

key = 'ER_D_CT'
subplot(234)
title(key+' Zn')
for i in range(numband):
    plot(datas[key]['zband'][i],label=i)
plot(datas[key]['aband'][0],lw=3,c='k',label='all')    
legend(loc='best')
xlabel('Pixel Value')    
ylabel('Relative Counts')
xlim(-5,260)

key = 'ER_D_RT'
subplot(235)
title(key+' Zn')
for i in range(numband):
    plot(datas[key]['zband'][i],label=i)
plot(datas[key]['aband'][0],lw=3,c='k',label='all')    
legend(loc='best')
xlabel('Pixel Value')    
ylabel('Relative Counts')
xlim(-5,260)

key = 'ER_D_WT'
subplot(236)
title(key+' Zn')
for i in range(numband):
    plot(datas[key]['zband'][i],label=i)
plot(datas[key]['aband'][0],lw=3,c='k',label='all')    
legend(loc='best')
xlabel('Pixel Value')    
ylabel('Relative Counts')
xlim(-5,260)

tight_layout()
showme()
clf()
