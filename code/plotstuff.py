from pithy import *

fdir = '/Users/andrewkim/Documents/AA_Discharge/TIFFS/EcoAdvanced_B1_Discharged_Warm50_TIFF/Linescan/'

fil1 = fdir+'Linescan_Pin.csv'
fil2 = fdir+'Linescan_Sep.csv'


cols = ['L'+str(i) for i in range(8)]
data1 = pd.read_csv(fil1,sep=',')
data2 = pd.read_csv(fil2,sep=',')

for col in cols:
    subplot(211)
    plot(data1['bin'],data1[col],label=col)
    subplot(212)
    plot(data2['bin'],data2[col],label=col)
subplot(211)
title('LineScan Pin')
legend(loc='center left',bbox_to_anchor=(1, 0.5))
xlabel('Pixel Position')
ylabel('Pixel Intensity')
subplot(212)
title('LineScan Sep')
legend(loc='center left',bbox_to_anchor=(1, 0.5))
xlabel('Pixel Position')
ylabel('Pixel Intensity')
tight_layout()
showme()
clf()

