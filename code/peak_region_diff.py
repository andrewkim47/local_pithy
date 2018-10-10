from pithy import *

fdir = '/Users/andrewkim/Documents/AA_Discharge/data/'
# fil = fdir+'discharge_peaks.csv'
fil = fdir+'peaks_abs.csv'

data = pd.read_csv(fil)
data = data.rename(index=int,columns = {"Unnamed: 0":"label"})
df = data

pws = dict()
pxs = dict()
pys = dict()


wdat = dict()
xdat = dict()

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
    pws[key] = data[key].loc[range(0,5)]
    pxs[key] = data[key].loc[range(5,10)]
    pys[key] = data[key].loc[range(10,15)]
    
    wdat[key] = []
    wdat[key].append(data[key].loc[0]-data[key].loc[1])
    wdat[key].append(data[key].loc[1]-data[key].loc[2])
    wdat[key].append(data[key].loc[2]-data[key].loc[3])
    wdat[key].append(data[key].loc[3]-data[key].loc[4])
    wdat[key].append(data[key].loc[0]-data[key].loc[2])
    wdat[key].append(data[key].loc[1]-data[key].loc[3])
    wdat[key].append(data[key].loc[2]-data[key].loc[4])
    wdat[key].append(data[key].loc[0]-data[key].loc[3])
    wdat[key].append(data[key].loc[1]-data[key].loc[4])
    wdat[key].append(data[key].loc[0]-data[key].loc[4])
    
    xdat[key] = []
    xdat[key].append(data[key].loc[5]-data[key].loc[6])
    xdat[key].append(data[key].loc[6]-data[key].loc[7])
    xdat[key].append(data[key].loc[7]-data[key].loc[8])
    xdat[key].append(data[key].loc[8]-data[key].loc[9])
    xdat[key].append(data[key].loc[5]-data[key].loc[7])
    xdat[key].append(data[key].loc[6]-data[key].loc[8])
    xdat[key].append(data[key].loc[7]-data[key].loc[9])
    xdat[key].append(data[key].loc[5]-data[key].loc[8])
    xdat[key].append(data[key].loc[6]-data[key].loc[9])
    xdat[key].append(data[key].loc[5]-data[key].loc[9])

x=arange(256)
    
ticklabel = [
    'n',
    '01',
    '12',
    '23',
    '34',
    'n',
    '02',
    '13',
    '24',
    'n',
    '03',
    '14',
    'n',
    '04',
]   

# df = df[df['lab']!='n'].reset_index(drop=True)
# df.to_csv(fdir2+'ssq.csv',index=False)

# print df['lab']

x1 = arange(1,5)
x2 = arange(5,8)
x3 = arange(8,10)
x4 = arange(10,11)

xlab = ['','0-1','1-2','2-3','3-4','0-2','1-3','2-4','0-3','1-4','0-4']
xticks = arange(0,11)

figure(figsize=(6.4*2,4.8*1.5))

ax1=subplot(231)
title('FU')
plot(x1,xdat['FU_D_CT'][0:4],'bo-')
plot(x1,xdat['FU_D_RT'][0:4],'go-')
plot(x1,xdat['FU_D_WT'][0:4],'ro-')
plot(x2,xdat['FU_D_CT'][4:7],'bs-')
plot(x2,xdat['FU_D_RT'][4:7],'gs-')
plot(x2,xdat['FU_D_WT'][4:7],'rs-')
plot(x3,xdat['FU_D_CT'][7:9],'b.-')
plot(x3,xdat['FU_D_RT'][7:9],'g.-')
plot(x3,xdat['FU_D_WT'][7:9],'r.-')
plot(x4,xdat['FU_D_CT'][9:10],'bo')
plot(x4,xdat['FU_D_RT'][9:10],'go')
plot(x4,xdat['FU_D_WT'][9:10],'ro')
xlabel('Region')
ylabel('Peak Center Difference')

