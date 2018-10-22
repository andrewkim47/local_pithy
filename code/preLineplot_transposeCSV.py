from pithy import *

codes = [
# 'CP_B1_C_WT_TIFF',
# 'CP_B1_D_WT_TIFF',
# 'CP_C1_C_RT_TIFF',
# 'CP_C1_C_RT_TIFF',
# 'CP_C1_D_RT_TIFF',
# 'CP_D1_C_CT_TIFF',
# 'CP_D1_D_CT_TIFF',

'EA_B1_C_WT_TIFF',
'EA_B1_D_WT_TIFF',
'EA_C1_C_RT_TIFF',
'EA_C1_D_RT_TIFF',
'EA_C1R_C_CT_TIFF',
'EA_C1R_D_CT_TIFF',

# 'EN_A1_C_CT_TIFF',
# 'EN_A1_D_CT_TIFF',
# 'EN_B1_C_WT_TIFF',
# 'EN_B1_D_WT_TIFF',
# 'EN_C1_C_RT_TIFF',
# 'EN_RT_D_RT_TIFF',

# 'ER_A1_C_RT_TIFF',
# 'ER_A1_D_RT_TIFF',
# 'ER_B1_C_WT_TIFF',
# 'ER_B1_D_WT_TIFF',
# 'ER_C1_C_CT_TIFF',
# 'ER_CT_D_CT_TIFF',

# 'FU_A1_C_RT_TIFF',
# 'FU_A1_D_RT_TIFF',
# 'FU_B1_C_WT_TIFF',
# 'FU_B1_D_WT_TIFF',
# 'FU_D1_C_CT_TIFF',
# 'FU_D1_D_CT_TIFF',

# 'QU_B1_C_WT_TIFF',
# 'QU_B1_D_WT_TIFF',
# 'QU_C1_C_RT_TIFF',
# 'QU_C1_D_RT_TIFF',
# 'QU_D1_C_CT_TIFF',
# 'QU_D1_D_CT_TIFF',
]



for code in codes:
    fdir = '/Users/andrewkim/Documents/AA_Discharge/TIFFS/' + code + '/Linescan/'

    fils = sorted(glob(fdir+'pre_Linescans_Sep16.csv'))
    for fil in fils:
        print fil
        fil1 = fil
        fil2 = fil.replace('pre_','')
        pd.read_csv(fil1, index_col=0, header=None, sep='\t').T.to_csv(fil2,index=False)

# print data
# plot(data['bin'],data['counts'])
# showme()