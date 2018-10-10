from Histogram_Band import *
from lmfit.models import PseudoVoigtModel

bins = range(256)

fdir = '/Users/andrewkim/Documents/AA_Discharge/TIFFS/'

datas = dict()

datas['CP_C_WT'] = dict()
datas['CP_D_WT'] = dict()
datas['CP_C_RT'] = dict()
datas['CP_D_RT'] = dict()
datas['CP_C_CT'] = dict()
datas['CP_D_CT'] = dict()

datas['CP_C_WT']['code'] = 'CP_B1_C_WT_TIFF'
datas['CP_D_WT']['code'] = 'CP_B1_D_WT_TIFF'
datas['CP_C_RT']['code'] = 'CP_C1_C_RT_TIFF'
datas['CP_D_RT']['code'] = 'CP_C1_D_RT_TIFF'
datas['CP_C_CT']['code'] = 'CP_D1_C_CT_TIFF'
datas['CP_D_CT']['code'] = 'CP_D1_D_CT_TIFF'

datas['CP_C_WT']['endpoint'] = [5,25,30,46]
datas['CP_D_WT']['endpoint'] = [5,24,28,46]
datas['CP_C_RT']['endpoint'] = [4,25,31,45]
datas['CP_D_RT']['endpoint'] = [4,24,29,46]
datas['CP_C_CT']['endpoint'] = [6,25,31,46]
datas['CP_D_CT']['endpoint'] = [5,24,28,45]


x = arange(256)

#Grab Data

key = 'CP_D_WT'
code = datas[key]['code']
folder = fdir + code + '/Histogram/'
endp = datas[key]['endpoint']
ndata,adata,bands = getBandHist(folder)


# ####################################
# ############ FIRST PASS , grab peak positions
# ####################################

numband = 1
datas[key]['zband'] = mergeBand(ndata,endp[0],endp[1],numband)

#Y = Total Histogram of Zinc:
band = 0
Y = array(mergeBand(ndata,endp[0],endp[1],1)[band])
y = Y

pv1 = PseudoVoigtModel(prefix='pv1_')
pars = pv1.guess(y, x=x)
pars['pv1_amplitude'].set(0.5,min=0)
pars['pv1_sigma'].set(13)
pars['pv1_center'].set(83)
pars['pv1_fraction'].set(0.10)
pars['pv1_fwhm'].set(150)
pars['pv1_height'].set(0.05)

pv2 = PseudoVoigtModel(prefix='pv2_')
pars.update(pv2.make_params())
pars['pv2_amplitude'].set(0.5,min=0)
pars['pv2_sigma'].set(13)
pars['pv2_center'].set(100)
pars['pv2_fraction'].set(0.10)
pars['pv2_fwhm'].set(150)
pars['pv2_height'].set(0.05)



# mod = pv1
mod = pv1 + pv2
init = mod.eval(pars, x=x)
out = mod.fit(y, pars, x=x)
comps = out.eval_components(x=x)


plot(x,y,lw=3)
plot(x,out.best_fit,c='k',lw=3,ls='--')
for subkey in comps.keys():
    plot(x,comps[subkey],ls='--')
# title(key+'_B'+str(band))
title('Total Zinc Region')
showme()
clf()
print(out.fit_report(min_correl=0.5))

# # print pars
# ####################################
# ####################################
# ####################################

numband = 5
datas[key]['zband'] = mergeBand(ndata,endp[0],endp[1],numband)

#Y = Total Histogram of Zinc:
Y = array(mergeBand(ndata,endp[0],endp[1],1)[0])

# y = Y


for band in range(5):
# for band in [0,4]:
    y = array(datas[key]['zband'][band])
    
    pv1 = PseudoVoigtModel(prefix='pv1_')
    pars = pv1.guess(y, x=x)
    pars['pv1_amplitude'].set(0.50,min=0)
    pars['pv1_sigma'].set(8.6)
    pars['pv1_center'].set(83.94, vary = False)
    pars['pv1_fraction'].set(0.001)
    pars['pv1_fwhm'].set(150)
    pars['pv1_height'].set(0.05)
    
    pv2 = PseudoVoigtModel(prefix='pv2_')
    pars.update(pv2.make_params())
    pars['pv2_amplitude'].set(0.50,min=0)
    pars['pv2_sigma'].set(8.6)
    pars['pv2_center'].set(100.0, vary = False)
    pars['pv2_fraction'].set(0.4)
    pars['pv2_fwhm'].set(150)
    pars['pv2_height'].set(0.05)
    
    # mod = pv1
    mod = pv1 + pv2
    init = mod.eval(pars, x=x)
    out = mod.fit(y, pars, x=x)
    comps = out.eval_components(x=x)
    
    
    plot(x,y,lw=3)
    plot(x,out.best_fit,c='k',lw=3,ls='--')
    for subkey in comps.keys():
        plot(x,comps[subkey],ls='--')
    # title(key+'_B'+str(band))
    title('Zinc SubRegion '+str(band))
    showme()
    clf()
    print(out.fit_report(min_correl=0.5))
    
    
    
    
