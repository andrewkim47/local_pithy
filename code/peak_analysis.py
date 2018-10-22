from pithy import *

fdir = '/Users/andrewkim/Documents/AA_Discharge/data/'
# fil = fdir+'discharge_peaks.csv'
fil = fdir+'peaks_abs.csv'

data = pd.read_csv(fil)
data = data.rename(index=int,columns = {"Unnamed: 0":"label"})

pws = dict()
pxs = dict()
pys = dict()
mes = dict()
kees = [
    'FU_D_CT',
    'FU_D_RT',
    'FU_D_WT',
    
    'ER_D_CT',
    'ER_D_RT',
    'ER_D_WT',
    
    'QU_D_CT',
    'QU_D_RT',
    'QU_D_WT',
    
    'CP_D_CT',
    'CP_D_RT',
    'CP_D_WT',
    
    'EN_D_CT',
    'EN_D_RT',
    'EN_D_WT',
    
    'EA_D_CT',
    'EA_D_RT',
    'EA_D_WT',
]

# print data
for key in kees:    
    mes[key] = data[key].loc[range(0,5)]
    pws[key] = data[key].loc[range(5,10)]
    pxs[key] = data[key].loc[range(10,15)]
    pys[key] = data[key].loc[range(15,20)]
x = range(5)


##AVG
figure(figsize=(6.4*2,4.8*1.5))
ax1 = subplot(231)
title('Fujitsu')
plot(x,mes['FU_D_CT'],c='b',marker='o',lw=1,ls='--',mec='k',ms=8,label='CT')
plot(x,mes['FU_D_RT'],c='g',marker='o',lw=1,ls='--',mec='k',ms=8,label='RT')
plot(x,mes['FU_D_WT'],c='r',marker='o',lw=1,ls='--',mec='k',ms=8,label='WT')
ax1.set_xticks(range(5))
ax1.set_xticklabels(range(5))
xlabel('Region')
ylabel('Average Gray Value')
legend(loc='best')

ax2 = subplot(232,sharex=ax1,sharey=ax1)
title('EverReady')
plot(x,mes['ER_D_CT'],c='b',marker='o',lw=1,ls='--',mec='k',ms=8,label='CT')
plot(x,mes['ER_D_RT'],c='g',marker='o',lw=1,ls='--',mec='k',ms=8,label='RT')
plot(x,mes['ER_D_WT'],c='r',marker='o',lw=1,ls='--',mec='k',ms=8,label='WT')
legend(loc='best')
xlabel('Region')
ylabel('Average Gray Value')

ax3 = subplot(233,sharex=ax1,sharey=ax1)
title('Quantum')
plot(x,mes['QU_D_CT'],c='b',marker='o',lw=1,ls='--',mec='k',ms=8,label='CT')
plot(x,mes['QU_D_RT'],c='g',marker='o',lw=1,ls='--',mec='k',ms=8,label='RT')
plot(x,mes['QU_D_WT'],c='r',marker='o',lw=1,ls='--',mec='k',ms=8,label='WT')
legend(loc='best')
xlabel('Region')
ylabel('Average Gray Value')

ax4 = subplot(234,sharex=ax1,sharey=ax1)
title('CopperTop')
plot(x,mes['CP_D_CT'],c='b',marker='o',lw=1,ls='--',mec='k',ms=8,label='CT')
plot(x,mes['CP_D_RT'],c='g',marker='o',lw=1,ls='--',mec='k',ms=8,label='RT')
plot(x,mes['CP_D_WT'],c='r',marker='o',lw=1,ls='--',mec='k',ms=8,label='WT')
legend(loc='best')
xlabel('Region')
ylabel('Average Gray Value')

ax5 = subplot(235,sharex=ax1,sharey=ax1)
title('Energizer')
plot(x,mes['EN_D_CT'],c='b',marker='o',lw=1,ls='--',mec='k',ms=8,label='CT')
plot(x,mes['EN_D_RT'],c='g',marker='o',lw=1,ls='--',mec='k',ms=8,label='RT')
plot(x,mes['EN_D_WT'],c='r',marker='o',lw=1,ls='--',mec='k',ms=8,label='WT')
legend(loc='best')
xlabel('Region')
ylabel('Average Gray Value')

