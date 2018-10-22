from pithy import *
# import matplotlib as mpl
rcParams['font.size'] = 14
rcParams['legend.fontsize'] = 14
# rcParams['figure.titlesize'] = 18

C_CT = [
4.06827, #FU_D1_C_CT_TIFF_Separator_peaks.csv
4.08161, #ER_C1_C_CT_TIFF_Separator_peaks.csv
4.15362, #QU_D1_C_CT_TIFF_Separator_peaks.csv
4.14148, #CP_D1_C_CT_TIFF_Separator_peaks.csv
4.10445, #EN_A1_C_CT_TIFF_Separator_peaks.csv
4.23568, #EA_C1R_C_CT_TIFF_Separator_peaks.csv
]

D_CT = [
3.82290, #FU_D1_D_CT_TIFF_Separator_peaks.csv
3.88399, #ER_CT_D_CT_TIFF_Separator_peaks.csv
3.80464, #QU_D1_D_CT_TIFF_Separator_peaks.csv
3.80220, #CP_D1_D_CT_TIFF_Separator_peaks.csv
3.88695, #EN_A1_D_CT_TIFF_Separator_peaks.csv
3.86519, #EA_C1R_D_CT_TIFF_Separator_peaks.csv 
]

C_RT = [
4.07298, #FU_A1_C_RT_TIFF_Separator_peaks.csv
4.07898, #ER_A1_C_RT_TIFF_Separator_peaks.csv
4.20443, #QU_C1_C_RT_TIFF_Separator_peaks.csv
4.13018, #CP_C1_C_RT_TIFF_Separator_peaks.csv
4.07559, #EN_C1_C_RT_TIFF_Separator_peaks.csv
4.20201, #EA_C1_C_RT_TIFF_Separator_peaks.csv
]

D_RT = [
3.83179, #FU_A1_D_RT_TIFF_Separator_peaks.csv
3.82104, #ER_A1_D_RT_TIFF_Separator_peaks.csv
3.88916, #QU_C1_D_RT_TIFF_Separator_peaks.csv
3.82646, #CP_C1_D_RT_TIFF_Separator_peaks.csv
3.89401, #EN_RT_D_RT_TIFF_Separator_peaks.csv
3.89771, #EA_C1_D_RT_TIFF_Separator_peaks.csv
]

C_WT = [
4.06725, #FU_B1_C_WT_TIFF_Separator_peaks.csv
4.09864, #ER_B1_C_WT_TIFF_Separator_peaks.csv
4.19948, #QU_B1_C_WT_TIFF_Separator_peaks.csv
4.13494, #CP_B1_C_WT_TIFF_Separator_peaks.csv
4.11212, #EN_B1_C_WT_TIFF_Separator_peaks.csv
4.22305, #EA_B1_C_WT_TIFF_Separator_peaks.csv
]

D_WT = [
3.77949, #FU_B1_D_WT_TIFF_Separator_peaks.csv
3.80553, #ER_B1_D_WT_TIFF_Separator_peaks.csv
3.97276, #QU_B1_D_WT_TIFF_Separator_peaks.csv
3.86352, #CP_B1_D_WT_TIFF_Separator_peaks.csv
3.94814, #EN_B1_D_WT_TIFF_Separator_peaks.csv
3.96479, #EA_B1_D_WT_TIFF_Separator_peaks.csv
]