ax2=subplot(232,sharex=ax1,sharey=ax1)
title('ER')
plot(x1,xdat['ER_D_CT'][0:4],'bo-')
plot(x1,xdat['ER_D_RT'][0:4],'go-')
plot(x1,xdat['ER_D_WT'][0:4],'ro-')
plot(x2,xdat['ER_D_CT'][4:7],'bs-')
plot(x2,xdat['ER_D_RT'][4:7],'gs-')
plot(x2,xdat['ER_D_WT'][4:7],'rs-')
plot(x3,xdat['ER_D_CT'][7:9],'b.-')
plot(x3,xdat['ER_D_RT'][7:9],'g.-')
plot(x3,xdat['ER_D_WT'][7:9],'r.-')
plot(x4,xdat['ER_D_CT'][9:10],'bo')
plot(x4,xdat['ER_D_RT'][9:10],'go')
plot(x4,xdat['ER_D_WT'][9:10],'ro')
xlabel('Region')
ylabel('Peak Center Difference')

ax3=subplot(233,sharex=ax1,sharey=ax1)
title('QU')
plot(x1,xdat['QU_D_CT'][0:4],'bo-')
plot(x1,xdat['QU_D_RT'][0:4],'go-')
plot(x1,xdat['QU_D_WT'][0:4],'ro-')
plot(x2,xdat['QU_D_CT'][4:7],'bs-')
plot(x2,xdat['QU_D_RT'][4:7],'gs-')
plot(x2,xdat['QU_D_WT'][4:7],'rs-')
plot(x3,xdat['QU_D_CT'][7:9],'b.-')
plot(x3,xdat['QU_D_RT'][7:9],'g.-')
plot(x3,xdat['QU_D_WT'][7:9],'r.-')
plot(x4,xdat['QU_D_CT'][9:10],'bo')
plot(x4,xdat['QU_D_RT'][9:10],'go')
plot(x4,xdat['QU_D_WT'][9:10],'ro')
xlabel('Region')
ylabel('Peak Center Difference')

ax4=subplot(234,sharex=ax1,sharey=ax1)
title('CP')
plot(x1,xdat['CP_D_CT'][0:4],'bo-')
plot(x1,xdat['CP_D_RT'][0:4],'go-')
plot(x1,xdat['CP_D_WT'][0:4],'ro-')
plot(x2,xdat['CP_D_CT'][4:7],'bs-')
plot(x2,xdat['CP_D_RT'][4:7],'gs-')
plot(x2,xdat['CP_D_WT'][4:7],'rs-')
plot(x3,xdat['CP_D_CT'][7:9],'b.-')
plot(x3,xdat['CP_D_RT'][7:9],'g.-')
plot(x3,xdat['CP_D_WT'][7:9],'r.-')
plot(x4,xdat['CP_D_CT'][9:10],'bo')
plot(x4,xdat['CP_D_RT'][9:10],'go')
plot(x4,xdat['CP_D_WT'][9:10],'ro')
xlabel('Region')
ylabel('Peak Center Difference')

ax5=subplot(235,sharex=ax1,sharey=ax1)
title('EN')
plot(x1,xdat['EN_D_CT'][0:4],'bo-')
plot(x1,xdat['EN_D_RT'][0:4],'go-')
plot(x1,xdat['EN_D_WT'][0:4],'ro-')
plot(x2,xdat['EN_D_CT'][4:7],'bs-')
plot(x2,xdat['EN_D_RT'][4:7],'gs-')
plot(x2,xdat['EN_D_WT'][4:7],'rs-')
plot(x3,xdat['EN_D_CT'][7:9],'b.-')
plot(x3,xdat['EN_D_RT'][7:9],'g.-')
plot(x3,xdat['EN_D_WT'][7:9],'r.-')
plot(x4,xdat['EN_D_CT'][9:10],'bo')
plot(x4,xdat['EN_D_RT'][9:10],'go')
plot(x4,xdat['EN_D_WT'][9:10],'ro')
xlabel('Region')
ylabel('Peak Center Difference')

