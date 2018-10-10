from pithy import *
codes = [
# 'CP_B1_C_WT_TIFF',
# 'CP_B1_D_WT_TIFF',
# 'CP_C1_C_WT_TIFF',
# 'CP_C1_D_RT_TIFF',
# 'CP_D1_C_CT_TIFF',
# 'CP_D1_D_CT_TIFF',
# 'EA_B1_C_WT_TIFF',
# 'EA_B1_D_WT_TIFF',
# 'EA_C1_C_RT_TIFF',
# 'EA_C1_D_RT_TIFF',
# 'EA_C1R_C_CT_TIFF',
# 'EA_C1R_D_CT_TIFF',
# 'EN_A1_D_CT_TIFF',
# 'EN_B1_C_WT_TIFF',
# 'EN_B1_D_WT_TIFF',
# 'EN_C1_C_RT_TIFF',
# 'EN_C1_D_RT_TIFF',
'ER_B1_C_WT_TIFF',
'ER_B1_D_WT_TIFF',
'ER_A1_C_RT_TIFF',
'ER_A1_D_RT_TIFF',
# 'FU_A1_C_RT_TIFF',
# 'FU_A1_D_RT_TIFF',
# 'FU_B1_C_RT_TIFF',
# 'FU_B1_D_WT_TIFF',
# 'FU_C1_C_RT_TIFF',
# 'FU_C1_D_RT_TIFF',
# 'FU_D1_C_CT_TIFF',
# 'FU_D1_D_CT_TIFF',
# 'QU_B1_C_WT_TIFF',
# 'QU_B1_D_WT_TIFF',
# 'QU_C1_C_RT_TIFF',
# 'QU_C1_D_RT_TIFF',
# 'QU_D1_C_CT_TIFF',
# 'QU_D1_D_CT_TIFF',
]
# code = 'QU_D1_C_CT_TIFF'


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
    fil = fdir+'Linescans_Sep.csv'
    data = pd.read_csv(fil,sep=',')
    data = data.drop('bin',axis=1)
    dat = data.mean(axis=1)
    datas[code] = dict()
    
    datas[code]['r'] = arange(len(data))*scale
    datas[code]['pix'] = dat
    # labls[code] = code.split


# print datas[codes[0]]['r']

# title(code)
plot(datas[codes[0]]['r'],datas[codes[0]]['pix'],color='y',label=codes[0])
plot(datas[codes[1]]['r'],datas[codes[1]]['pix'],color='r',label=codes[1])
plot(datas[codes[2]]['r'],datas[codes[2]]['pix'],color='y',label=codes[2])
plot(datas[codes[3]]['r'],datas[codes[3]]['pix'],color='g',label=codes[3])
# plot(datas[codes[4]]['r'],datas[codes[4]]['pix'],color='y',label=codes[4])
# plot(datas[codes[5]]['r'],datas[codes[5]]['pix'],color='b',label=codes[5])

legend(loc='center left',bbox_to_anchor=(1, 0.5))
xlabel('Pixel Position (mm)')
ylabel('Pixel Intensity')
ylim(0,255)
showme()
clf()