ax6 = subplot(236,sharex=ax1,sharey=ax1)
title('EcoAdvanced')
plot(x,mes['EA_D_CT'],c='b',marker='o',lw=1,ls='--',mec='k',ms=8,label='CT')
plot(x,mes['EA_D_RT'],c='g',marker='o',lw=1,ls='--',mec='k',ms=8,label='RT')
plot(x,mes['EA_D_WT'],c='r',marker='o',lw=1,ls='--',mec='k',ms=8,label='WT')
legend(loc='best')
xlabel('Region')
ylabel('Average Gray Value')

tight_layout()
showme()
clf()


##################
###Peak Center
##################
# figure(figsize=(6.4,4.8*2))
# ax1 = subplot(311)
# ax1.set_xticks(range(5))
# ax1.set_xticklabels(range(5))

# plot(x,pxs['FU_D_CT'],c='b',marker='o',lw=1,ls='--',mec='k',ms=8,label='FU')
# plot(x,pxs['ER_D_CT'],c='b',marker='s',lw=1,ls='--',mec='k',ms=8,label='ER')
# plot(x,pxs['QU_D_CT'],c='b',marker='^',lw=1,ls='--',mec='k',ms=8,label='QU')
# plot(x,pxs['CP_D_CT'],c='b',marker='D',lw=1,ls='--',mec='k',ms=8,label='CP')
# plot(x,pxs['EN_D_CT'],c='b',marker='P',lw=1,ls='--',mec='k',ms=8,label='EN')
# plot(x,pxs['EA_D_CT'],c='b',marker='*',lw=1,ls='--',mec='k',ms=8,label='EA')
# title('Cold')
# xlabel('Region')
# ylabel('Peak Center')
# legend(loc='best')

# ax2 = subplot(312,sharex=ax1,sharey=ax1)
# plot(x,pxs['FU_D_RT'],c='g',marker='o',lw=1,ls='--',mec='k',ms=8,label='FU')
# plot(x,pxs['ER_D_RT'],c='g',marker='s',lw=1,ls='--',mec='k',ms=8,label='ER')
# plot(x,pxs['QU_D_RT'],c='g',marker='^',lw=1,ls='--',mec='k',ms=8,label='QU')
# plot(x,pxs['CP_D_RT'],c='g',marker='D',lw=1,ls='--',mec='k',ms=8,label='CP')
# plot(x,pxs['EN_D_RT'],c='g',marker='P',lw=1,ls='--',mec='k',ms=8,label='EN')
# plot(x,pxs['EA_D_RT'],c='g',marker='*',lw=1,ls='--',mec='k',ms=8,label='EA')
# title('Room')
# xlabel('Region')
# ylabel('Peak Center')
# legend(loc='best')

# ax3 = subplot(313,sharex=ax1,sharey=ax1)
# plot(x,pxs['FU_D_WT'],c='r',marker='o',lw=1,ls='--',mec='k',ms=8,label='FU')
# plot(x,pxs['ER_D_WT'],c='r',marker='s',lw=1,ls='--',mec='k',ms=8,label='ER')
# plot(x,pxs['QU_D_WT'],c='r',marker='^',lw=1,ls='--',mec='k',ms=8,label='QU')
# plot(x,pxs['CP_D_WT'],c='r',marker='D',lw=1,ls='--',mec='k',ms=8,label='CP')
# plot(x,pxs['EN_D_WT'],c='r',marker='P',lw=1,ls='--',mec='k',ms=8,label='EN')
# plot(x,pxs['EA_D_WT'],c='r',marker='*',lw=1,ls='--',mec='k',ms=8,label='EA')
# title('Hot')
# xlabel('Region')
# ylabel('Peak Center')
# legend(loc='best')

# tight_layout()
# showme()
# clf()


