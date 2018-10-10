from pithy import *
fdir = '/Users/andrewkim/Documents/AA_Discharge/TIFFS/EA_B1_C_WT_TIFF/Histogram/'

datas = pd.DataFrame()

fils = sorted(glob(fdir+'Hist_Por*.csv'))
n = 0
for fil in fils:
    # print code
    # print fil
    data = pd.read_csv(fil,sep='\t',skiprows=0)
    datas[n] = data['counts']
    # print fil
    n+=1

datas['tot'] = datas.sum(axis=1)
datas['bin'] = data['bin']
# datas['tot'] = datas['tot']/sum(datas['tot'])


blacks = float(sum(datas['tot'][0]))
whites = float(sum(datas['tot'][255]))

porosity = blacks/(blacks+whites)
print porosity

plot(datas['bin'],datas['tot'])
showme()
clf()

x1 = range(1,7,1)
x2 = range(6,0,-1)


bar(datas['bin'],datas['tot'])
xlabel('Region')
ylabel('Average Pixel Intensity')
xlim(-50,300)
tight_layout()
showme()
clf()


