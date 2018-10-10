from pithy import *
def getBandHist(fdir):
    datas = pd.DataFrame()

    fils = sorted(glob(fdir+'Hist_Bands*.csv'))
    bands = []
    for fil in fils:
        suff = fil.split('/')[-1]
        B = suff.split('_')[2][0:5]
        bands.append(B)
    bands = unique(bands)
    # print bands
    
    for band in bands:
        tempDatas = pd.DataFrame()
        for fil in fils:
            if band in fil: 
                suff = fil.split('/')[-1]
                N = int(suff.split('_')[3][1:5])
                data = pd.read_csv(fil,sep='\t',skiprows=1)['counts']
                tempDatas[N] = data
                # data['Band'] = 
        datas[band] = tempDatas.sum(axis=1)
    alldatas = datas.copy() #adata keeps the counts for bin 0
    datas.loc[0,:]= 0
    ndatas = datas/datas.sum(axis=0)
    return datas,alldatas,bands


def mergeBand(df,start=0,end=None,num=5,norm=True):
    columns = list(df)
    if end == None: end = df.shape[1]
    outp = pd.DataFrame()
    arrays = array_split(arange(start,end),num)
    
    for n in range(len(arrays)):
        ista = arrays[n][0]
        iend = arrays[n][-1]
        tempval = df.loc[:,columns[ista]:columns[iend]].sum(axis=1)
        
        if norm ==True: outp[n] = tempval/tempval.sum(axis=0)
        else: outp[n] = tempval
    return outp
    
datas = dict()

datas['CP_C_WT'] = dict()
datas['CP_D_WT'] = dict()
datas['CP_C_RT'] = dict()
datas['CP_D_RT'] = dict()
datas['CP_C_CT'] = dict()
datas['CP_D_CT'] = dict()

datas['CP_C_WT']['code'] = 'CP_B1_C_WT_TIFF'
datas['CP_D_WT']['code'] = 'CP_B1_D_WT_TIFF'
datas['CP_C_RT']['code'] = 'CP_C1_C_RT_TIFF'
datas['CP_D_RT']['code'] = 'CP_C1_D_RT_TIFF'
datas['CP_C_CT']['code'] = 'CP_D1_C_CT_TIFF'
datas['CP_D_CT']['code'] = 'CP_D1_D_CT_TIFF'

datas['CP_C_WT']['endpoint'] = [5,25,30,46]
datas['CP_D_WT']['endpoint'] = [6,24,28,46]
datas['CP_C_RT']['endpoint'] = [4,25,31,45]
datas['CP_D_RT']['endpoint'] = [5,24,29,46]
datas['CP_C_CT']['endpoint'] = [6,25,31,46]
datas['CP_D_CT']['endpoint'] = [5,24,28,45]    

datas['FU_C_WT'] = dict()
datas['FU_D_WT'] = dict()
datas['FU_C_RT'] = dict()
datas['FU_D_RT'] = dict()
datas['FU_C_CT'] = dict()
datas['FU_D_CT'] = dict()

datas['FU_C_WT']['code'] = 'FU_B1_C_WT_TIFF'
datas['FU_D_WT']['code'] = 'FU_B1_D_WT_TIFF'
datas['FU_C_RT']['code'] = 'FU_A1_C_RT_TIFF'
datas['FU_D_RT']['code'] = 'FU_A1_D_RT_TIFF'
datas['FU_C_CT']['code'] = 'FU_D1_C_CT_TIFF'
datas['FU_D_CT']['code'] = 'FU_D1_D_CT_TIFF'

datas['FU_C_WT']['endpoint'] = [7,26,30,46]
datas['FU_D_WT']['endpoint'] = [8,24,28,45]
datas['FU_C_RT']['endpoint'] = [6,26,29,45]
datas['FU_D_RT']['endpoint'] = [5,24,27,46]
datas['FU_C_CT']['endpoint'] = [6,26,30,45]
datas['FU_D_CT']['endpoint'] = [6,24,28,45]

datas['QU_C_WT'] = dict()
datas['QU_D_WT'] = dict()
datas['QU_C_RT'] = dict()
datas['QU_D_RT'] = dict()
datas['QU_C_CT'] = dict()
datas['QU_D_CT'] = dict()

datas['QU_C_WT']['code'] = 'QU_B1_C_WT_TIFF'
datas['QU_D_WT']['code'] = 'QU_B1_D_WT_TIFF'
datas['QU_C_RT']['code'] = 'QU_C1_C_RT_TIFF'
datas['QU_D_RT']['code'] = 'QU_C1_D_RT_TIFF'
datas['QU_C_CT']['code'] = 'QU_D1_C_CT_TIFF'
datas['QU_D_CT']['code'] = 'QU_D1_D_CT_TIFF'

datas['QU_C_WT']['endpoint'] = [6,26,30,46]
datas['QU_D_WT']['endpoint'] = [6,23,28,46]
datas['QU_C_RT']['endpoint'] = [6,27,30,46]
datas['QU_D_RT']['endpoint'] = [6,24,28,46]
datas['QU_C_CT']['endpoint'] = [5,24,30,46]
datas['QU_D_CT']['endpoint'] = [5,24,28,46]


