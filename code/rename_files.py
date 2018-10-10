import os
fdir = '/Users/andrewkim/Documents/AA_Discharge/Fujitsu_A1_RTChargedThresh/'

fils = os.listdir(fdir)
# print fils
# print '5'.zfill(4)
oldstr = 'Fujitsu_A1_RT_Charged'
newstr = 'Fujitsu_A1_RT_Charged_'
for f in fils:
    try:
        fold = fdir+f
        fnew = fold.replace(oldstr,newstr)
        print fnew
        os.rename(fold,fnew)
    except Exception as E:
        print E
