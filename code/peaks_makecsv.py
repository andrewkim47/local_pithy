from Histogram_Band import *
import peakutils
from peakutils.plot import plot as pplot
from scipy.interpolate import interp1d


def FWHM(x,y,n=1000):
    X = linspace(x[0],x[-1],n)
    f = interp1d(x,y)
    Y = f(X)
    
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
    'FU_D_CT',
    'FU_D_RT',
    'FU_D_WT',
    
    'ER_D_CT',
    'ER_D_RT',
    'ER_D_WT',
    
    'QU_D_CT',
    'QU_D_RT',
    'QU_D_WT',
    
    'CP_D_CT',
    'CP_D_RT',
    'CP_D_WT',
    
    'EN_D_CT',
    'EN_D_RT',
    'EN_D_WT',
    
    'EA_D_CT',
    'EA_D_RT',
    'EA_D_WT',
]

d = dict()
ys = dict()

for key in kees:    
    numband = 5
    fdir = '/Users/andrewkim/Documents/AA_Discharge/TIFFS/'
    code = datas[key]['code']
    folder = fdir + code + '/Histogram/'
    endp = datas[key]['endpoint']
    ndata,adata,bands = getBandHist(folder)
    datas[key]['zband'] = mergeBand(ndata,endp[0],endp[1],numband)
    datas[key]['Zband'] = mergeBand(ndata,endp[0],endp[1],numband,norm=False) #raw
    x = arange(256)
    
    
    d[key] = dict()
    ys[key] = dict()
    
    # df[key] = 
    for n in range(numband):
        # y = array(datas[key]['zband'][n])
        ynorm = array(datas[key]['zband'][n])
        y = array(datas[key]['Zband'][n])
        ys[key][n] = y
        idxs = peakutils.indexes(y,thres=.9,min_dist=25)
        iidxs = peakutils.interpolate(x, y, ind=idxs)

        idx = idxs[0]
        xi = iidxs[0]
        yi = y[int(round(xi))]
        wid = FWHM(x,y)/2.
        
        if len(idxs)>1: 
            print key,n,'more than 1 peak'
            print idxs
        elif len(idxs)<1: 
            print key,n,'less than 1 peak'
        # print idxs,iidxs,wid
        # d[key]['label'] = key
        d[key]['px'+str(n)] = xi
        d[key]['py'+str(n)] = yi
        d[key]['pw'+str(n)] = wid 
        d[key]['me'+str(n)] = sum(multiply(x,ynorm)) #weighted mean pixel
    
        # print d[key]['me'+str(n)]
        plot(x,y)
        plot(idxs,y[idxs],'ro')
    showme()
    clf()
        

fdir2 = '/Users/andrewkim/Documents/AA_Discharge/data/'    
df = pd.DataFrame.from_dict(d)
df.to_csv(fdir2+'peaks_abs.csv')

    # print a
    # ds.append(pd.DataFrame.from_dict(d))

# print pd.concat(ds)
#     # df[key] = pd.DataFrame(d,dtype=None)
#     df[key] = pd.DataFrame.from_dict(d)
# print df    