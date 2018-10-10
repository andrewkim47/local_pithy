from pithy import *

codes = [
'CP_B1_C_WT_TIFF',
'CP_B1_D_WT_TIFF',
'CP_C1_C_RT_TIFF',
'CP_C1_D_RT_TIFF',
'CP_D1_C_CT_TIFF',
'CP_D1_D_CT_TIFF',

'QU_B1_C_WT_TIFF',
'QU_B1_D_WT_TIFF',
'QU_C1_C_RT_TIFF',
'QU_C1_D_RT_TIFF',
'QU_D1_C_CT_TIFF',
'QU_D1_D_CT_TIFF',

'EN_A1_D_CT_TIFF',
'EN_B1_C_WT_TIFF',
'EN_B1_D_WT_TIFF',
'EN_C1_C_RT_TIFF',
'EN_C1_D_RT_TIFF',

'EA_B1_C_WT_TIFF',
'EA_B1_D_WT_TIFF',
'EA_C1_C_RT_TIFF',
'EA_C1_D_RT_TIFF',
'EA_C1R_C_CT_TIFF',
'EA_C1R_D_CT_TIFF',

'FU_A1_C_RT_TIFF',
'FU_A1_D_RT_TIFF',
'FU_B1_C_WT_TIFF',
'FU_B1_D_WT_TIFF',
'FU_C1_C_RT_TIFF',
'FU_C1_D_RT_TIFF',
'FU_D1_C_CT_TIFF',
'FU_D1_D_CT_TIFF',

'ER_A1_C_RT_TIFF',
'ER_A1_D_RT_TIFF',
'ER_B1_C_WT_TIFF',
'ER_B1_D_WT_TIFF',


]



for code in codes:
    fdir = '/Users/andrewkim/Documents/AA_Discharge/TIFFS/'+code+'/Histogram/'
    
    datas = pd.DataFrame()
    
    fils = sorted(glob(fdir+'Hist_Por*.csv'))
    # print len(fils)
    n = 0
    for fil in fils:
        # print code
        # print fil
        data = pd.read_csv(fil,sep='\t',skiprows=0)
        datas[n] = data['counts']
        # print fil
        n+=1

    datas['tot'] = datas.sum(axis=1)
    datas['bin'] = data['bin']
    # datas['tot'] = datas['tot']/sum(datas['tot'])
    
    
    blacks = float(sum(datas['tot'][0]))
    whites = float(sum(datas['tot'][255]))
    
    porosity = blacks/(blacks+whites)
    
    # if 'D_WT' in code: print code+'\t'+str(porosity)
    print code+'\t'+str(porosity)
    
    # plot(datas['bin'],datas['tot'])
    # showme()
    # clf()
    
    x1 = range(1,7,1)
    x2 = range(6,0,-1)
    
    
    # bar(datas['bin'],datas['tot'])
    # xlabel('Region')
    # ylabel('Average Pixel Intensity')
    # xlim(-50,300)
    # tight_layout()
    # showme()
    # clf()
    
    

    
    
    