errC_CT = [
0.04267 ,#FU_D1_C_CT_TIFF_Separator_peaks.csv
0.04246 ,#ER_C1_C_CT_TIFF_Separator_peaks.csv
0.05078 ,#QU_D1_C_CT_TIFF_Separator_peaks.csv
0.05483 ,#CP_D1_C_CT_TIFF_Separator_peaks.csv
0.03405 ,#EN_A1_C_CT_TIFF_Separator_peaks.csv
0.02784 ,#EA_C1R_C_CT_TIFF_Separator_peaks.csv
]
errD_CT = [
0.05043 ,#FU_D1_D_CT_TIFF_Separator_peaks.csv
0.07245 ,#ER_CT_D_CT_TIFF_Separator_peaks.csv
0.07925 ,#QU_D1_D_CT_TIFF_Separator_peaks.csv
0.05795 ,#CP_D1_D_CT_TIFF_Separator_peaks.csv
0.03937 ,#EN_A1_D_CT_TIFF_Separator_peaks.csv
0.03102 ,#EA_C1R_D_CT_TIFF_Separator_peaks.csv
]
errC_RT = [
0.04484 ,#FU_A1_C_RT_TIFF_Separator_peaks.csv
0.03196 ,#ER_A1_C_RT_TIFF_Separator_peaks.csv
0.02732 ,#QU_C1_C_RT_TIFF_Separator_peaks.csv
0.05947 ,#CP_C1_C_RT_TIFF_Separator_peaks.csv
0.04294 ,#EN_C1_C_RT_TIFF_Separator_peaks.csv
0.03855 ,#EA_C1_C_RT_TIFF_Separator_peaks.csv
]
errD_RT = [
0.0502 ,#FU_A1_D_RT_TIFF_Separator_peaks.csv
0.04323 ,#ER_A1_D_RT_TIFF_Separator_peaks.csv
0.07054 ,#QU_C1_D_RT_TIFF_Separator_peaks.csv
0.05586 ,#CP_C1_D_RT_TIFF_Separator_peaks.csv
0.04705 ,#EN_RT_D_RT_TIFF_Separator_peaks.csv
0.05663 ,#EA_C1_D_RT_TIFF_Separator_peaks.csv
]
errC_WT = [
0.0463 ,#FU_B1_C_WT_TIFF_Separator_peaks.csv
0.03924 ,#ER_B1_C_WT_TIFF_Separator_peaks.csv
0.03574 ,#QU_B1_C_WT_TIFF_Separator_peaks.csv
0.07063 ,#CP_B1_C_WT_TIFF_Separator_peaks.csv
0.04171 ,#EN_B1_C_WT_TIFF_Separator_peaks.csv
0.04274 ,#EA_B1_C_WT_TIFF_Separator_peaks.csv
]
errD_WT = [
0.06179 ,#FU_B1_D_WT_TIFF_Separator_peaks.csv
0.04743 ,#ER_B1_D_WT_TIFF_Separator_peaks.csv
0.07011 ,#QU_B1_D_WT_TIFF_Separator_peaks.csv
0.08506 ,#CP_B1_D_WT_TIFF_Separator_peaks.csv
0.03449 ,#EN_B1_D_WT_TIFF_Separator_peaks.csv
0.02793 ,#EA_B1_D_WT_TIFF_Separator_peaks.csv
]



N = 6
width = 4
gap = 4
spacing = (width*6 + gap)

fig, ax = plt.subplots(figsize=(6.4*1.5,4.8*1.5))
x1 = arange(width*(1-1),(width*6+gap)*6,spacing)
x2 = arange(width*(2-1),(width*6+gap)*6,spacing)
x3 = arange(width*(3-1),(width*6+gap)*6,spacing)
x4 = arange(width*(4-1),(width*6+gap)*6,spacing)
x5 = arange(width*(5-1),(width*6+gap)*6,spacing)
x6 = arange(width*(6-1),(width*6+gap)*6,spacing)


tickind = (x4+x5)/2
ticklab = [
    'Fujitsu',
    'EverReady',
    'Quantum',
    'CopperTop',
    'Energizer',
    'EcoAdvanced',
]
    


# print x1
# print x2
# print x3
# print x4
# print x5
# print x6
# print '----'



rects1 = ax.bar(x1, C_CT, width, color='y',yerr=errC_CT)
rects2 = ax.bar(x2, D_CT, width, color='b',yerr=errD_CT)
rects3 = ax.bar(x3, C_RT, width, color='y',yerr=errC_RT)
rects4 = ax.bar(x4, D_RT, width, color='g',yerr=errD_RT)
rects5 = ax.bar(x5, C_WT, width, color='y',yerr=errC_WT)
rects6 = ax.bar(x6, D_WT, width, color='r',yerr=errD_WT)
# add some text for labels, title and axes ticks
ax.set_ylabel('Average Radial Distance (mm)')
# ax.set_xlabel('Sample')
# ax.set_title('AA TXM')

# print tickind
ax.set_xticks(tickind)
ax.set_xticklabels(ticklab)

ax.legend(
        (rects1[0], rects2[0],rects4[0],rects6[0]),
        ('Charged_RT', 'Discharged_CT','Discharged_RT','Discharged_WT'),
        loc='center right',bbox_to_anchor=(1.32, 0.5))
xlim(x1[0]-width,x6[-1]+2*width)
grid(axis='y')
title('Separator Center Position')
ylim(3.4,4.3)
showme()
clf()










