from pithy import *
import json
from glob import glob


flist = []
flist.append(sorted(glob('files/SIUITest/146-1/146-1*.json')))
flist.append(sorted(glob('files/SIUITest/155-1/155-1*.json')))
flist.append(sorted(glob('files/SIUITest/155-2/155-2*.json')))
flist.append(sorted(glob('files/SIUITest/188-1/188-1*.json')))
flist.append(sorted(glob('files/SIUITest/242-1/242-1*.json')))
# flist.append(sorted(glob('files/SIUITest/242-2/242-2*.json')))

labels =[
    '146-1',   
    '153-1',   
    '153-2',   
    '188-1',   
    '242-1',   
    # '242-2',   
]

imgs = []
for j in range(len(flist)):
    files = flist[j]
    numF = len(files)
    angles = []
    img = []
    for fil in files:
        data = json.load(open(fil))
        img.append(data['wave'])
        
        step = fil.split('_')[-2]
        # angle = mod(int(step),200) * 360./200.
        angle = int(step) * 360./200.
        angles.append(angle)

    imgs.append(img)
    tof = array(data['x'])/float(data['vel'])*1000.
    xmin = tof[0]
    xmax = tof[-1]
    
    vmax = 2**15 + 10.e3
    vmin = 2**15 - 10.e3
    
    imshow(transpose(img),aspect='auto',cmap=cm.bwr,extent=[angles[0],angles[-1],xmax,xmin],vmin=vmin,vmax=vmax)
    
    axvline(x=0,color='k',ls='--')
    axvline(x=360,color='k',ls='--')
    axvline(x=720,color='k',ls='--')
    axvline(x=1080,color='k',ls='--')
    
    xlabel('Angle')
    ylabel('ToF uS')
    title(labels[j])
    showme()
    clf()
    
    
    plot(img[10])
    showme()
    clf()
    



# imshow(transpose(img[0:200]),aspect='auto',cmap=cm.bwr,extent=[0,200,xmax,xmin])
# showme()
# clf()


# imshow(transpose(img[200:400]),aspect='auto',cmap=cm.bwr,extent=[200,400,xmax,xmin])
# showme()
# clf()