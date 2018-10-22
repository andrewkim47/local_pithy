from pithy import *

fdir = '/Users/andrewkim/Documents/AA_Discharge/data/'

fils = [
'FU_D1_C_CT_TIFF_Separator_peaks.csv',
'ER_C1_C_CT_TIFF_Separator_peaks.csv',
'QU_D1_C_CT_TIFF_Separator_peaks.csv',
'CP_D1_C_CT_TIFF_Separator_peaks.csv',
'EN_A1_C_CT_TIFF_Separator_peaks.csv',
'EA_C1R_C_CT_TIFF_Separator_peaks.csv',

'FU_D1_D_CT_TIFF_Separator_peaks.csv',
'ER_CT_D_CT_TIFF_Separator_peaks.csv',
'QU_D1_D_CT_TIFF_Separator_peaks.csv',
'CP_D1_D_CT_TIFF_Separator_peaks.csv',
'EN_A1_D_CT_TIFF_Separator_peaks.csv',
'EA_C1R_D_CT_TIFF_Separator_peaks.csv',

'FU_A1_C_RT_TIFF_Separator_peaks.csv',
'ER_A1_C_RT_TIFF_Separator_peaks.csv',
'QU_C1_C_RT_TIFF_Separator_peaks.csv',
'CP_C1_C_RT_TIFF_Separator_peaks.csv',
'EN_C1_C_RT_TIFF_Separator_peaks.csv',
'EA_C1_C_RT_TIFF_Separator_peaks.csv',
    
'FU_A1_D_RT_TIFF_Separator_peaks.csv',
'ER_A1_D_RT_TIFF_Separator_peaks.csv',
'QU_C1_D_RT_TIFF_Separator_peaks.csv',
'CP_C1_D_RT_TIFF_Separator_peaks.csv',
'EN_RT_D_RT_TIFF_Separator_peaks.csv',
'EA_C1_D_RT_TIFF_Separator_peaks.csv',

'FU_B1_C_WT_TIFF_Separator_peaks.csv',
'ER_B1_C_WT_TIFF_Separator_peaks.csv',
'QU_B1_C_WT_TIFF_Separator_peaks.csv',
'CP_B1_C_WT_TIFF_Separator_peaks.csv',
'EN_B1_C_WT_TIFF_Separator_peaks.csv',
'EA_B1_C_WT_TIFF_Separator_peaks.csv',

'FU_B1_D_WT_TIFF_Separator_peaks.csv',
'ER_B1_D_WT_TIFF_Separator_peaks.csv',
'QU_B1_D_WT_TIFF_Separator_peaks.csv',
'CP_B1_D_WT_TIFF_Separator_peaks.csv',
'EN_B1_D_WT_TIFF_Separator_peaks.csv',
'EA_B1_D_WT_TIFF_Separator_peaks.csv',

]

thics = dict()
cens1 = dict()
cens2 = dict()

def rmOutlier(dat,lo,hi):
    loval = np.percentile(dat,lo)
    hival = np.percentile(dat,hi)
    newdat = dat[(dat>=loval)&(dat<=hival)]
    return newdat

for i in range(len(fils)):
    fil = fdir+fils[i]
    data_pre = pd.read_csv(fil)
    data = data_pre[data_pre['cen']!=0]
    
    data['thic'] = data['upp']-data['low']
    data['cen2'] = (data['upp']+data['low'])/2.
    
    thics[i] = rmOutlier(data['thic'],10,90)
    cens1[i] = rmOutlier(data['cen'],10,90)
    cens2[i] = rmOutlier(data['cen2'],10,90)
    

    # print round(thics[i].mean(),4),',#'+fils[i]
    # print round(thics[i].std(),5),',#'+fils[i]
    
    # print cens1[i].mean(),'#'+fils[i]
    # print cens2[i].mean(),'#'+fils[i]
    print round(cens2[i].std(),5),',#'+fils[i]

