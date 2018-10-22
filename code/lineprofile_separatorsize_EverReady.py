from pithy import *
import peakutils
from scipy.interpolate import interp1d

cols = []
for N in range(33):
    for L in range(17):
        cols.append('N'+str(N)+'L'+str(L))

datas = dict()
cents = dict()
edges = dict()
ydats = dict()
# labls = dict()

dropcols = ['N0L12', 'N0L13', 'N1L12', 'N1L13', 'N2L12', 'N2L13', 'N3L12', 'N3L13', 'N4L12', 'N4L13', 'N5L12', 'N5L13', 'N6L12', 'N6L13', 'N7L12', 'N7L13', 'N8L12', 'N8L13', 'N9L12', 'N9L13', 'N10L12', 'N10L13']

def loadLines(code):
    #load header files for scale ratio
    hfile = '/Users/andrewkim/Documents/AA_Discharge/TIFFS/'+code+'/Raw/Header.txt'
    hdata = open(hfile).read()
    lines = hdata.split('\r\n')
    for line in lines:
        if('Pixel' in line): scale = float(line.split('= ')[-1])/1000.
    
    #load file
    fdir = '/Users/andrewkim/Documents/AA_Discharge/TIFFS/'+code+'/Linescan/'
    fil = fdir+'Linescans_Sep16.csv'
    data = pd.read_csv(fil,sep=',')
    data = data.drop('bin',axis=1)
    if code == 'ER_B1_D_WT_TIFF':
        print 'drop'
        data = data.drop(dropcols,axis=1)
    # dat = data.mean(axis=1)
    return data,scale


def peakFind(x,y,thres=-65,min_dist=50,min_marg=0.15,up_marg=75,numpoint=1000):
    icen = []
    centers = []
    low = []
    upp = []
    
    idxs = peakutils.indexes(y,thres=thres,min_dist=min_dist,thres_abs=True)
    for i in idxs:
        if (x[i]>3.5) & (x[i]<4.5): icen.append(i)
    
    if len(icen) < 1:
        print 'No Peaks'
        #fill with zero
        center = 0
        low = 0
        upp = 0
    elif len(icen) > 1:
        print '2+ Peaks'
        #fill with zero
        center = 0
        low = 0
        upp = 0
    else: #only 1 peak found
        for ic in icen:
            # centers.append(x[ic])
            center = ic
            zcr = where(diff(signbit(diff(y))))[0] # 0 crossing
        
            zcr_lo = zcr[x[zcr]<x[ic] - min_marg] # slope 0 works good for left side
            # zcr_up = zcr[x[zcr]>x[ic] + min_margin] 
            # zcr_up = zcr[x[zcr]>x[ic] + min_margin] 
            
            dat_upp = y[ic:ic+up_marg]
            # print dat_upp
            dubdermax = argmax(diff(diff(dat_upp)))+2+ic
            
            low= zcr_lo.max()
            # upp.append(zcr_up.min())
            upp= dubdermax
                
    return center,low,upp


codes = [
# 'ER_A1_C_RT_TIFF', #thres=-53,min_dist=50,min_marg=0.15,up_marg=75
# 'ER_A1_D_RT_TIFF', #thres=-50,min_dist=50,min_marg=0.15,up_marg=75
# 'ER_B1_C_WT_TIFF', #thres=-55,min_dist=50,min_marg=0.15,up_marg=75
'ER_B1_D_WT_TIFF', #thres=-50,min_dist=50,min_marg=0.15,up_marg=75
# 'ER_C1_C_CT_TIFF', #thres=-50,min_dist=50,min_marg=0.15,up_marg=75
# 'ER_CT_D_CT_TIFF', #thres=-50,min_dist=50,min_marg=0.15,up_marg=75
]

thr = -50
mindist = 50
minmarg = 0.15
upmarg = 75


code = codes[0]

# plotFlag = True
# saveFlag = False
plotFlag = False
saveFlag = True

# ii = range(400,416)
ii = range(0,16)

data,scale = loadLines(code)
kees = list(data)
X = arange(len(data))*scale
x = linspace(X[0],X[-1],1000)

icens = []
ilows = []
iupps = []
yvals = []

idxs = range(len(kees))
for i in idxs:
    kee = kees[i]
    Y = -pd.rolling_mean(data[kee],3)
    y = interp1d(X,Y)(x)
    
    yvals.append(y)
    icen,ilow,iupp = peakFind(x,y,thr,mindist,minmarg,upmarg)
    
    icens.append(icen)
    ilows.append(ilow)
    iupps.append(iupp)

# inds = array(icens) != 0
# b = flatnonzero(a==0)

plot(x[ilows],'bo')
plot(x[icens],'ro')
plot(x[iupps],'go')
title('peak points')
# xlim(200,220)
showme()
clf()


if plotFlag == True:
    # ii = range(16)
    for i in ii:
        subplot(211)
        plot(x,-yvals[i])
        plot(x[ilows[i]],-yvals[i][ilows[i]],'bo')
        plot(x[icens[i]],-yvals[i][icens[i]],'ro')
        plot(x[iupps[i]],-yvals[i][iupps[i]],'go')
        title(i)
        # xlim(3,5)
        grid()
    
        # subplot(212)
        # plot(x[1:],diff(yvals[i]),'r')
        # plot(x[2:],diff(diff(yvals[i])),'g')
        # ylim(-5,5)
        # # xlim(3,5)
        # grid()
        
        tight_layout()
        showme()
        clf()

if saveFlag == True:
    
    fdir2 = '/Users/andrewkim/Documents/AA_Discharge/data/'
    dat = pd.DataFrame()
    dat['line'] = kees
    dat['low'] = x[ilows]
    dat['cen'] = x[icens]
    dat['upp'] = x[iupps]
    dat.to_csv(fdir2+code+'_Separator_peaks.csv',index=False)
    print fdir2
    
    
