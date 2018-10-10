from Histogram_Band import *
bins = range(256)
numband = 5

fdir = '/Users/andrewkim/Documents/AA_Discharge/TIFFS/'


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

for key in sorted(kees):
    code = datas[key]['code']
    folder = fdir + code + '/Histogram/'
    endp = datas[key]['endpoint']
    ndata,adata,bands = getBandHist(folder)
    # datas[code]['ndata'] = ndata
    # datas[code]['adata'] = adata
    datas[key]['zband'] = mergeBand(ndata,endp[0],endp[1],numband)
    datas[key]['mband'] = mergeBand(ndata,endp[2],endp[3],numband)
    
    datas[key]['Zband'] = mergeBand(ndata,endp[0],endp[1],numband,norm=False) #raw value
    datas[key]['aband'] = mergeBand(ndata,endp[0],endp[1],1,norm=True) #raw value
    datas[key]['Aband'] = mergeBand(ndata,endp[0],endp[1],1,norm=False) #raw value

    fdir2 = '/Users/andrewkim/Documents/AA_Discharge/data/'
    
    # datas[key]['zband'][0].to_csv(fdir2+'FU_Zn_Region0_Norm.csv')
    # datas[key]['zband'][1].to_csv(fdir2+'FU_Zn_Region1_Norm.csv')
    # datas[key]['zband'][2].to_csv(fdir2+'FU_Zn_Region2_Norm.csv')
    # datas[key]['zband'][3].to_csv(fdir2+'FU_Zn_Region3_Norm.csv')
    # datas[key]['zband'][4].to_csv(fdir2+'FU_Zn_Region4_Norm.csv')
    # datas[key]['Zband'][0].to_csv(fdir2+'FU_Zn_RegionAll_Norm.csv')
    # datas[key]['Aband'][0].to_csv(fdir2+'FU_Zn_RegionAll_Raw.csv')
    
    #####
    #####
    plot(datas[key]['Zband'][0],label=0)
    plot(datas[key]['Zband'][1],label=1)
    plot(datas[key]['Zband'][2],label=2)
    plot(datas[key]['Zband'][3],label=3)
    plot(datas[key]['Zband'][4],label=4)
    plot(datas[key]['Aband'][0],lw=3,c='k',label='all')
    title(key)
    showme()
    clf()
    
    # plot(datas[key]['zband'][0],label=0)
    # plot(datas[key]['zband'][1],label=1)
    # plot(datas[key]['zband'][2],label=2)
    # plot(datas[key]['zband'][3],label=3)
    # plot(datas[key]['zband'][4],label=4)
    # plot(datas[key]['aband'][0],lw=3,c='k',label='all')
    # showme()
    # clf()