figure(figsize=(6.4*2,4.8*1.5))
ax1 = subplot(231)
title('Fujitsu')
plot(x,pxs['FU_D_CT'],c='b',marker='o',lw=1,ls='--',mec='k',ms=8,label='CT')
plot(x,pxs['FU_D_RT'],c='g',marker='o',lw=1,ls='--',mec='k',ms=8,label='RT')
plot(x,pxs['FU_D_WT'],c='r',marker='o',lw=1,ls='--',mec='k',ms=8,label='WT')
ax1.set_xticks(range(5))
ax1.set_xticklabels(range(5))
xlabel('Region')
ylabel('Peak Center')
legend(loc='best')

ax2 = subplot(232,sharex=ax1,sharey=ax1)
title('EverReady')
plot(x,pxs['ER_D_CT'],c='b',marker='o',lw=1,ls='--',mec='k',ms=8,label='CT')
plot(x,pxs['ER_D_RT'],c='g',marker='o',lw=1,ls='--',mec='k',ms=8,label='RT')
plot(x,pxs['ER_D_WT'],c='r',marker='o',lw=1,ls='--',mec='k',ms=8,label='WT')
legend(loc='best')
xlabel('Region')
ylabel('Peak Center')

ax3 = subplot(233,sharex=ax1,sharey=ax1)
title('Quantum')
plot(x,pxs['QU_D_CT'],c='b',marker='o',lw=1,ls='--',mec='k',ms=8,label='CT')
plot(x,pxs['QU_D_RT'],c='g',marker='o',lw=1,ls='--',mec='k',ms=8,label='RT')
plot(x,pxs['QU_D_WT'],c='r',marker='o',lw=1,ls='--',mec='k',ms=8,label='WT')
legend(loc='best')
xlabel('Region')
ylabel('Peak Center')

ax4 = subplot(234,sharex=ax1,sharey=ax1)
title('CopperTop')
plot(x,pxs['CP_D_CT'],c='b',marker='o',lw=1,ls='--',mec='k',ms=8,label='CT')
plot(x,pxs['CP_D_RT'],c='g',marker='o',lw=1,ls='--',mec='k',ms=8,label='RT')
plot(x,pxs['CP_D_WT'],c='r',marker='o',lw=1,ls='--',mec='k',ms=8,label='WT')
legend(loc='best')
xlabel('Region')
ylabel('Peak Center')

ax5 = subplot(235,sharex=ax1,sharey=ax1)
title('Energizer')
plot(x,pxs['EN_D_CT'],c='b',marker='o',lw=1,ls='--',mec='k',ms=8,label='CT')
plot(x,pxs['EN_D_RT'],c='g',marker='o',lw=1,ls='--',mec='k',ms=8,label='RT')
plot(x,pxs['EN_D_WT'],c='r',marker='o',lw=1,ls='--',mec='k',ms=8,label='WT')
legend(loc='best')
xlabel('Region')
ylabel('Peak Center')

ax6 = subplot(236,sharex=ax1,sharey=ax1)
title('EcoAdvanced')
plot(x,pxs['EA_D_CT'],c='b',marker='o',lw=1,ls='--',mec='k',ms=8,label='CT')
plot(x,pxs['EA_D_RT'],c='g',marker='o',lw=1,ls='--',mec='k',ms=8,label='RT')
plot(x,pxs['EA_D_WT'],c='r',marker='o',lw=1,ls='--',mec='k',ms=8,label='WT')
legend(loc='best')
xlabel('Region')
ylabel('Peak Center')

tight_layout()
showme()
clf()

##################
###Peak Width
##################
# figure(figsize=(6.4,4.8*2))
# ax1 = subplot(311)
# ax1.set_xticks(range(5))
# ax1.set_xticklabels(range(5))

# plot(x,pws['FU_D_CT'],c='b',marker='o',lw=1,ls='--',mec='k',ms=8,label='FU')
# plot(x,pws['ER_D_CT'],c='b',marker='s',lw=1,ls='--',mec='k',ms=8,label='ER')
# plot(x,pws['QU_D_CT'],c='b',marker='^',lw=1,ls='--',mec='k',ms=8,label='QU')
# plot(x,pws['CP_D_CT'],c='b',marker='D',lw=1,ls='--',mec='k',ms=8,label='CP')
# plot(x,pws['EN_D_CT'],c='b',marker='P',lw=1,ls='--',mec='k',ms=8,label='EN')
# plot(x,pws['EA_D_CT'],c='b',marker='*',lw=1,ls='--',mec='k',ms=8,label='EA')
# title('Cold')
# xlabel('Region')
# ylabel('Peak Width')
# legend(loc='best')

