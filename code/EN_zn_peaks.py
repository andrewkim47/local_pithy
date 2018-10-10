from Histogram_Band import *
import peakutils
from scipy.interpolate import interp1d
from peakutils.plot import plot as pplot

bins = range(256)
numband = 5

fdir = '/Users/andrewkim/Documents/AA_Discharge/TIFFS/'

datas = dict()

datas['EN_C_WT'] = dict()
datas['EN_D_WT'] = dict()
datas['EN_C_RT'] = dict()
datas['EN_D_RT'] = dict()
datas['EN_C_CT'] = dict()
datas['EN_D_CT'] = dict()

datas['EN_C_WT']['code'] = 'EN_B1_C_WT_TIFF'
datas['EN_D_WT']['code'] = 'EN_B1_D_WT_TIFF'
datas['EN_C_RT']['code'] = 'EN_C1_C_RT_TIFF'
datas['EN_D_RT']['code'] = 'EN_RT_D_RT_TIFF'
datas['EN_C_CT']['code'] = 'EN_A1_C_CT_TIFF'
datas['EN_D_CT']['code'] = 'EN_A1_D_CT_TIFF'

datas['EN_C_WT']['endpoint'] = [7,26,30,46]
datas['EN_D_WT']['endpoint'] = [6,25,28,46]
datas['EN_C_RT']['endpoint'] = [6,25,30,45]
datas['EN_D_RT']['endpoint'] = [5,24,28,47]
datas['EN_C_CT']['endpoint'] = [6,26,30,45]
datas['EN_D_CT']['endpoint'] = [6,24,28,45]

for key in ['EN_C_WT']:
# for key in sorted(list(datas)):
    code = datas[key]['code']
    folder = fdir + code + '/Histogram/'
    endp = datas[key]['endpoint']
    ndata,adata,bands = getBandHist(folder)
    # datas[code]['ndata'] = ndata
    # datas[code]['adata'] = adata
    datas[key]['zband'] = mergeBand(ndata,endp[0],endp[1],numband)
    datas[key]['mband'] = mergeBand(ndata,endp[2],endp[3],numband)

x0 = arange(256)
y1 = array(datas['EN_C_WT']['zband'][0])
f1 = interp1d(x0,y1)



ix = peakutils.indexes(y1, thres=0.2, min_dist=30)
px = peakutils.interpolate(x0, y1, ind=ix)

pplot(x0,y1,ix)
showme()
clf()