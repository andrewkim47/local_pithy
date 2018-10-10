import os


fdir = '/Users/andrewkim/Documents/AA_Discharge/TIFFS/'

fldrs = [
    # 'CopperTop_B1_Charged_TIFF',   
    # 'CopperTop_B1_Discharged_Warm50Explode_TIFF',  
    # 'CopperTop_C1_Charged_TIFF',   
    # 'CopperTop_C1_Discharged_RoomTemp_TIFF',   
    # 'CopperTop_D1_Charged_TIFF',   
    # 'CopperTop_D1_Discharged_ColdTemp_TIFF',   
    # 'Quantum_B1_Charged_TIFF',
    # 'Quantum_C1_Charged_TIFF',
    # 'Quantum_D1_Charged_TIFF',
    # 'Quantum_C1_Discharged_RoomTemp_Again_TIFF',
    # 'Quantum_B1_Discharged_Warm50_TIFF',
    # 'Quantum_D1_Discharged_ColdTemp_TIFF',
    # 'Energizer_B1_Charged_TIFF',
    # 'Energizer_C1_Charged_TIFF',
    # 'Energizer_C1_Discharged_RoomTemp_TIFF',
    # 'Energizer_B1_Discharged_Warm50_TIFF',
    # 'Energizer_A1_Discharged_ColdTemp_TIFF',
    # 'Fujitsu_D1_Discharged_ColdTemp_TIFF',
    # 'Fujitsu_C1_Discharged_RoomTemp_TIFF',
    # 'Fujitsu_B1_Discharged_Warm50Explode_TIFF',
    # 'Fujitsu_A1_Discharged_RoomTemp_TIFF',
    # 'Fujitsu_A1_Charged_TIFF',
    # 'Fujitsu_B1_Charged_TIFF',
    # 'Fujitsu_C1_Charged_TIFF',
    # 'Fujitsu_D1_Charged_TIFF',
    # 'EverReady_A1_Charged_TIFF',
    # 'EverReady_B1_Charged_TIFF',
    # 'EverReady_A1_Discharged_RoomTemp_TIFF',
    # 'EverReady_B1_Discharged_Warm50_TIFF',
    '20170602_EcoAdvanced_B1_Charged_TIFF',
    '20170602_EcoAdvanced_C1_Charged_TIFF',
    '20170613_EcoAdvanced_C1R_Charged_TIFF',
    '20180116_Ecoadvanced_C1_Discharged_RoomTemp_TIFF',
    '20180119_EcoAdvanced_B1_Discharged_Warm50_TIFF',
    '20180410_EcoAdvanced_C1R_Disch_ColdTemp_TIFF',    
]


tokeep = ['0608.tiff', '0409.tiff', '0604.tiff', '0405.tiff', '0501.tiff', '0500.tiff', '0404.tiff', '.DS_Store', '0605.tiff', '0408.tiff', '0609.tiff', '0602.tiff', '0403.tiff', '0507.tiff', '0506.tiff', '0510.tiff', '0402.tiff', '0603.tiff', '0505.tiff', '0401.tiff', '0600.tiff', '0509.tiff', '0508.tiff', '0601.tiff', '0400.tiff', '0504.tiff', '0503.tiff', '0407.tiff', '0610.tiff', 'Header.txt', '0606.tiff', '0607.tiff', '0406.tiff', '0502.tiff', '0410.tiff']

for fldr in fldrs:
    folder = fdir + fldr + '/'
    for fil in os.listdir(folder):
        if not(fil in tokeep):
            os.remove(folder+fil)

# Strip date
for fldr in fldrs:
    os.rename(fdir+fldr,fdir+fldr[9:])
