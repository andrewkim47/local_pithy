from pithy import *
# import matplotlib as mpl
rcParams['font.size'] = 14
rcParams['legend.fontsize'] = 14
# rcParams['figure.titlesize'] = 18





C_CT = [
    59.50 , #FU_D1_C_CT
    64.66 , #ER_C1_C_CT
    31.30 , #QU_D1_C_CT
    34.95 , #CP_D1_C_CT
    55.75 , #EN_A1_C_CT
    49.47 , #EA_C1R_C_CT
]

D_CT = [
    7.20 , #FU_D1_D_CT
    7.08 , #ER_CT_D_CT
    2.06 , #QU_D1_D_CT
    5.55 , #CP_D1_D_CT
    8.65 , #EN_A1_D_CT
    7.87 , #EA_C1R_D_CT    
]

C_RT = [
    58.07 , #FU_A1_C_RT
    65.53 , #EV_A1_C_RT
    32.21 , #QU_C1_C_RT
    33.48 , #CP_C1_C_RT
    52.25 , #EN_C1_C_RT
    50.66 , #EA_C1_C_RT
]

D_RT = [
    22.39 , #FU_A1_D_RT
    23.63 , #EV_A1_D_RT
    6.08 , #QU_C1_D_RT
    13.96 , #CP_C1_D_RT
    33.14   ,#EN
    16.85 , #EA_C1_D_RT

]

C_WT = [
    61.94 , #FU_B1_C_WT
    66.31 , #EV_B1_C_WT
    32.71 , #QU_B1_C_WT
    32.35 , #CP_B1_C_WT
    57.07 , #EN_B1_C_WT
    52.08 , #EA_B1_C_WT
]

D_WT = [
    31.75 , #FU_B1_D_WT
    52.46 , #EV_B1_D_WT
    3.58 , #QU_B1_D_WT
    3.23 , #CP_B1_D_WT
    29.18 , #EN_B1_D_WT
    27.32 , #EA_B1_D_WT
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



rects1 = ax.bar(x1, C_CT, width, color='y')
rects2 = ax.bar(x2, D_CT, width, color='b')
rects3 = ax.bar(x3, C_RT, width, color='y')
rects4 = ax.bar(x4, D_RT, width, color='g')
rects5 = ax.bar(x5, C_WT, width, color='y')
rects6 = ax.bar(x6, D_WT, width, color='r')
# add some text for labels, title and axes ticks
ax.set_ylabel('Void Fraction')
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
showme()
clf()










