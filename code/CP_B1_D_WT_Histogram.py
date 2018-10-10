from pithy import *
fdir = '/Users/andrewkim/Documents/AA_Discharge/TIFFS/CP_B1_D_WT_TIFF/Histogram/'

datas = pd.DataFrame()

fils = sorted(glob(fdir+'Hist_Bands*.csv'))
bands = []
for fil in fils:
    suff = fil.split('/')[-1]
    B = suff.split('_')[2][0:5]
    bands.append(B)
bands = unique(bands)
# print bands

for band in bands:
    tempDatas = pd.DataFrame()
    for fil in fils:
        if band in fil: 
            suff = fil.split('/')[-1]
            N = int(suff.split('_')[3][1:5])
            data = pd.read_csv(fil,sep='\t',skiprows=1)['counts']
            tempDatas[N] = data
            # data['Band'] = 
    datas[band] = tempDatas.sum(axis=1)
datas.loc[0,:]= 0
bins = range(256)

#normalize
ndata = datas/datas.sum(axis=0)

figure(figsize=(6.4,4.8*1))
shift = 0
for band in bands[5:26]:
    plot(bins,ndata[band]+shift,'k')
    shift+=0.00
showme()
clf()


# dict_you_want = { your_key: old_dict[your_key] for your_key in your_keys }

# band = {'B': datas['B'] for 'B' in keys}

# print datas['B']==0
# print datas[data['B']==0]

# datas['tot'] = datas.sum(axis=1)
# datas['bin'] = data['bin']
# # datas['tot'] = datas['tot']/sum(datas['tot'])

# tlow = int(open(fil,'r').readline().split('\t')[-1])+1

# blacks = float(sum(datas['tot'][0:tlow+1]))
# whites = float(sum(datas['tot'][tlow+1:]))
# porosity = blacks/(blacks+whites)


# print tlow

# title('EA_B1_D_WT_Zn')
# plot(datas['bin'],datas['tot'],color='k',label='')
# plot(0,0,label=round(porosity,3),c='k')
# fill_between(datas['bin'][0:tlow],datas['tot'][0:tlow],color='k')
# legend(loc='center right')
# # axvline(x=tlow-1,color='k',ls='--',label='Cutoff')
# # legend(loc='center left',bbox_to_anchor=(1, 0.5))
# xlabel('Pixel Value')
# ylabel('Counts')
# # xlim(0,255)
# # ylim(0,0.025)
# showme()
# clf()



