from Histogram_Band import *
from lmfit.models import PseudoVoigtModel

bins = range(256)

fdir = '/Users/andrewkim/Documents/AA_Discharge/TIFFS/'

x = arange(256)

#Grab Data

key = 'CP_D_RT'
code = datas[key]['code']
folder = fdir + code + '/Histogram/'
endp = datas[key]['endpoint']
ndata,adata,bands = getBandHist(folder)


####################################
############ FIRST PASS , grab peak positions
####################################

# numband = 1
# datas[key]['zband'] = mergeBand(ndata,endp[0],endp[1],numband)

# #Y = Total Histogram of Zinc:
# band = 0
# Y = array(mergeBand(ndata,endp[0],endp[1],1)[band])
# y = Y


# pv1 = PseudoVoigtModel(prefix='pv1_')
# pars = pv1.guess(y, x=x)
# pars['pv1_amplitude'].set(0.33,min=0)
# pars['pv1_sigma'].set(13)
# pars['pv1_center'].set(73.9)
# pars['pv1_fraction'].set(0.10)
# pars['pv1_fwhm'].set(50)
# pars['pv1_height'].set(0.05)

# pv2 = PseudoVoigtModel(prefix='pv2_')
# pars.update(pv2.make_params())
# pars['pv2_amplitude'].set(0.33,min=0)
# pars['pv2_sigma'].set(13)
# pars['pv2_center'].set(88.7)
# pars['pv2_fraction'].set(0.10)
# pars['pv2_fwhm'].set(50)
# pars['pv2_height'].set(0.05)


# pv3 = PseudoVoigtModel(prefix='pv3_')
# pars.update(pv3.make_params())
# pars['pv3_amplitude'].set(0.33,min=0)
# pars['pv3_sigma'].set(13)
# pars['pv3_center'].set(112.)
# pars['pv3_fraction'].set(0.10)
# pars['pv3_fwhm'].set(50)
# pars['pv3_height'].set(0.05)



# # mod = pv1
# mod = pv1 + pv2 + pv3
# init = mod.eval(pars, x=x)
# out = mod.fit(y, pars, x=x)
# comps = out.eval_components(x=x)


# figure(figsize=(6.4,4.8*3))
# subplot(6,1,1)
# plot(x,y,lw=3)
# plot(x,out.best_fit,c='k',lw=3,ls='--')
# for subkey in comps.keys():
#     plot(x,comps[subkey],ls='--')
# # title(key+'_B'+str(band))
# title(key+ ' Total Zinc Region')
# grid()
# xlim(50,200)
# # showme()
# # clf()

# results = out.fit_report(min_correl=0.5)
# print results.split('[[')[3]


# numband = 5
# datas[key]['zband'] = mergeBand(ndata,endp[0],endp[1],numband)

# for band in range(5):
# # for band in [0,4]:
#     y = array(datas[key]['zband'][band])
    
#     # mod = pv1
#     mod = pv1 + pv2 + pv3
#     init = mod.eval(pars, x=x)
#     out = mod.fit(y, pars, x=x)
#     comps = out.eval_components(x=x)
    
    
#     subplot(6,1,band+2)
#     plot(x,y,lw=3)
#     plot(x,out.best_fit,c='k',lw=3,ls='--')
#     for subkey in comps.keys():
#         plot(x,comps[subkey],ls='--')
#     # title(key+'_B'+str(band))
#     title(key+ ' Zinc SubRegion '+str(band))
#     grid()
#     xlim(50,200)
#     results = out.fit_report(min_correl=0.5)
#     print results.split('[[')[3]
    
# tight_layout()    
# showme()
# clf()


# # ####################################
# # ############ 2nd pass
# # ####################################

numband = 1
datas[key]['zband'] = mergeBand(ndata,endp[0],endp[1],numband)

#Y = Total Histogram of Zinc:
band = 0
Y = array(mergeBand(ndata,endp[0],endp[1],1)[band])
y = Y

pv1 = PseudoVoigtModel(prefix='pv1_')
pars = pv1.guess(y, x=x)
pars['pv1_amplitude'].set(0.27,min=0)
pars['pv1_sigma'].set(16)
pars['pv1_center'].set(73.9, vary = False)
pars['pv1_fraction'].set(0.10)
pars['pv1_fwhm'].set(50)
pars['pv1_height'].set(0.03)

pv2 = PseudoVoigtModel(prefix='pv2_')
pars.update(pv2.make_params())
pars['pv2_amplitude'].set(0.39,min=0)
pars['pv2_sigma'].set(13)
pars['pv2_center'].set(88.7, vary = False)
pars['pv2_fraction'].set(0.10)
pars['pv2_fwhm'].set(50)
pars['pv2_height'].set(0.05)


pv3 = PseudoVoigtModel(prefix='pv3_')
pars.update(pv3.make_params())
pars['pv3_amplitude'].set(0.34,min=0)
pars['pv3_sigma'].set(12)
pars['pv3_center'].set(112., vary = False)
pars['pv3_fraction'].set(0.10)
pars['pv3_fwhm'].set(50)
pars['pv3_height'].set(0.05)



# mod = pv1
mod = pv1 + pv2 + pv3
init = mod.eval(pars, x=x)
out = mod.fit(y, pars, x=x)
comps = out.eval_components(x=x)


figure(figsize=(6.4,4.8*3))
subplot(6,1,1)
plot(x,y,lw=3)
plot(x,out.best_fit,c='k',lw=3,ls='--')
for subkey in comps.keys():
    plot(x,comps[subkey],ls='--')
# title(key+'_B'+str(band))
title(key+ ' Total Zinc Region')
grid()
xlim(50,150)
# showme()
# clf()

results = out.fit_report(min_correl=0.5)
print results.split('[[')[3]


numband = 5
datas[key]['zband'] = mergeBand(ndata,endp[0],endp[1],numband)
print array_split(arange(endp[0],endp[1]),numband)

for band in range(5):
# for band in [0,4]:
    y = array(datas[key]['zband'][band])
    
    # mod = pv1
    mod = pv1 + pv2 + pv3
    init = mod.eval(pars, x=x)
    out = mod.fit(y, pars, x=x)
    comps = out.eval_components(x=x)
    
    
    subplot(6,1,band+2)
    plot(x,y,lw=3)
    plot(x,out.best_fit,c='k',lw=3,ls='--')
    for subkey in comps.keys():
        plot(x,comps[subkey],ls='--')
    # title(key+'_B'+str(band))
    title(key+ ' Zinc SubRegion '+str(band))
    grid()
    xlim(50,150)
    results = out.fit_report(min_correl=0.5)
    print results.split('[[')[3]
    
tight_layout()    
showme()
clf()