# ax2 = subplot(312,sharex=ax1,sharey=ax1)
# plot(x,pws['FU_D_RT'],c='g',marker='o',lw=1,ls='--',mec='k',ms=8,label='FU')
# plot(x,pws['ER_D_RT'],c='g',marker='s',lw=1,ls='--',mec='k',ms=8,label='ER')
# plot(x,pws['QU_D_RT'],c='g',marker='^',lw=1,ls='--',mec='k',ms=8,label='QU')
# plot(x,pws['CP_D_RT'],c='g',marker='D',lw=1,ls='--',mec='k',ms=8,label='CP')
# plot(x,pws['EN_D_RT'],c='g',marker='P',lw=1,ls='--',mec='k',ms=8,label='EN')
# plot(x,pws['EA_D_RT'],c='g',marker='*',lw=1,ls='--',mec='k',ms=8,label='EA')
# title('Room')
# xlabel('Region')
# ylabel('Peak Width')
# legend(loc='best')

# ax3 = subplot(313,sharex=ax1,sharey=ax1)
# plot(x,pws['FU_D_WT'],c='r',marker='o',lw=1,ls='--',mec='k',ms=8,label='FU')
# plot(x,pws['ER_D_WT'],c='r',marker='s',lw=1,ls='--',mec='k',ms=8,label='ER')
# plot(x,pws['QU_D_WT'],c='r',marker='^',lw=1,ls='--',mec='k',ms=8,label='QU')
# plot(x,pws['CP_D_WT'],c='r',marker='D',lw=1,ls='--',mec='k',ms=8,label='CP')
# plot(x,pws['EN_D_WT'],c='r',marker='P',lw=1,ls='--',mec='k',ms=8,label='EN')
# plot(x,pws['EA_D_WT'],c='r',marker='*',lw=1,ls='--',mec='k',ms=8,label='EA')
# title('Hot')
# xlabel('Region')
# ylabel('Peak Width')
# legend(loc='best')

# tight_layout()
# showme()
# clf()


figure(figsize=(6.4*2,4.8*1.5))
ax1 = subplot(231)
title('Fujitsu')
plot(x,pws['FU_D_CT'],c='b',marker='o',lw=1,ls='--',mec='k',ms=8,label='CT')
plot(x,pws['FU_D_RT'],c='g',marker='o',lw=1,ls='--',mec='k',ms=8,label='RT')
plot(x,pws['FU_D_WT'],c='r',marker='o',lw=1,ls='--',mec='k',ms=8,label='WT')
ax1.set_xticks(range(5))
ax1.set_xticklabels(range(5))
xlabel('Region')
ylabel('Peak Width')
legend(loc='best')

ax2 = subplot(232,sharex=ax1,sharey=ax1)
title('EverReady')
plot(x,pws['ER_D_CT'],c='b',marker='o',lw=1,ls='--',mec='k',ms=8,label='CT')
plot(x,pws['ER_D_RT'],c='g',marker='o',lw=1,ls='--',mec='k',ms=8,label='RT')
plot(x,pws['ER_D_WT'],c='r',marker='o',lw=1,ls='--',mec='k',ms=8,label='WT')
legend(loc='best')
xlabel('Region')
ylabel('Peak Width')

ax3 = subplot(233,sharex=ax1,sharey=ax1)
title('Quantum')
plot(x,pws['QU_D_CT'],c='b',marker='o',lw=1,ls='--',mec='k',ms=8,label='CT')
plot(x,pws['QU_D_RT'],c='g',marker='o',lw=1,ls='--',mec='k',ms=8,label='RT')
plot(x,pws['QU_D_WT'],c='r',marker='o',lw=1,ls='--',mec='k',ms=8,label='WT')
legend(loc='best')
xlabel('Region')
ylabel('Peak Width')