datas['EN_C_WT'] = dict()
datas['EN_D_WT'] = dict()
datas['EN_C_RT'] = dict()
datas['EN_D_RT'] = dict()
datas['EN_C_CT'] = dict()
datas['EN_D_CT'] = dict()

datas['EN_C_WT']['code'] = 'EN_B1_C_WT_TIFF'
datas['EN_D_WT']['code'] = 'EN_B1_D_WT_TIFF'
datas['EN_C_RT']['code'] = 'EN_C1_C_RT_TIFF'
datas['EN_D_RT']['code'] = 'EN_RT_D_RT_TIFF'
datas['EN_C_CT']['code'] = 'EN_A1_C_CT_TIFF'
datas['EN_D_CT']['code'] = 'EN_A1_D_CT_TIFF'

datas['EN_C_WT']['endpoint'] = [7,26,30,46]
datas['EN_D_WT']['endpoint'] = [6,25,28,46]
datas['EN_C_RT']['endpoint'] = [6,25,30,45]
datas['EN_D_RT']['endpoint'] = [5,24,28,47]
datas['EN_C_CT']['endpoint'] = [6,26,30,45]
datas['EN_D_CT']['endpoint'] = [6,24,28,45]

datas['EA_C_WT'] = dict()
datas['EA_D_WT'] = dict()
datas['EA_C_RT'] = dict()
datas['EA_D_RT'] = dict()
datas['EA_C_CT'] = dict()
datas['EA_D_CT'] = dict()

datas['EA_C_WT']['code'] = 'EA_B1_C_WT_TIFF'
datas['EA_D_WT']['code'] = 'EA_B1_D_WT_TIFF'
datas['EA_C_RT']['code'] = 'EA_C1_C_RT_TIFF'
datas['EA_D_RT']['code'] = 'EA_C1_D_RT_TIFF'
datas['EA_C_CT']['code'] = 'EA_C1R_C_CT_TIFF'
datas['EA_D_CT']['code'] = 'EA_C1R_D_CT_TIFF'

datas['EA_C_WT']['endpoint'] = [5,27,30,46]
datas['EA_D_WT']['endpoint'] = [5,26,29,46]
datas['EA_C_RT']['endpoint'] = [6,27,30,46]
datas['EA_D_RT']['endpoint'] = [5,25,28,46]
datas['EA_C_CT']['endpoint'] = [6,27,30,46]
datas['EA_D_CT']['endpoint'] = [7,25,27,46]


datas['ER_C_WT'] = dict()
datas['ER_D_WT'] = dict()
datas['ER_C_RT'] = dict()
datas['ER_D_RT'] = dict()
datas['ER_C_CT'] = dict()
datas['ER_D_CT'] = dict()

datas['ER_C_WT']['code'] = 'ER_B1_C_WT_TIFF'
datas['ER_D_WT']['code'] = 'ER_B1_D_WT_TIFF'
datas['ER_C_RT']['code'] = 'ER_A1_C_RT_TIFF'
datas['ER_D_RT']['code'] = 'ER_A1_D_RT_TIFF'
datas['ER_C_CT']['code'] = 'ER_C1_C_CT_TIFF'
datas['ER_D_CT']['code'] = 'ER_CT_D_CT_TIFF'

datas['ER_C_WT']['endpoint'] = [7,27,30,45]
datas['ER_D_WT']['endpoint'] = [7,25,28,45]
datas['ER_C_RT']['endpoint'] = [5,26,30,45]
datas['ER_D_RT']['endpoint'] = [5,24,27,45]
datas['ER_C_CT']['endpoint'] = [5,26,30,45]
datas['ER_D_CT']['endpoint'] = [8,24,28,45]
    

if __name__=="__main__":
    # print arange(0,0)
    pre = '/Users/andrewkim/Documents/AA_Discharge/TIFFS/'
    
    # code = 'CP_B1_D_WT_TIFF'
    codes = [
        # 'QU_B1_C_WT_TIFF',
        'QU_B1_D_WT_TIFF',
        # 'QU_C1_C_RT_TIFF',
        'QU_C1_D_RT_TIFF',
        # 'QU_D1_C_CT_TIFF',
        'QU_D1_D_CT_TIFF',
        ]
    
    for code in codes:
        fdir  = pre + code + '/Histogram/'
        bins = range(256)
        datas,ndatas,bands = getBandHist(fdir)
        
        band = mergeBand(datas,5,25,5)
        plot(band[0],label=0)
        plot(band[1],label=1)
        plot(band[2],label=2)
        plot(band[3],label=3)
        plot(band[4],label=4)
        legend()
        showme()
        clf()
        
        band = mergeBand(datas,5,25,1)
        plot(band[0],label=0)
        # plot(band[1],label=1)
        # plot(band[2],label=2)
        # plot(band[3],label=3)
        # plot(band[4],label=4)
        legend()
        showme()
        clf()

    
    
