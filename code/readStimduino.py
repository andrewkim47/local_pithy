from pithy import *
import pandas as pd

file = 'files/'+'stim300.txt'

dat = pd.read_csv(file)
t=dat['t']-dat['t'].iloc[0]
tov=dat['tov']
val=dat['val']


plot(t,tov,'b',label='tov')
plot(t,val,'g',label='val')
ylim(-.2,1.2)
xlim(0,5e3)
legend(loc='best')
showme()
clf()