from pithy import *

fils1 = sorted(glob('/Users/andrewkim/Documents/AA_Discharge/TIFFS/EcoAdvanced_B1_Discharged_Warm50_TIFF/Histograms/Hist_Sep_Band_B1*.csv'))

print fils1


# i=0
# for fil in fils:
#     rawdata = pd.read_csv(fil,sep='\t',skiprows=0)
#     # print rawdata
#     data = rawdata.groupby(['b']).mean()
#     means[i] = array(data['mean'])
#     i+=1
#     # means.append(data['mean'].mean())
#     # stds.append(data['std'].mean())
    


# # # hist(means, len(means), facecolor='blue', alpha=0.5)
# # # bar(range(len(means)),means,yerr=stds)
# x1 = range(1,7,1)
# x2 = range(6,0,-1)

# subplot(211)
# title('Pin')
# bar(x1,means[0])
# xlabel('Region')
# ylabel('Average Pixel Intensity')
# ylim(60,100)

# subplot(212)
# title('Sep')
# bar(x2,means[1])
# xlabel('Region')
# ylabel('Average Pixel Intensity')
# ylim(60,100)

# tight_layout()
# showme()
# clf()