ax6=subplot(236,sharex=ax1,sharey=ax1)
title('EA')
plot(x1,xdat['EA_D_CT'][0:4],'bo-')
plot(x1,xdat['EA_D_RT'][0:4],'go-')
plot(x1,xdat['EA_D_WT'][0:4],'ro-')
plot(x2,xdat['EA_D_CT'][4:7],'bs-')
plot(x2,xdat['EA_D_RT'][4:7],'gs-')
plot(x2,xdat['EA_D_WT'][4:7],'rs-')
plot(x3,xdat['EA_D_CT'][7:9],'b.-')
plot(x3,xdat['EA_D_RT'][7:9],'g.-')
plot(x3,xdat['EA_D_WT'][7:9],'r.-')
plot(x4,xdat['EA_D_CT'][9:10],'bo')
plot(x4,xdat['EA_D_RT'][9:10],'go')
plot(x4,xdat['EA_D_WT'][9:10],'ro')
xlabel('Region')
ylabel('Peak Center Difference')

ax1.set_xticks(xticks)
ax1.set_xticklabels(xlab)
ax1.grid()
ax2.grid()
ax3.grid()
ax4.grid()
ax5.grid()
ax6.grid()

tight_layout()
showme()
clf()

figure(5)
plot(x1,wdat['QU_D_CT'][0:4],'bo-')
plot(x2,wdat['QU_D_CT'][4:7],'bs-')
plot(x3,wdat['QU_D_CT'][7:9],'b.-')
plot(x4,wdat['QU_D_CT'][9:10],'bo')
plot(x1,wdat['QU_D_WT'][0:4],'ro-')
plot(x2,wdat['QU_D_WT'][4:7],'rs-')
plot(x3,wdat['QU_D_WT'][7:9],'r.-')
plot(x4,wdat['QU_D_WT'][9:10],'ro')
showme()
clf()


figure(figsize=(6.4*2,4.8*1.5))

ax1=subplot(231)
title('FU')
plot(x1,wdat['FU_D_CT'][0:4],'bo-')
plot(x1,wdat['FU_D_RT'][0:4],'go-')
plot(x1,wdat['FU_D_WT'][0:4],'ro-')
plot(x2,wdat['FU_D_CT'][4:7],'bs-')
plot(x2,wdat['FU_D_RT'][4:7],'gs-')
plot(x2,wdat['FU_D_WT'][4:7],'rs-')
plot(x3,wdat['FU_D_CT'][7:9],'b.-')
plot(x3,wdat['FU_D_RT'][7:9],'g.-')
plot(x3,wdat['FU_D_WT'][7:9],'r.-')
plot(x4,wdat['FU_D_CT'][9:10],'bo')
plot(x4,wdat['FU_D_RT'][9:10],'go')
plot(x4,wdat['FU_D_WT'][9:10],'ro')
xlabel('Region')
ylabel('Peak Width Difference')

ax2=subplot(232,sharex=ax1,sharey=ax1)
title('ER')
plot(x1,wdat['ER_D_CT'][0:4],'bo-')
plot(x1,wdat['ER_D_RT'][0:4],'go-')
plot(x1,wdat['ER_D_WT'][0:4],'ro-')
plot(x2,wdat['ER_D_CT'][4:7],'bs-')
plot(x2,wdat['ER_D_RT'][4:7],'gs-')
plot(x2,wdat['ER_D_WT'][4:7],'rs-')
plot(x3,wdat['ER_D_CT'][7:9],'b.-')
plot(x3,wdat['ER_D_RT'][7:9],'g.-')
plot(x3,wdat['ER_D_WT'][7:9],'r.-')
plot(x4,wdat['ER_D_CT'][9:10],'bo')
plot(x4,wdat['ER_D_RT'][9:10],'go')
plot(x4,wdat['ER_D_WT'][9:10],'ro')
xlabel('Region')
ylabel('Peak Width Difference')

