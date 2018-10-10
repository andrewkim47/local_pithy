from pithy import *
from glob import glob
import pandas as pd
f1 = 'files/SAD/Data_20180315_LiT_A_LongCycle_1521148604.csv'
f2 = 'files/SAD/Data_20180315_LiT_B_LongCycle_1521148188.csv'

d1 = pd.read_csv(f1)
d2 = pd.read_csv(f2)

t1 = (d1['time']-d1['time'].iloc[0])/3600.
t2 = (d2['time']-d2['time'].iloc[0])/3600.



# subplot(211)
plot(t1,d1['voltage'],label='A')
# plot(t2,d2['voltage'],label='B')
legend(loc='best')
xlabel('Hour')
ylabel('Potential V')
ylim(13,15)
twinx()
plot(t1[0:-1],diff(d1['voltage']),'r')
xlim(38,45)
ylim(-.001,.001)
ylabel('dV')
showme()
clf()



figure(figsize=(6.4,4.8*2))
subplot(211)
title('A')
plot(t1,d1['voltage'])
legend(loc='best')
xlabel('Hour')
ylabel('Potential V')
xlim(14,19)
ylim(10.4,11.6)
subplot(212)
title('B')
plot(t2,d2['voltage'],'g')
legend(loc='best')
xlabel('Hour')
ylabel('Potential V')
xlim(21,26)
ylim(10.4,11.6)
showme()
clf()

# figure(figsize=(6.4,4.8*2))
# subplot(211)
# title('A')
# plot(t1,d1['voltage'])
# legend(loc='best')
# xlabel('Hour')
# ylabel('Potential V')
# xlim(14,19)
# ylim(10.4,11.6)
# subplot(212)
# title('B')
# plot(t2,d2['voltage'],'g')
# legend(loc='best')
# xlabel('Hour')
# ylabel('Potential V')
# xlim(21,26)
# ylim(11.4,11.6)
# showme()
# clf()