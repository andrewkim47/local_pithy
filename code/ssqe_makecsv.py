from Histogram_Band import *

def ssqe(v1,v2):
    vdif = v1-v2
    return sum(np.multiply(vdif,vdif))
    
fdir = '/Users/andrewkim/Documents/AA_Discharge/TIFFS/'

x=arange(256)

#Grab Data
kees = [
    'FU_C_CT', #'FU_D_CT',
    'FU_C_RT', #'FU_D_RT',
    'FU_C_WT', #'FU_D_WT',
    'ER_C_CT', #'ER_D_CT',
    'ER_C_RT', #'ER_D_RT',
    'ER_C_WT', #'ER_D_WT',
    'QU_C_CT', #'QU_D_CT',
    'QU_C_RT', #'QU_D_RT',
    'QU_C_WT', #'QU_D_WT',
    'CP_C_CT', #'CP_D_CT',
    'CP_C_RT', #'CP_D_RT',
    'CP_C_WT', #'CP_D_WT',
    'EN_C_CT', #'EN_D_CT',
    'EN_C_RT', #'EN_D_RT',
    'EN_C_WT', #'EN_D_WT',
    'EA_C_CT', #'EA_D_CT',
    'EA_C_RT', #'EA_D_RT',
    'EA_C_WT', #'EA_D_WT',
    ]
    
ticklabel = [
    '',
    '01',
    '12',
    '23',
    '34',
    '',
    '02',
    '13',
    '24',
    '',
    '03',
    '14',
    '',
    '04',
    
    
]   
xlim1 = (50,200)

ylim1 = (0,0.10)
ylim2 = (0,0.08)

fdir2 = '/Users/andrewkim/Documents/AA_Discharge/data/'

ssq = dict()
for key in kees:
    code = datas[key]['code']
    folder = fdir + code + '/Histogram/'
    endp = datas[key]['endpoint']
    ndata,adata,bands = getBandHist(folder)
    
    datas[key] = dict()
    
    x=arange(256)
    numband = 5
    datas[key]['zband'] = mergeBand(ndata,endp[0],endp[1],numband,norm=True)
    datas[key]['Zband'] = mergeBand(ndata,endp[0],endp[1],numband,norm=False)
    datas[key]['aband'] = mergeBand(ndata,endp[0],endp[1],1,norm=True)
    datas[key]['Aband'] = mergeBand(ndata,endp[0],endp[1],1,norm=False)
    # datas[key]['mband'] = mergeBand(ndata,endp[2],endp[3],numband)
    
    z0 = datas[key]['zband'][0]
    z1 = datas[key]['zband'][1]
    z2 = datas[key]['zband'][2]
    z3 = datas[key]['zband'][3]
    z4 = datas[key]['zband'][4]
    za = datas[key]['aband'][0]
    
    datas[key]['zband'][5] = datas[key]['aband'][0]
    
    ssq[key] = [0]
    ssq[key].append(ssqe(z0,z1))
    ssq[key].append(ssqe(z1,z2))
    ssq[key].append(ssqe(z2,z3))
    ssq[key].append(ssqe(z3,z4))
    ssq[key].append(0)
    ssq[key].append(ssqe(z0,z2))
    ssq[key].append(ssqe(z1,z3))
    ssq[key].append(ssqe(z2,z4))
    ssq[key].append(0)
    ssq[key].append(ssqe(z0,z3))
    ssq[key].append(ssqe(z1,z4))
    ssq[key].append(0)
    ssq[key].append(ssqe(z0,z4))
    
    

    x1 = range(len(ssq[key]))
    # fig, ax = plt.subplots()
    
    
    f, (ax1, ax2) = plt.subplots(2,1,figsize=(6.4,4.8*1.5))


    ax1.set_title(key)
    ax1.plot(x,datas[key]['zband'][0],label='0')
    ax1.plot(x,datas[key]['zband'][1],label='1')
    ax1.plot(x,datas[key]['zband'][2],label='2')
    ax1.plot(x,datas[key]['zband'][3],label='3')
    ax1.plot(x,datas[key]['zband'][4],label='4')
    ax1.plot(x,datas[key]['aband'][0],lw=3,c='k',label='all')
    ax1.set_xlabel('Pixel Value')
    ax1.set_ylabel('Normalized Counts in Region')
    ax1.legend()
    # ax1.set_ylim(ylim1)
    ax1.set_xlim(xlim1)
    
    ax2.rects1 = bar(x1,ssq[key])
    ax2.set_xticks(arange(len(x1))+0.5)
    ax2.set_xticklabels(ticklabel)
    ax2.set_xlabel('Regional Pairs')
    ax2.set_ylabel('SSD')
    if max(ssq[key]) <0.005:
        ax2.set_ylim(None)
    else: ax2.set_ylim(ylim2)
    
    tight_layout()
    showme()
    clf()
    
    # ssq[key].to_csv(fdir2+key+'.csv')
    np.savetxt(fdir2+key+'.csv',ssq[key])
    


# spacing = (width*1 + gap)

# x1 = arange(width*(1-1),(width*3+gap)*6,spacing)
# x2 = arange(width*(2-1),(width*3+gap)*6,spacing)
# x3 = arange(width*(3-1),(width*3+gap)*6,spacing)

# print x1
# print x2
# print x3

# tickind = [x1[0]+width/2.+spacing*(i) for i in range(N)]
# ticklab = [
#     # 'Fujitsu',
#     # 'EverReady',
#     # 'Quantum',
#     'CopperTop',
#     # 'Energizer',
#     # 'EcoAdvanced',
# ]

# # # print tickind

# fig, ax = plt.subplots()
# rects1 = ax.bar(x1, ssq[key], width, color='b')
# # rects2 = ax.bar(x2, room, width, color='g')
# # rects3 = ax.bar(x3, hott, width, color='r')
# # add some text for labels, title and axes ticks
# # ax.set_ylabel('Discharge Capacity (mAh)')
# # ax.set_xlabel('Sample')
# # ax.set_title('Discharge Capacity')
# # ax.set_xticks(tickind)
# # ax.set_xticks(ind + width)
# # ax.set_xticklabels(ticklab)
# # ax.legend(
# #         (rects1[0], rects2[0],rects3[0]),
# #         ('6.5'+deg,'20'+deg,'51.5'+deg),
# #         loc='center right',bbox_to_anchor=(1.27, 0.5))

# # # autolabel(rects1)
# # # autolabel(rects2)
# # xlim(x1[0]-width,x3[-1]+2*width)
# # grid(axis='y')
# showme()


