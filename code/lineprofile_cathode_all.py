from pithy import *

dropcols1 = ['N0L12', 'N0L13', 'N0L14', 'N1L12', 'N1L13', 'N1L14', 'N2L12', 'N2L13', 'N2L14', 'N3L12', 'N3L13', 'N3L14', 'N4L12', 'N4L13', 'N4L14', 'N5L12', 'N5L13', 'N5L14', 'N6L12', 'N6L13', 'N6L14', 'N7L12', 'N7L13', 'N7L14', 'N8L12', 'N8L13', 'N8L14', 'N9L12', 'N9L13', 'N9L14', 'N10L12', 'N10L13', 'N10L14', 'N11L12', 'N11L13', 'N11L14', 'N12L12', 'N12L13', 'N12L14', 'N13L12', 'N13L13', 'N13L14', 'N14L12', 'N14L13', 'N14L14', 'N15L12', 'N15L13', 'N15L14', 'N16L12', 'N16L13', 'N16L14', 'N17L12', 'N17L13', 'N17L14', 'N18L12', 'N18L13', 'N18L14', 'N19L12', 'N19L13', 'N19L14', 'N20L12', 'N20L13', 'N20L14', 'N21L12', 'N21L13', 'N21L14', 'N22L12', 'N22L13', 'N22L14', 'N23L12', 'N23L13', 'N23L14', 'N24L12', 'N24L13', 'N24L14', 'N25L12', 'N25L13', 'N25L14', 'N26L12', 'N26L13', 'N26L14', 'N27L12', 'N27L13', 'N27L14', 'N28L12', 'N28L13', 'N28L14', 'N29L12', 'N29L13', 'N29L14', 'N30L12', 'N30L13', 'N30L14', 'N31L12', 'N31L13', 'N31L14', 'N32L12', 'N32L13', 'N32L14']
dropcols2 = ['N0L12', 'N0L13', 'N0L14', 'N1L12', 'N1L13', 'N1L14', 'N2L12', 'N2L13', 'N2L14', 'N3L12', 'N3L13', 'N3L14', 'N4L12', 'N4L13', 'N4L14', 'N5L12', 'N5L13', 'N5L14', 'N6L12', 'N6L13', 'N6L14', 'N7L12', 'N7L13', 'N7L14', 'N8L12', 'N8L13', 'N8L14', 'N9L12', 'N9L13', 'N9L14', 'N10L12', 'N10L13', 'N10L14', 'N11L12', 'N11L13', 'N11L14', 'N12L12', 'N12L13', 'N12L14', 'N13L12', 'N13L13', 'N13L14', 'N14L12', 'N14L13', 'N14L14', 'N15L12', 'N15L13', 'N15L14', 'N16L12', 'N16L13', 'N16L14', 'N17L12', 'N17L13', 'N17L14', 'N18L12', 'N18L13', 'N18L14', 'N19L12', 'N19L13', 'N19L14', 'N20L12', 'N20L13', 'N20L14', 'N21L12', 'N21L13', 'N21L14', 'N22L12', 'N22L13', 'N22L14', 'N23L12', 'N23L13', 'N23L14', 'N24L12', 'N24L13', 'N24L14', 'N25L12', 'N25L13', 'N25L14', 'N26L12', 'N26L13', 'N26L14', 'N27L12', 'N27L13', 'N27L14', 'N28L12', 'N28L13', 'N28L14', 'N29L12', 'N29L13', 'N29L14', 'N30L12', 'N30L13', 'N30L14', 'N31L12', 'N31L13', 'N31L14', 'N32L12', 'N32L13', 'N32L14']

codes = [
# 'CP_B1_C_WT_TIFF',
# 'CP_B1_D_WT_TIFF',
# 'CP_C1_C_RT_TIFF',
# 'CP_C1_D_RT_TIFF',
# 'CP_D1_C_CT_TIFF',
# 'CP_D1_D_CT_TIFF',

# 'EA_B1_C_WT_TIFF',
# 'EA_B1_D_WT_TIFF',
# 'EA_C1_C_RT_TIFF',
# 'EA_C1_D_RT_TIFF',
# 'EA_C1R_C_CT_TIFF',
# 'EA_C1R_D_CT_TIFF',

# 'EN_B1_C_WT_TIFF',
# 'EN_B1_D_WT_TIFF',
# 'EN_C1_C_RT_TIFF',
# 'EN_RT_D_RT_TIFF',
# 'EN_A1_C_CT_TIFF',
# 'EN_A1_D_CT_TIFF',

'ER_B1_C_WT_TIFF',
'ER_B1_D_WT_TIFF',
'ER_A1_C_RT_TIFF',
'ER_A1_D_RT_TIFF',
'ER_C1_C_CT_TIFF',
'ER_CT_D_CT_TIFF',

# 'FU_B1_C_WT_TIFF',
# 'FU_B1_D_WT_TIFF',
# 'FU_A1_C_RT_TIFF',
# 'FU_A1_D_RT_TIFF',
# 'FU_D1_C_CT_TIFF',
# 'FU_D1_D_CT_TIFF',

# 'QU_B1_C_WT_TIFF',
# 'QU_B1_D_WT_TIFF',
# 'QU_C1_C_RT_TIFF',
# 'QU_C1_D_RT_TIFF',
# 'QU_D1_C_CT_TIFF',
# 'QU_D1_D_CT_TIFF',
]

cols = []
for N in range(33):
    for L in range(17):
        cols.append('N'+str(N)+'L'+str(L))

datas = dict()
# labls = dict()

for code in codes:
    hfile = '/Users/andrewkim/Documents/AA_Discharge/TIFFS/'+code+'/Raw/Header.txt'
    hdata = open(hfile).read()
    lines = hdata.split('\r\n')
    for line in lines:
        if('Pixel' in line): scale = float(line.split('= ')[-1])/1000.
    
    fdir = '/Users/andrewkim/Documents/AA_Discharge/TIFFS/'+code+'/Linescan/'
    fil = fdir+'Linescans_Sep16.csv'
    data = pd.read_csv(fil,sep=',')
    data = data.drop('bin',axis=1)
    
    # fdata = data
    # if code == 'ER_B1_D_WT_TIFF':
    #     data = data.drop(dropcols1,axis=1)
    #     print 'drop'
    #     # print list(data)
    # elif code == 'QU_B1_C_WT_TIFF':
    #     data = data.drop(dropcols2,axis=1)
    #     print 'drop'
        # print list(data)
    print len(list(data))
    dat = data.mean(axis=1)
    datas[code] = dict()
    
    datas[code]['r'] = arange(len(data))*scale
    datas[code]['pix'] = dat
    
        
    # labls[code] = code.split

# print list(datas[
# print list(data)

title('Quantum')
plot(datas[codes[0]]['r'],datas[codes[0]]['pix'],color='y',label=codes[0])
plot(datas[codes[1]]['r'],datas[codes[1]]['pix'],color='r',label=codes[1])
plot(datas[codes[2]]['r'],datas[codes[2]]['pix'],color='y',label=codes[2])
plot(datas[codes[3]]['r'],datas[codes[3]]['pix'],color='g',label=codes[3])
plot(datas[codes[4]]['r'],datas[codes[4]]['pix'],color='k',label=codes[4])
plot(datas[codes[5]]['r'],datas[codes[5]]['pix'],color='b',label=codes[5])

legend(loc='center left',bbox_to_anchor=(1, 0.5))
xlabel('Radial Distance (mm)')
ylabel('Average Pixel Intensity')
# ylim(30,120)
# xlim(8,3)
showme()
clf()
