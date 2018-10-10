from Histogram_Band import *
import peakutils
from peakutils.plot import plot as pplot

def FWHM(X,Y):
    half_max = max(Y) / 2.
    #find when function crosses line half_max (when sign of diff flips)
    #take the 'derivative' of signum(half_max - Y[])
    d = sign(half_max - array(Y[0:-1])) - sign(half_max - array(Y[1:]))
    #plot(X[0:len(d)],d) #if you are interested
    #find the left and right most indexes
    left_idx = find(d > 0)[0]
    right_idx = find(d < 0)[-1]
    return X[right_idx] - X[left_idx] #return the difference (full width)

kees = [
    'EN_D_CT',
    'EN_D_RT',
    'EN_D_WT',
    ]

for key in kees:    
    numband = 5
    fdir = '/Users/andrewkim/Documents/AA_Discharge/TIFFS/'
    code = datas[key]['code']
    folder = fdir + code + '/Histogram/'
    endp = datas[key]['endpoint']
    ndata,adata,bands = getBandHist(folder)
    datas[key]['zband'] = mergeBand(ndata,endp[0],endp[1],numband)
    x = arange(256)
    
    for n in range(numband):
        y = array(datas[key]['zband'][n])
    
        idxs = peakutils.indexes(y,thres=.7,min_dist=25)
        peaks_x = peakutils.interpolate(x, y, ind=idxs)

        print idxs,peaks_x
        idx = idxs[0]
        adx = peaks_x[0]
        wid = FWHM(x,y)/2.
        
        plot(x,y)
        plot(idx,y[idx],'ro')
        plot(adx,y[int(adx)],'bo')
        # plot([idx-wid,idx+wid],[max(y)/2.,max(y)/2.])
    title(key)
    showme()
    clf()
    # peakind = signal.find_peaks_cwt(