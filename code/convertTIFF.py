import os
from glob import glob

fdir = '/Users/andrewkim/Documents/AA_Discharge/TIFFS/'

fldrs = [
    'CopperTop_B1_Charged_TIFF',
    'CopperTop_B1_Discharged_Warm50Explode_TIFF',
    'CopperTop_C1_Charged_TIFF',
    'CopperTop_C1_Discharged_RoomTemp_TIFF',
    'CopperTop_D1_Charged_TIFF',
    'CopperTop_D1_Discharged_ColdTemp_TIFF',
    'EcoAdvanced_B1_Charged_TIFF',
    'EcoAdvanced_B1_Discharged_Warm50_TIFF',
    'EcoAdvanced_C1_Charged_TIFF',
    'Ecoadvanced_C1_Discharged_RoomTemp_TIFF',
    'EcoAdvanced_C1R_Charged_TIFF',
    'EcoAdvanced_C1R_Disch_ColdTemp_TIFF',
    'Energizer_A1_Discharged_ColdTemp_TIFF',
    'Energizer_B1_Charged_TIFF',
    'Energizer_B1_Discharged_Warm50_TIFF',
    'Energizer_C1_Charged_TIFF',
    'Energizer_C1_Discharged_RoomTemp_TIFF',
    'EverReady_A1_Charged_TIFF',
    'EverReady_A1_Discharged_RoomTemp_TIFF',
    'EverReady_B1_Charged_TIFF',
    'EverReady_B1_Discharged_Warm50_TIFF',
    'Fujitsu_A1_Charged_TIFF',
    'Fujitsu_A1_Discharged_RoomTemp_TIFF',
    'Fujitsu_B1_Charged_TIFF',
    'Fujitsu_B1_Discharged_Warm50Explode_TIFF',
    'Fujitsu_C1_Charged_TIFF',
    'Fujitsu_C1_Discharged_RoomTemp_TIFF',
    'Fujitsu_D1_Charged_TIFF',
    'Fujitsu_D1_Discharged_ColdTemp_TIFF',
    'Quantum_B1_Charged_TIFF',
    'Quantum_B1_Discharged_Warm50_TIFF',
    'Quantum_C1_Charged_TIFF',
    'Quantum_C1_Discharged_RoomTemp_Again_TIFF',
    'Quantum_D1_Charged_TIFF',
    'Quantum_D1_Discharged_ColdTemp_TIFF',
]

for fldr in fldrs:
    folder = fdir+fldr+'/'
    
    codename = folder.split('/')[-2]
    fils = sorted(glob(folder+'*.tiff'))
    
    
    for fil in fils:
        oldname = fil
        suffix = oldname.split('/')[-1]
        newname = folder+codename+'_'+suffix
        # print newname
        os.rename(oldname,newname)
        