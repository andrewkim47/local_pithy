import os
from glob import glob



# code = 'CP_C1_C_WT_TIFF'
# fdir = '/Users/andrewkim/Documents/AA_Discharge/TIFFS/'+code+'/'
fdir = '/Users/andrewkim/Documents/AA_Discharge/TIFFS/CP_C1_C_RT_TIFF/'
# fils = sorted(glob(fdir+'zQU*'))
fils = sorted(glob(fdir+'*.js'))


for fil in fils:
    oldname = fil
    # newname = oldname.replace('XX_X1_C_RT',code)
    newname = oldname.replace('CP_C1_C_WT','CP_C1_C_RT')
    
    # print newname
    os.rename(oldname,newname)
    # print fil
    
# code = 'CP_C1_D_RT_TIFF';

# /Users/andrewkim/Documents/AA_Discharge/TIFFS/

