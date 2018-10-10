import matplotlib
# matplotlib.use('agg')
from pithy import showme
import matplotlib.pyplot as plt
import numpy as np

filedir = 'files/testplot/'
x = np.linspace(0, 2*np.pi, 100)
y = np.sin(x)
z = np.zeros(100)

fig = plt.figure()
ax = plt.axes(xlim=(0,2*np.pi),ylim=(-2,2))

# #12.3seconds for 100 files
# vl = ax.axvline(x=0)
# line1,=ax.plot(x, y, 'r-')
# for i in np.linspace(0,6,100):
#     vl.set_xdata(i)
#     plt.savefig(filedir+str(i)+'.png')

#16
for i in np.linspace(0,6,100):
    ax.plot(x,y,'r-')
    ax.axvline(x=i)
    plt.savefig(filedir+str(i)+'.png')
    ax.cla()
    