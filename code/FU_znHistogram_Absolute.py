from Histogram_Band import *
bins = range(256)
numband = 5

fdir = '/Users/andrewkim/Documents/AA_Discharge/TIFFS/'
fdir2 = '/Users/andrewkim/Documents/AA_Discharge/data/'



biglist = [
    [
    'FU_C_CT',    
    'FU_C_RT',    
    'FU_C_WT',    
    'FU_D_CT',    
    'FU_D_RT',    
    'FU_D_WT',    
    ],
    [
    'ER_C_CT',    
    'ER_C_RT',    
    'ER_C_WT',    
    'ER_D_CT',    
    'ER_D_RT',    
    'ER_D_WT',    
    ],
    [
    'QU_C_CT',    
    'QU_C_RT',    
    'QU_C_WT',    
    'QU_D_CT',    
    'QU_D_RT',    
    'QU_D_WT',    
    ],
    [
    'CP_C_CT',    
    'CP_C_RT',    
    'CP_C_WT',    
    'CP_D_CT',    
    'CP_D_RT',    
    'CP_D_WT',    
    ],
    [
    'EN_C_CT',    
    'EN_C_RT',    
    'EN_C_WT',    
    'EN_D_CT',    
    'EN_D_RT',    
    'EN_D_WT',    
    ],
    [
    'EA_C_CT',    
    'EA_C_RT',    
    'EA_C_WT',    
    'EA_D_CT',    
    'EA_D_RT',    
    'EA_D_WT',    
    ]

]

for kees in biglist:
    for key in kees:
        code = datas[key]['code']
        folder = fdir + code + '/Histogram/'
        endp = datas[key]['endpoint']
        ndata,adata,bands = getBandHist(folder)
        # datas[code]['ndata'] = ndata
        # datas[code]['adata'] = adata
        # datas[key]['zband'] = mergeBand(ndata,endp[0],endp[1],numband)
        # datas[key]['mband'] = mergeBand(ndata,endp[2],endp[3],numband)
        # datas[key]['aband'] = mergeBand(ndata,endp[0],endp[1],1,norm=True) #raw value
        
        datas[key]['Zband'] = mergeBand(ndata,endp[0],endp[1],numband,norm=False) #raw value
        datas[key]['Aband'] = mergeBand(ndata,endp[0],endp[1],1,norm=False) #raw value

        print key
    
# # datas[key]['zband'][0].to_csv(fdir2+'FU_Zn_Region0_Norm.csv')
# # datas[key]['zband'][1].to_csv(fdir2+'FU_Zn_Region1_Norm.csv')
# # datas[key]['zband'][2].to_csv(fdir2+'FU_Zn_Region2_Norm.csv')
# # datas[key]['zband'][3].to_csv(fdir2+'FU_Zn_Region3_Norm.csv')
# # datas[key]['zband'][4].to_csv(fdir2+'FU_Zn_Region4_Norm.csv')
# # datas[key]['Zband'][0].to_csv(fdir2+'FU_Zn_RegionAll_Norm.csv')
# # datas[key]['Aband'][0].to_csv(fdir2+'FU_Zn_RegionAll_Raw.csv')
    
    # #####
    # #####
    # figure(figsize=(6.4*3,4.8*2))
    
    # key = kees[0]
    # subplot(231)
    # title(key+' Zn')
    # for i in range(numband):
    #     plot(datas[key]['Zband'][i],label=i)
    # plot(datas[key]['Aband'][0],lw=3,c='k',label='all')    
    # legend(loc='best')
    # xlabel('Pixel Value')    
    # ylabel('Relative Counts')
    # xlim(-5,260)
    
    # key = kees[1]
    # subplot(232)
    # title(key+' Zn')
    # for i in range(numband):
    #     plot(datas[key]['Zband'][i],label=i)
    # plot(datas[key]['Aband'][0],lw=3,c='k',label='all')    
    # legend(loc='best')
    # xlabel('Pixel Value')    
    # ylabel('Relative Counts')
    # xlim(-5,260)
    
    # key = kees[2]
    # subplot(233)
    # title(key+' Zn')
    # for i in range(numband):
    #     plot(datas[key]['Zband'][i],label=i)
    # plot(datas[key]['Aband'][0],lw=3,c='k',label='all')    
    # legend(loc='best')
    # xlabel('Pixel Value')    
    # ylabel('Relative Counts')
    # xlim(-5,260)
    
    # key = kees[3]
    # subplot(234)
    # title(key+' Zn')
    # for i in range(numband):
    #     plot(datas[key]['Zband'][i],label=i)
    # plot(datas[key]['Aband'][0],lw=3,c='k',label='all')    
    # legend(loc='best')
    # xlabel('Pixel Value')    
    # ylabel('Relative Counts')
    # xlim(-5,260)
    
    # key = kees[4]
    # subplot(235)
    # title(key+' Zn')
    # for i in range(numband):
    #     plot(datas[key]['Zband'][i],label=i)
    # plot(datas[key]['Aband'][0],lw=3,c='k',label='all')    
    # legend(loc='best')
    # xlabel('Pixel Value')    
    # ylabel('Relative Counts')
    # xlim(-5,260)
    
    # key = kees[5]
    # subplot(236)
    # title(key+' Zn')
    # for i in range(numband):
    #     plot(datas[key]['Zband'][i],label=i)
    # plot(datas[key]['Aband'][0],lw=3,c='k',label='all')    
    # legend(loc='best')
    # xlabel('Pixel Value')    
    # ylabel('Relative Counts')
    # xlim(-5,260)
    
    # tight_layout()
    # showme()
    # clf()
