from Histogram_Band import *
bins = range(256)
numband = 5

fdir = '/Users/andrewkim/Documents/AA_Discharge/TIFFS/'

datas = dict()

datas['EA_C_WT'] = dict()
datas['EA_D_WT'] = dict()
datas['EA_C_RT'] = dict()
datas['EA_D_RT'] = dict()
datas['EA_C_CT'] = dict()
datas['EA_D_CT'] = dict()

datas['EA_C_WT']['code'] = 'EA_B1_C_WT_TIFF'
datas['EA_D_WT']['code'] = 'EA_B1_D_WT_TIFF'
datas['EA_C_RT']['code'] = 'EA_C1_C_RT_TIFF'
datas['EA_D_RT']['code'] = 'EA_C1_D_RT_TIFF'
datas['EA_C_CT']['code'] = 'EA_C1R_C_CT_TIFF'
datas['EA_D_CT']['code'] = 'EA_C1R_D_CT_TIFF'

datas['EA_C_WT']['endpoint'] = [5,27,30,46]
datas['EA_D_WT']['endpoint'] = [5,26,29,46]
datas['EA_C_RT']['endpoint'] = [6,27,30,46]
datas['EA_D_RT']['endpoint'] = [5,25,28,46]
datas['EA_C_CT']['endpoint'] = [6,27,30,46]
datas['EA_D_CT']['endpoint'] = [7,25,27,46]

# for i in sorted(list(datas)): print i

for key in sorted(list(datas)):
    code = datas[key]['code']
    folder = fdir + code + '/Histogram/'
    endp = datas[key]['endpoint']
    ndata,adata,bands = getBandHist(folder)
    # datas[code]['ndata'] = ndata
    # datas[code]['adata'] = adata
    datas[key]['zband'] = mergeBand(ndata,endp[0],endp[1],numband)
    datas[key]['mband'] = mergeBand(ndata,endp[2],endp[3],numband)


#####
#####
figure(figsize=(6.4*1.5,4.8*1.5))
key = 'EA_C_CT'
subplot(221)
title(key+' Zn')
for i in range(numband):
    plot(datas[key]['zband'][i],label=i)
    legend()
xlabel('Pixel Value')    
ylabel('Relative Counts')
xlim(-5,260)

subplot(222)
title(key+' Mn')
for i in range(numband):
    plot(datas[key]['mband'][i],label=i)
    legend()
xlabel('Pixel Value')    
ylabel('Relative Counts')
xlim(-5,260)

key = 'EA_D_CT'
subplot(223)
title(key+' Zn')
for i in range(numband):
    plot(datas[key]['zband'][i],label=i)
    legend()
xlabel('Pixel Value')    
ylabel('Relative Counts')
xlim(-5,260)

subplot(224)
title(key+' Mn')
for i in range(numband):
    plot(datas[key]['mband'][i],label=i)
    legend()
xlabel('Pixel Value')    
ylabel('Relative Counts')
xlim(-5,260)

tight_layout()
showme()
clf()

#####
#####
figure(figsize=(6.4*1.5,4.8*1.5))
key = 'EA_C_RT'
subplot(221)
title(key+' Zn')
for i in range(numband):
    plot(datas[key]['zband'][i],label=i)
    legend()
xlabel('Pixel Value')    
ylabel('Relative Counts')
xlim(-5,260)

subplot(222)
title(key+' Mn')
for i in range(numband):
    plot(datas[key]['mband'][i],label=i)
    legend()
xlabel('Pixel Value')    
ylabel('Relative Counts')
xlim(-5,260)

key = 'EA_D_RT'
subplot(223)
title(key+' Zn')
for i in range(numband):
    plot(datas[key]['zband'][i],label=i)
    legend()
xlabel('Pixel Value')    
ylabel('Relative Counts')
xlim(-5,260)

subplot(224)
title(key+' Mn')
for i in range(numband):
    plot(datas[key]['mband'][i],label=i)
    legend()
xlabel('Pixel Value')    
ylabel('Relative Counts')
xlim(-5,260)

tight_layout()
showme()
clf()

#####
#####
figure(figsize=(6.4*1.5,4.8*1.5))
key = 'EA_C_WT'
subplot(221)
title(key+' Zn')
for i in range(numband):
    plot(datas[key]['zband'][i],label=i)
    legend()
xlabel('Pixel Value')    
ylabel('Relative Counts')
xlim(-5,260)

subplot(222)
title(key+' Mn')
for i in range(numband):
    plot(datas[key]['mband'][i],label=i)
    legend()
xlabel('Pixel Value')    
ylabel('Relative Counts')
xlim(-5,260)

key = 'EA_D_WT'
subplot(223)
title(key+' Zn')
for i in range(numband):
    plot(datas[key]['zband'][i],label=i)
    legend()
xlabel('Pixel Value')    
ylabel('Relative Counts')
xlim(-5,260)

subplot(224)
title(key+' Mn')
for i in range(numband):
    plot(datas[key]['mband'][i],label=i)
    legend()
xlabel('Pixel Value')    
ylabel('Relative Counts')
xlim(-5,260)

tight_layout()
showme()
clf()
