from pithy import *
from glob import glob
# import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import numpy as np
import json
from matplotlib import animation

#find all relevant json files
sdir = 'files/ARPAEdemo/'
imgs = sorted(glob('files/100StepsPNG/*.png'))
carts = sorted(glob('files/18650Cross/cartoon*.png'))

trfiles = sorted(glob(sdir+'Demo6_*TR.json'))
pefiles = sorted(glob(sdir+'Demo6_*PE.json'))

#load each json file and extract the wave and motorpos
tr = []
pe = []
motorpos=[]
angles=[]
for i in range(101):
    #load TR
    fo = open(trfiles[i],'r')
    trdata = json.load(fo)
    onewave = array(trdata['wave'])-2**15 #center at 2^15
    tr.append(list(onewave))
    motorpos.append(trdata['motorpos'])
    angles.append(trdata['motorpos']*3.6)
    fo.close()
    #load PE
    fo = open(pefiles[i],'r')
    pedata = json.load(fo)
    onewave = array(pedata['wave'])-2**15 #center at 2^15
    pe.append(list(onewave))
    fo.close()

angles[-1]=360.0
# print angles


# tend = data['tstamp']-tsta
#Get the tof data by math'ing the x and vel data
trxs = trdata['x'] #mm
trvel = trdata['vel']*1000. # mm/s
trtofs = array(trxs)/float(trvel)*1.e6 #uS

trext = [angles[0],angles[-1],trtofs[-1],trtofs[0]]

pexs = pedata['x'] #mm
pevel = pedata['vel']*1000. # mm/s
petofs = array(pexs)/float(pevel)*1.e6 #uS
peext = [angles[0],angles[-1],petofs[-1],petofs[0]]

# #set color saturation map to maximum value for best resoltuion
# if abs(np.max(siuidata)) > abs(np.min(siuidata)): 
#     colormax = abs(np.max(siuidata))
# else:
#     colormax = abs(np.min(siuidata))
colormax = 2**15

fig = figure(0)
fig.set_figheight(15)
fig.set_figwidth(15)
ax1 = subplot2grid((3,4), (0,0), colspan=2)
ax2 = subplot2grid((3,4), (0,2), colspan=2)
ax3 = subplot2grid((3,3), (1,0), colspan=2)
ax4 = subplot2grid((3,3), (1, 2))
ax5 = subplot2grid((3,3), (2,0), colspan=2)
ax6 = subplot2grid((3,3), (2, 2))
# tight_layout()
# fig.subplots_adjust(left=0, bottom=0, right=1, top=1, wspace=None, hspace=None)
# showme()
# clf()

#ax1 Photo
img = mpimg.imread(imgs[0])
photo=ax1.imshow(img,aspect='auto')
ax1.set_yticks([])
ax1.set_xticks([])
#ax2 Cartoon
cart = mpimg.imread(carts[0])
cartoon=ax2.imshow(cart,aspect='auto')
ax2.set_yticks([])
ax2.set_xticks([])
#ax3 TR Map
ax3.imshow(transpose(tr),aspect='auto',cmap='bwr',extent=trext)
ax3.set_ylabel('ToF (uS)')
ax3.set_title('Transmission Mode')
vl3=ax3.axvline(x=0,color='k')
#ax4 TR Snapshot
trsnap=ax4.plot(trtofs,tr[0],'k')[0]
ax4.set_yticks([])
#ax5 PE Map
ax5.imshow(transpose(pe),aspect='auto',cmap='bwr',extent=peext)
ax5.set_xlabel('Angle (deg)')
ax5.set_ylabel('ToF (uS)')
ax5.set_title('Pulse-Echo Mode')
vl5=ax5.axvline(x=0,color='k')
#ax6 PE Snapshot
pesnap=ax6.plot(petofs,pe[0],'k')[0]
ax6.set_xlabel('ToF (uS)')
ax6.set_yticks([])
showme()

# # #i is the frame-number, 
def animate(i):
    #photo
    img = mpimg.imread(imgs[i])
    photo.set_data(img)
    #cartoon
    cart = mpimg.imread(carts[i])
    cartoon.set_data(cart)
    #tr
    trsnap.set_ydata(tr[i])
    vl3.set_xdata(x=angles[i])
    #pe
    pesnap.set_ydata(pe[i])
    vl5.set_xdata(x=angles[i])
    lines = [photo,cartoon,vl3,vl5]
    return lines
#     # # # # call the animator.  blit=True means only re-draw the parts that have changed.
filename = 'files/Demo6.mp4'
anim = animation.FuncAnimation(fig, animate, frames=101,blit=True)
anim.save(filename, fps=20, extra_args=['-vcodec', 'libx264'])    # cur 