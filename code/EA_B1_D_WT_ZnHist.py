from pithy import *
fdir = '/Users/andrewkim/Documents/AA_Discharge/TIFFS/CP_B1_C_WT_TIFF/Histogram/'

datas = pd.DataFrame()

fils = sorted(glob(fdir+'Hist_Bands*.csv'))
n = 0
for fil in fils:
    # print code
    print fil
    data = pd.read_csv(fil,sep='\t',skiprows=1)
    datas[n] = data['counts']
    n+=1

datas['tot'] = datas.sum(axis=1)
datas['bin'] = data['bin']
# datas['tot'] = datas['tot']/sum(datas['tot'])

tlow = int(open(fil,'r').readline().split('\t')[-1])+1

blacks = float(sum(datas['tot'][0:tlow+1]))
whites = float(sum(datas['tot'][tlow+1:]))
porosity = blacks/(blacks+whites)


print tlow

title('EA_B1_D_WT_Zn')
plot(datas['bin'],datas['tot'],color='k',label='')
plot(0,0,label=round(porosity,3),c='k')
fill_between(datas['bin'][0:tlow],datas['tot'][0:tlow],color='k')
legend(loc='center right')
# axvline(x=tlow-1,color='k',ls='--',label='Cutoff')
# legend(loc='center left',bbox_to_anchor=(1, 0.5))
xlabel('Pixel Value')
ylabel('Counts')
# xlim(0,255)
# ylim(0,0.025)
showme()
clf()



