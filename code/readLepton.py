# import matplotlib

from pithy import *
import os
from glob import glob
files = sorted(glob('files/Lepton_1500_Paint/*.txt'))
# for f in sorted(os.listdir('/Users/andrewkim/pithy/files/LeptonWater')):
    # if '.txt' in f: files.append(f)
# for i in range(len(files)): print i,files[i]
# print len(files)

xlo = 30
xhi = 50
ylo = 20
yhi = 40

def qplot(data,cmap=None,vmin=None,vmax=None):
    imshow(data,cmap=cmap,vmin=vmin,vmax=vmax)
    plot([xlo,xlo,xhi,xhi,xlo],[yhi,ylo,ylo,yhi,yhi])
    xlim(0,80)
    ylim(60,0)
    colorbar()
    # xlabel('Pixel')
    ylabel('Pixel')
    # showme()
    # clf()

def qplotmini(data,cmap=None,vmin=None,vmax=None):
    imshow(data,cmap=cmap,vmin=vmin,vmax=vmax,extent=[xlo,xhi,yhi,ylo])
    plot([xlo,xlo,xhi,xhi,xlo],[yhi,ylo,ylo,yhi,yhi])
    xlim(0,80)
    ylim(60,0)
    colorbar()
    xlabel('Pixel')
    ylabel('Pixel')
    # showme()
    # clf()
    
temps = []
dats = dict()
datas=dict()
ldatas=dict()
# isp = [0
for i in range(len(files)):
    f = files[i]
    temps.append(f.split('_')[1])
    datas[i] = np.loadtxt(f)
    # ldatas[i] = log(datas[i])
    dats[i] = datas[i][xlo:xhi,ylo:yhi]

init = np.loadtxt(files[0])

qplot(datas[10000/30]-init)
showme()




