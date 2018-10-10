from pithy import *
# fdir = '/Users/andrewkim/Documents/AA_Discharge/TIFFS/EA_B1_C_WT_TIFF/Histogram/'
fdir = '/Users/andrewkim/Documents/AA_Discharge/TIFFS/EA_B1_D_WT_TIFF/Histogram/'

datas = dict()
alldatas = dict()
bands = ['B0','B1','B2','B3','B4']

for band in bands:
    alldatas[band] = pd.DataFrame()
    fils = sorted(glob(fdir+'Hist_Mn_Band_' +band+ '*.csv'))
    
    for fil in fils:
        code = fil.split('_')[-1].split('.')[0]
        # print code
        data = pd.read_csv(fil,sep='\t',skiprows=1)
        alldatas[band][code] = data['counts']
    
    tot = alldatas[band].sum(axis=1)
    alldatas[band]['tot'] = tot
    alldatas['bin'] = data['bin']
    
    datas['bin'] = data['bin']
    datas[band] = tot/sum(tot)

# subplot(212)
# title('EA_B1_C_WT_Mn')
title('EA_B1_D_WT_Mn')
plot(datas['bin'],datas['B0'],label='Band0')
plot(datas['bin'],datas['B1'],label='Band1')
plot(datas['bin'],datas['B2'],label='Band2')
plot(datas['bin'],datas['B3'],label='Band3')
plot(datas['bin'],datas['B4'],label='Band4')
legend(loc='center left',bbox_to_anchor=(1, 0.5))
xlabel('Pixel Value')
ylabel('Relative Counts')
# ylim(0,.05)
# tight_layout()
showme()
clf()