ax4 = subplot(234,sharex=ax1,sharey=ax1)
title('CopperTop')
plot(x,pws['CP_D_CT'],c='b',marker='o',lw=1,ls='--',mec='k',ms=8,label='CT')
plot(x,pws['CP_D_RT'],c='g',marker='o',lw=1,ls='--',mec='k',ms=8,label='RT')
plot(x,pws['CP_D_WT'],c='r',marker='o',lw=1,ls='--',mec='k',ms=8,label='WT')
legend(loc='best')
xlabel('Region')
ylabel('Peak Width')

ax5 = subplot(235,sharex=ax1,sharey=ax1)
title('Energizer')
plot(x,pws['EN_D_CT'],c='b',marker='o',lw=1,ls='--',mec='k',ms=8,label='CT')
plot(x,pws['EN_D_RT'],c='g',marker='o',lw=1,ls='--',mec='k',ms=8,label='RT')
plot(x,pws['EN_D_WT'],c='r',marker='o',lw=1,ls='--',mec='k',ms=8,label='WT')
legend(loc='best')
xlabel('Region')
ylabel('Peak Width')

ax6 = subplot(236,sharex=ax1,sharey=ax1)
title('EcoAdvanced')
plot(x,pws['EA_D_CT'],c='b',marker='o',lw=1,ls='--',mec='k',ms=8,label='CT')
plot(x,pws['EA_D_RT'],c='g',marker='o',lw=1,ls='--',mec='k',ms=8,label='RT')
plot(x,pws['EA_D_WT'],c='r',marker='o',lw=1,ls='--',mec='k',ms=8,label='WT')
legend(loc='best')
xlabel('Region')
ylabel('Peak Width')

tight_layout()
showme()
clf()

##################
##################

# ##################
# ###Peak Height
# ##################
# figure(figsize=(6.4,4.8*2))
# ax1 = subplot(311)
# ax1.set_xticks(range(5))
# ax1.set_xticklabels(range(5))

# plot(x,pys['FU_D_CT'],c='b',marker='o',lw=1,ls='--',mec='k',ms=8,label='FU')
# plot(x,pys['ER_D_CT'],c='b',marker='s',lw=1,ls='--',mec='k',ms=8,label='ER')
# plot(x,pys['QU_D_CT'],c='b',marker='^',lw=1,ls='--',mec='k',ms=8,label='QU')
# plot(x,pys['CP_D_CT'],c='b',marker='D',lw=1,ls='--',mec='k',ms=8,label='CP')
# plot(x,pys['EN_D_CT'],c='b',marker='P',lw=1,ls='--',mec='k',ms=8,label='EN')
# plot(x,pys['EA_D_CT'],c='b',marker='*',lw=1,ls='--',mec='k',ms=8,label='EA')
# title('Cold')
# xlabel('Region')
# ylabel('Peak Height')
# legend(loc='best')

# ax2 = subplot(312,sharex=ax1,sharey=ax1)
# plot(x,pys['FU_D_RT'],c='g',marker='o',lw=1,ls='--',mec='k',ms=8,label='FU')
# plot(x,pys['ER_D_RT'],c='g',marker='s',lw=1,ls='--',mec='k',ms=8,label='ER')
# plot(x,pys['QU_D_RT'],c='g',marker='^',lw=1,ls='--',mec='k',ms=8,label='QU')
# plot(x,pys['CP_D_RT'],c='g',marker='D',lw=1,ls='--',mec='k',ms=8,label='CP')
# plot(x,pys['EN_D_RT'],c='g',marker='P',lw=1,ls='--',mec='k',ms=8,label='EN')
# plot(x,pys['EA_D_RT'],c='g',marker='*',lw=1,ls='--',mec='k',ms=8,label='EA')
# title('Room')
# xlabel('Region')
# ylabel('Peak Height')
# legend(loc='best')

# ax3 = subplot(313,sharex=ax1,sharey=ax1)
# plot(x,pys['FU_D_WT'],c='r',marker='o',lw=1,ls='--',mec='k',ms=8,label='FU')
# plot(x,pys['ER_D_WT'],c='r',marker='s',lw=1,ls='--',mec='k',ms=8,label='ER')
# plot(x,pys['QU_D_WT'],c='r',marker='^',lw=1,ls='--',mec='k',ms=8,label='QU')
# plot(x,pys['CP_D_WT'],c='r',marker='D',lw=1,ls='--',mec='k',ms=8,label='CP')
# plot(x,pys['EN_D_WT'],c='r',marker='P',lw=1,ls='--',mec='k',ms=8,label='EN')
# plot(x,pys['EA_D_WT'],c='r',marker='*',lw=1,ls='--',mec='k',ms=8,label='EA')
# title('Hot')
# xlabel('Region')
# ylabel('Peak Height')
# legend(loc='best')

