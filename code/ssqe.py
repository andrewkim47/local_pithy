from Histogram_Band import *

def ssqe(v1,v2):
    vdif = v1-v2
    return sum(np.multiply(vdif,vdif))
    
fdir = '/Users/andrewkim/Documents/AA_Discharge/TIFFS/'

x=arange(256)

#Grab Data
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
    # 'FU_C_CT',
    # 'FU_C_RT',
    # 'FU_C_WT',
    # 'ER_C_CT',
    # 'ER_C_RT',
    # 'ER_C_WT',
    # 'QU_C_CT',
    # 'QU_C_RT',
    # 'QU_C_WT',
    # 'CP_C_CT',
    # 'CP_C_RT',
    # 'CP_C_WT',
    # 'EN_C_CT',
    # 'EN_C_RT',
    # 'EN_C_WT',
    # 'EA_C_CT',
    # 'EA_C_RT',
    # 'EA_C_WT',
    ]
    
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

fdir2 = '/Users/andrewkim/Documents/AA_Discharge/data/'

df = pd.DataFrame()
df['lab'] = ticklabel
for key in kees:
    code = datas[key]['code']
    fil = fdir2 + key + '.csv'
    data = np.loadtxt(fil)*1000
    df[key] = data.transpose()

df = df[df['lab']!='n'].reset_index(drop=True)
# df.to_csv(fdir2+'ssq.csv',index=False)

# print df['lab']

x1 = arange(1,5)
x2 = arange(5,8)
x3 = arange(8,10)
x4 = arange(10,11)

xlab = ['','0-1','1-2','2-3','3-4','0-2','1-3','2-4','0-3','1-4','0-4']
xticks = arange(0,11)

# xlab = ['','01',''


xs = np.concatenate([x1,x2,x3,x4])

figure(figsize=(6.4*2,4.8*1.5))

ax1=subplot(231)
title('FU')
plot(x1,df['FU_D_CT'].tolist()[0:4],'bo-')
plot(x1,df['FU_D_RT'].tolist()[0:4],'go-')
plot(x1,df['FU_D_WT'].tolist()[0:4],'ro-')
plot(x2,df['FU_D_CT'].tolist()[4:7],'bs-')
plot(x2,df['FU_D_RT'].tolist()[4:7],'gs-')
plot(x2,df['FU_D_WT'].tolist()[4:7],'rs-')
plot(x3,df['FU_D_CT'].tolist()[7:9],'b.-')
plot(x3,df['FU_D_RT'].tolist()[7:9],'g.-')
plot(x3,df['FU_D_WT'].tolist()[7:9],'r.-')
plot(x4,df['FU_D_CT'].tolist()[9:10],'bo')
plot(x4,df['FU_D_RT'].tolist()[9:10],'go')
plot(x4,df['FU_D_WT'].tolist()[9:10],'ro')
xlabel('Position')
ylabel('Squared Difference')

# showme()
ax2=subplot(232,sharex=ax1,sharey=ax1)
title('ER')
plot(x1,df['ER_D_CT'].tolist()[0:4],'bo-')
plot(x1,df['ER_D_RT'].tolist()[0:4],'go-')
plot(x1,df['ER_D_WT'].tolist()[0:4],'ro-')
plot(x2,df['ER_D_CT'].tolist()[4:7],'bs-')
plot(x2,df['ER_D_RT'].tolist()[4:7],'gs-')
plot(x2,df['ER_D_WT'].tolist()[4:7],'rs-')
plot(x3,df['ER_D_CT'].tolist()[7:9],'b.-')
plot(x3,df['ER_D_RT'].tolist()[7:9],'g.-')
plot(x3,df['ER_D_WT'].tolist()[7:9],'r.-')
plot(x4,df['ER_D_CT'].tolist()[9:10],'bo')
plot(x4,df['ER_D_RT'].tolist()[9:10],'go')
plot(x4,df['ER_D_WT'].tolist()[9:10],'ro')
xlabel('Position')
ylabel('Squared Difference')

