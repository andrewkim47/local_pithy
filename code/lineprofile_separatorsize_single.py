from pithy import *
import peakutils
from scipy.interpolate import interp1d

codes = [
'CP_B1_C_WT_TIFF',

# 'QU_B1_C_WT_TIFF',
# 'QU_B1_D_WT_TIFF',
# 'QU_C1_C_RT_TIFF',
# 'QU_C1_D_RT_TIFF',
# 'QU_D1_C_CT_TIFF',
# 'QU_D1_D_CT_TIFF',
]

cols = []
for N in range(33):
    for L in range(17):
        cols.append('N'+str(N)+'L'+str(L))

datas = dict()
cents = dict()
edges = dict()
ydats = dict()
# labls = dict()

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
    # dat = data.mean(axis=1)
    return data,scale

def peakFind(x,y,thres=-55,min_dist=50,min_marg=0.2,up_marg=75,numpoint=1000):
    icen = []
    centers = []
    low = []
    upp = []
    
    idxs = peakutils.indexes(y,thres=thres,min_dist=min_dist,thres_abs=True)
    for i in idxs:
        if (x[i]>3) & (x[i]<5): icen.append(i)
    
    if len(icen) < 1:
        print 'No Peaks'
        #fill with zero
        centers.append(0)
        low.append(0)
        upp.append(0)
    elif len(icen) > 1:
        print '2+ Peaks'
        #fill with zero
        centers.append(0)
        low.append(0)
        upp.append(0)
    else: #only 1 peak found
        for ic in icen:
            # centers.append(x[ic])
            centers.append(ic)
            zcr = where(diff(signbit(diff(y))))[0] # 0 crossing
        
            zcr_lo = zcr[x[zcr]<x[ic] - min_marg] # slope 0 works good for left side
            # zcr_up = zcr[x[zcr]>x[ic] + min_margin] 
            # zcr_up = zcr[x[zcr]>x[ic] + min_margin] 
            
            dat_upp = y[ic:ic+up_marg]
            # print dat_upp
            dubdermax = argmax(diff(diff(dat_upp)))+2+ic
            
            low.append(zcr_lo.max())
            # upp.append(zcr_up.min())
            upp.append(dubdermax)
                
    return centers,low,upp
    
data,scale = loadLines(codes[0])
kees = list(data)
X = arange(len(data))*scale
x = linspace(X[0],X[-1],1000)

####
####
####

# Y = -data[kees[4]]
# y = interp1d(X,Y)(x)
# icen,ilow,iupp = peakFind(x,y)
# plot(x,y)
# plot(x[ilow],y[ilow],'bo')
# plot(x[icen],y[icen],'ro')
# plot(x[iupp],y[iupp],'go')
# showme()
# clf()

# print kees[2]


###


icens = []
ilows = []
iupps = []
yvals = []
idxs = arange(4,len(kees),16)
# for kee in kees:
for i in idxs:
    kee = kees[i]
    Y = -data[kee]
    y = interp1d(X,Y)(x)
    
    yvals.append(y)
    icen,ilow,iupp = peakFind(x,y)
    icens.append(icen)
    ilows.append(ilow)
    iupps.append(iupp)

# print ilows
# print x[ilows]

# plot(x[ilows],'bo')
# plot(x[icens],'ro')
# plot(x[iupps],'go')
# # xlim(0,32)
# showme()
# clf()


# idxs = range(16)
# idxs = arange(4,len(kees),16)
# for i in idxs:
#     subplot(211)
#     plot(x,yvals[i])
#     plot(x[ilows[i]],yvals[i][ilows[i]],'bo')
#     plot(x[icens[i]],yvals[i][icens[i]],'ro')
#     plot(x[iupps[i]],yvals[i][iupps[i]],'go')
#     title(i)
#     xlim(3,5)
#     grid()
    
#     subplot(212)
#     plot(x[1:],diff(yvals[i]),'r')
#     plot(x[2:],diff(diff(yvals[i])),'g')
#     ylim(-10,10)
#     xlim(3,5)
#     grid()
    
#     tight_layout()
#     showme()
#     clf()