ax3=subplot(233,sharex=ax1,sharey=ax1)
title('QU')
plot(x1,wdat['QU_D_CT'][0:4],'bo-')
plot(x1,wdat['QU_D_RT'][0:4],'go-')
plot(x1,wdat['QU_D_WT'][0:4],'ro-')
plot(x2,wdat['QU_D_CT'][4:7],'bs-')
plot(x2,wdat['QU_D_RT'][4:7],'gs-')
plot(x2,wdat['QU_D_WT'][4:7],'rs-')
plot(x3,wdat['QU_D_CT'][7:9],'b.-')
plot(x3,wdat['QU_D_RT'][7:9],'g.-')
plot(x3,wdat['QU_D_WT'][7:9],'r.-')
plot(x4,wdat['QU_D_CT'][9:10],'bo')
plot(x4,wdat['QU_D_RT'][9:10],'go')
plot(x4,wdat['QU_D_WT'][9:10],'ro')
xlabel('Region')
ylabel('Peak Width Difference')

ax4=subplot(234,sharex=ax1,sharey=ax1)
title('CP')
plot(x1,wdat['CP_D_CT'][0:4],'bo-')
plot(x1,wdat['CP_D_RT'][0:4],'go-')
plot(x1,wdat['CP_D_WT'][0:4],'ro-')
plot(x2,wdat['CP_D_CT'][4:7],'bs-')
plot(x2,wdat['CP_D_RT'][4:7],'gs-')
plot(x2,wdat['CP_D_WT'][4:7],'rs-')
plot(x3,wdat['CP_D_CT'][7:9],'b.-')
plot(x3,wdat['CP_D_RT'][7:9],'g.-')
plot(x3,wdat['CP_D_WT'][7:9],'r.-')
plot(x4,wdat['CP_D_CT'][9:10],'bo')
plot(x4,wdat['CP_D_RT'][9:10],'go')
plot(x4,wdat['CP_D_WT'][9:10],'ro')
xlabel('Region')
ylabel('Peak Width Difference')

ax5=subplot(235,sharex=ax1,sharey=ax1)
title('EN')
plot(x1,wdat['EN_D_CT'][0:4],'bo-')
plot(x1,wdat['EN_D_RT'][0:4],'go-')
plot(x1,wdat['EN_D_WT'][0:4],'ro-')
plot(x2,wdat['EN_D_CT'][4:7],'bs-')
plot(x2,wdat['EN_D_RT'][4:7],'gs-')
plot(x2,wdat['EN_D_WT'][4:7],'rs-')
plot(x3,wdat['EN_D_CT'][7:9],'b.-')
plot(x3,wdat['EN_D_RT'][7:9],'g.-')
plot(x3,wdat['EN_D_WT'][7:9],'r.-')
plot(x4,wdat['EN_D_CT'][9:10],'bo')
plot(x4,wdat['EN_D_RT'][9:10],'go')
plot(x4,wdat['EN_D_WT'][9:10],'ro')
xlabel('Region')
ylabel('Peak Width Difference')

ax6=subplot(236,sharex=ax1,sharey=ax1)
title('EA')
plot(x1,wdat['EA_D_CT'][0:4],'bo-')
plot(x1,wdat['EA_D_RT'][0:4],'go-')
plot(x1,wdat['EA_D_WT'][0:4],'ro-')
plot(x2,wdat['EA_D_CT'][4:7],'bs-')
plot(x2,wdat['EA_D_RT'][4:7],'gs-')
plot(x2,wdat['EA_D_WT'][4:7],'rs-')
plot(x3,wdat['EA_D_CT'][7:9],'b.-')
plot(x3,wdat['EA_D_RT'][7:9],'g.-')
plot(x3,wdat['EA_D_WT'][7:9],'r.-')
plot(x4,wdat['EA_D_CT'][9:10],'bo')
plot(x4,wdat['EA_D_RT'][9:10],'go')
plot(x4,wdat['EA_D_WT'][9:10],'ro')
xlabel('Region')
ylabel('Peak Width Difference')

ax1.set_xticks(xticks)
ax1.set_xticklabels(xlab)
ax1.grid()
ax2.grid()
ax3.grid()
ax4.grid()
ax5.grid()
ax6.grid()

tight_layout()
showme()
clf()

