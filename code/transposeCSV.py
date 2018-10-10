from pithy import *

fdir = '/Users/andrewkim/Documents/AA_Discharge/TIFFS/EA_C1R_D_CT_TIFF/'


fils = sorted(glob(fdir+'pre_*.csv'))

for fil in fils:
    fil1 = fil
    fil2 = fil.replace('pre_','')
    pd.read_csv(fil1, index_col=0, header=None, sep='\t').T.to_csv(fil2,index=False)

# print data
# plot(data['bin'],data['counts'])
# showme()