from Histogram_Band import *
from lmfit.models import PseudoVoigtModel

bins = range(256)
numband = 5

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

# kees = [
    # 'CP_C_WT',
    # ]

# for key in kees:
# for key in sorted(list(datas)):

key = 'CP_C_WT'
code = datas[key]['code']
folder = fdir + code + '/Histogram/'
endp = datas[key]['endpoint']
ndata,adata,bands = getBandHist(folder)
datas[key]['zband'] = mergeBand(ndata,endp[0],endp[1],numband)
datas[key]['mband'] = mergeBand(ndata,endp[2],endp[3],numband)
y = array(datas[key]['zband'][0])


pv1 = PseudoVoigtModel(prefix='pv1_')
pars = pv1.guess(y, x=x)

pars['pv1_amplitude'].set(1)
pars['pv1_sigma'].set(13)
pars['pv1_center'].set(100)
pars['pv1_fraction'].set(0.10)
pars['pv1_fwhm'].set(25)
pars['pv1_height'].set(0.04)

mod = pv1 #+ pv2
init = mod.eval(pars, x=x)
out = mod.fit(y, pars, x=x)
comps = out.eval_components(x=x)

plot(x,y,lw=3)
plot(x,out.best_fit,lw=3,ls='--')
# plot(x,comps['pv1_'])
# plot(x,comps['pv2_'])
showme()
clf()


print(out.fit_report(min_correl=0.5))