# tight_layout()
# showme()
# clf()


# figure(figsize=(6.4*2,4.8*1.5))
# ax1 = subplot(231)
# title('Fujitsu')
# plot(x,pys['FU_D_CT'],c='b',marker='o',lw=1,ls='--',mec='k',ms=8,label='CT')
# plot(x,pys['FU_D_RT'],c='g',marker='o',lw=1,ls='--',mec='k',ms=8,label='RT')
# plot(x,pys['FU_D_WT'],c='r',marker='o',lw=1,ls='--',mec='k',ms=8,label='WT')
# ax1.set_xticks(range(5))
# ax1.set_xticklabels(range(5))
# xlabel('Region')
# ylabel('Peak Height')
# legend(loc='best')

# ax2 = subplot(232,sharex=ax1,sharey=ax1)
# title('EverReady')
# plot(x,pys['ER_D_CT'],c='b',marker='o',lw=1,ls='--',mec='k',ms=8,label='CT')
# plot(x,pys['ER_D_RT'],c='g',marker='o',lw=1,ls='--',mec='k',ms=8,label='RT')
# plot(x,pys['ER_D_WT'],c='r',marker='o',lw=1,ls='--',mec='k',ms=8,label='WT')
# legend(loc='best')
# xlabel('Region')
# ylabel('Peak Height')

# ax3 = subplot(233,sharex=ax1,sharey=ax1)
# title('Quantum')
# plot(x,pys['QU_D_CT'],c='b',marker='o',lw=1,ls='--',mec='k',ms=8,label='CT')
# plot(x,pys['QU_D_RT'],c='g',marker='o',lw=1,ls='--',mec='k',ms=8,label='RT')
# plot(x,pys['QU_D_WT'],c='r',marker='o',lw=1,ls='--',mec='k',ms=8,label='WT')
# legend(loc='best')
# ylabel('Region')
# xlabel('Peak Height')

# ax4 = subplot(234,sharex=ax1,sharey=ax1)
# title('CopperTop')
# plot(x,pys['CP_D_CT'],c='b',marker='o',lw=1,ls='--',mec='k',ms=8,label='CT')
# plot(x,pys['CP_D_RT'],c='g',marker='o',lw=1,ls='--',mec='k',ms=8,label='RT')
# plot(x,pys['CP_D_WT'],c='r',marker='o',lw=1,ls='--',mec='k',ms=8,label='WT')
# legend(loc='best')
# xlabel('Region')
# xlabel('Peak Height')

# ax5 = subplot(235,sharex=ax1,sharey=ax1)
# title('Energizer')
# plot(x,pys['EN_D_CT'],c='b',marker='o',lw=1,ls='--',mec='k',ms=8,label='CT')
# plot(x,pys['EN_D_RT'],c='g',marker='o',lw=1,ls='--',mec='k',ms=8,label='RT')
# plot(x,pys['EN_D_WT'],c='r',marker='o',lw=1,ls='--',mec='k',ms=8,label='WT')
# legend(loc='best')
# xlabel('Region')
# xlabel('Peak Height')

# ax6 = subplot(236,sharex=ax1,sharey=ax1)
# title('EcoAdvanced')
# plot(x,pys['EA_D_CT'],c='b',marker='o',lw=1,ls='--',mec='k',ms=8,label='CT')
# plot(x,pys['EA_D_RT'],c='g',marker='o',lw=1,ls='--',mec='k',ms=8,label='RT')
# plot(x,pys['EA_D_WT'],c='r',marker='o',lw=1,ls='--',mec='k',ms=8,label='WT')
# legend(loc='best')
# xlabel('Region')
# xlabel('Peak Height')

# tight_layout()
# showme()
# clf()

# ##################
# ##################