ax3=subplot(233,sharex=ax1,sharey=ax1)
title('QU')
plot(x1,df['QU_D_CT'].tolist()[0:4],'bo-')
plot(x1,df['QU_D_RT'].tolist()[0:4],'go-')
plot(x1,df['QU_D_WT'].tolist()[0:4],'ro-')
plot(x2,df['QU_D_CT'].tolist()[4:7],'bs-')
plot(x2,df['QU_D_RT'].tolist()[4:7],'gs-')
plot(x2,df['QU_D_WT'].tolist()[4:7],'rs-')
plot(x3,df['QU_D_CT'].tolist()[7:9],'b.-')
plot(x3,df['QU_D_RT'].tolist()[7:9],'g.-')
plot(x3,df['QU_D_WT'].tolist()[7:9],'r.-')
plot(x4,df['QU_D_CT'].tolist()[9:10],'bo')
plot(x4,df['QU_D_RT'].tolist()[9:10],'go')
plot(x4,df['QU_D_WT'].tolist()[9:10],'ro')
xlabel('Position')
ylabel('Squared Difference')

ax4=subplot(234,sharex=ax1,sharey=ax1)
title('CP')
plot(x1,df['CP_D_CT'].tolist()[0:4],'bo-')
plot(x1,df['CP_D_RT'].tolist()[0:4],'go-')
plot(x1,df['CP_D_WT'].tolist()[0:4],'ro-')
plot(x2,df['CP_D_CT'].tolist()[4:7],'bs-')
plot(x2,df['CP_D_RT'].tolist()[4:7],'gs-')
plot(x2,df['CP_D_WT'].tolist()[4:7],'rs-')
plot(x3,df['CP_D_CT'].tolist()[7:9],'b.-')
plot(x3,df['CP_D_RT'].tolist()[7:9],'g.-')
plot(x3,df['CP_D_WT'].tolist()[7:9],'r.-')
plot(x4,df['CP_D_CT'].tolist()[9:10],'bo')
plot(x4,df['CP_D_RT'].tolist()[9:10],'go')
plot(x4,df['CP_D_WT'].tolist()[9:10],'ro')
xlabel('Position')
ylabel('Squared Difference')

ax5=subplot(235,sharex=ax1,sharey=ax1)
title('EN')
plot(x1,df['EN_D_CT'].tolist()[0:4],'bo-')
plot(x1,df['EN_D_RT'].tolist()[0:4],'go-')
plot(x1,df['EN_D_WT'].tolist()[0:4],'ro-')
plot(x2,df['EN_D_CT'].tolist()[4:7],'bs-')
plot(x2,df['EN_D_RT'].tolist()[4:7],'gs-')
plot(x2,df['EN_D_WT'].tolist()[4:7],'rs-')
plot(x3,df['EN_D_CT'].tolist()[7:9],'b.-')
plot(x3,df['EN_D_RT'].tolist()[7:9],'g.-')
plot(x3,df['EN_D_WT'].tolist()[7:9],'r.-')
plot(x4,df['EN_D_CT'].tolist()[9:10],'bo')
plot(x4,df['EN_D_RT'].tolist()[9:10],'go')
plot(x4,df['EN_D_WT'].tolist()[9:10],'ro')
xlabel('Position')
ylabel('Squared Difference')

ax6=subplot(236,sharex=ax1,sharey=ax1)
title('EA')
plot(x1,df['EA_D_CT'].tolist()[0:4],'bo-')
plot(x1,df['EA_D_RT'].tolist()[0:4],'go-')
plot(x1,df['EA_D_WT'].tolist()[0:4],'ro-')
plot(x2,df['EA_D_CT'].tolist()[4:7],'bs-')
plot(x2,df['EA_D_RT'].tolist()[4:7],'gs-')
plot(x2,df['EA_D_WT'].tolist()[4:7],'rs-')
plot(x3,df['EA_D_CT'].tolist()[7:9],'b.-')
plot(x3,df['EA_D_RT'].tolist()[7:9],'g.-')
plot(x3,df['EA_D_WT'].tolist()[7:9],'r.-')
plot(x4,df['EA_D_CT'].tolist()[9:10],'bo')
plot(x4,df['EA_D_RT'].tolist()[9:10],'go')
plot(x4,df['EA_D_WT'].tolist()[9:10],'ro')
xlabel('Position')
ylabel('Squared Difference')

xlim(0,11)
ax1.set_xticks(xticks)
ax1.set_xticklabels(xlab)




tight_layout()
showme()
clf()




