from pithy import *
import libEASI
import libneware as lbn
import libtemperature
# import pandas as pd
from AK_SpotFinder import findSpots,dumpSpots
from scipy.interpolate import interp1d
from common_functions import cross_correlate

# http://stackoverflow.com/questions/8914491/finding-the-nearest-value-and-return-the-index-of-array-in-python
def find_nearest(A, target):
    #A must be sorted
    idx = A.searchsorted(target)
    idx = np.clip(idx, 1, len(A)-1)
    left = A[idx-1]
    right = A[idx]
    idx -= target - left < right - target
    return idx

#subtract t0, make hours    
def normT(T):
    return (T-t00)/3600.

#Collect the Acoustic 
collection = 'mac-mini-129-2'
nw = lbn.neware_data(db='echem_db')

# collection = 'brix-129-4'
# nw = lbn.neware_data(db='echem_2_db')

#-----------------------------------------------------------------
#------------------     Parameters      --------------------------
# -----------------------------------------------------------------
xlow=3
xhigh=10
ylow = -.5
yhigh = 2

limy = True
# limy = False

# shouldShow = True
# shouldShow = False

# shouldSave = True
# shouldSave = False

# offset = 0. #0 if before daylightsavings
offset = 3600. #3600 if after daylightsavings

# runs = [    
# 'P_LCO_210_20160826_TR_0_0_40_2_16_2.25_0',
# 'P_LCO_210_20160926_TR_1_11_40_2_16_2.25_0',
# 'P_LCO_210_20160825_TR_0_0_40_2_16_2.25_0',
# 'P_LCO_210_20160826_TR_0_0_40_2_16_2.25_0',
# 'P_LCO_210_20160830_TR_0_0_40_2_16_2.25_0',
# 'P_LCO_210_20160902_TR_0_0_40_2_16_2.25_0',
# 'P_LCO_210_20160922_TR_1_10_40_2_16_2.25_0',
# 'P_LCO_210_20160923_TR_1_11_40_2_16_2.25_0',
# 'P_LCO_210_20160926_TR_1_11_40_2_16_2.25_0',
# 'P_LCO_210_20160929_TR_0_0_40_2_16_2.25_0'
# ]

# runs =[
# '20161008_P_210_LCO_2C_1_TR_2_11_30_2_16_2.25_0',
# '20161012_P_LCO_210_1C_1_TR_2_11_30_2_16_2.25_0',
# '20161019_P_LCO_210_2C_1_TR_2_11_30_2_16_2.25_0',
# '20161020_P_LCO_210_2C_1_TR_2_11_30_2_16_2.25_0',
# '20161021_P_LCO_210_C5_1_TR_2_11_30_2_16_2.25_0',
# '20161024_P_LCO_210_2C_1_TR_8_5_30_2_16_2.25_0',
# '20161024_P_LCO_210_2C_2_TR_11_2_30_2_16_2.25_0',
# '20161027_P_LCO_210_1C_2_TR_8_6_30_2_16_2.25_0',
# '20161031_P_LCO_210_1C_1_TR_11_2_25_2_16_2.25_0', 
# ]

# runs=[
# # '20161126_P_LCO_210_C5_2_TR_9_6_27_2_20_2.25_0',
# '20161203_P_LCO_210_1C_1_TR_1_10_30_2_20_2.25_0',
# '20161203_P_LCO_210_1C_2_TR_2_11_25_2_20_2.25_0',
# '20161203_P_LCO_210_C2_1_TR_3_12_22_2_20_2.25_0',
# '20161203_P_LCO_210_C2_2_TR_6_9_25_2_20_2.25_0'
# ]

runs = ['20161203_P_LCO_210_1C_1_TR_1_10_30_2_20_2.25_0']
filedir = drop_pre
#-----------------------------------------------------------------
#-----------------------------------------------------------------
#-----------------------------------------------------------------
for run in runs:
    acoo = libEASI.EASI(run=run,col=collection)
    
    dtus = acoo.meta['dtus']
    delay = float(run.split('_')[-4])
    #snapshotsize
    sssize = shape(acoo.out_NR)[1]
    tofs = linspace(0+delay,dtus*sssize+delay,sssize)
    
    #Collect the Neware Data
    unitchanid = acoo.meta['CyclerCode']
    print unitchanid
    ivdata = nw.get_cell(unitchanid)
    nwt = array(ivdata['unix_time'])
    nwv = array(ivdata['test_vol'])
    nwi = array(ivdata['test_cur']) * 1000.
    nwcc = array(ivdata['test_capchg'])*1000.
    nwdc = array(ivdata['test_capdchg'])*1000.
    t00 = nwt[0]
    nwhrs = (nwt-t00)/3600.
    
    #Grab Spots
    spots = findSpots(run,acoo_offset = offset ,iv = ivdata)
    
    dumpSpots(spots,filedir+run+'.json')
    # numSpots = spots['numSpots']
    # cmap = get_cmap('cool')
    # colors = [cmap(i) for i in linspace(.3,.8, numSpots-2)]
    # colors.insert(0,'K')
    # colors.append('red')
    
    # int_pts = 4
    # total_pts = int_pts*495
    # t = linspace(0+delay,dtus*sssize+delay,total_pts)
    
    # ikind='cubic'
    
    # #categories
    # cats = ['crs','crm','cre','drs','drm','dre','cs','cm','ce','ds','dm','de']
    # # cats = ['cs','crs','ds','drs']
    # # cats = ['cs','cm','ce']

    # # for key in spots.keys():
    #     # print key
    
    # for cat in cats:
    #     #take 2nd cycle as signal to compare to
    #     ref = spots[cat]['waves'][10]-128
    #     ref_f = interp1d(tofs,ref,kind=ikind)
    #     iref = ref_f(t)
    #     spots[cat]['iwaves'] = []
    #     spots[cat]['tshift'] = []
    #     spots[cat]['func'] = []
    #     for i in range(numSpots):
    #         func = interp1d(tofs,spots[cat]['waves'][i]-128,kind=ikind)
    #         iwave = func(t)
    #         tshift = cross_correlate(iwave,iref,t,'us')
    #         if abs(tshift) > 5: tshift = 0
    #         spots[cat]['iwaves'].append(iwave)
    #         spots[cat]['tshift'].append(tshift)
    #         spots[cat]['func'].append(func)
    

# # #######------------------------------------------------------------
# # #######    #Plot TOF-shift within Cycle
# # ####### subtract SME, without adjusting TOF
# # #######------------------------------------------------------------
    
#     fig = figure(0)
#     fig.set_figheight(numSpots*5)
#     fig.set_figwidth(8)    
#     for i in range(numSpots):
#         subplot(numSpots,1,i+1)
#         title('Charge Cycle:'+str(i))
#         plot(t,array(spots['cs']['iwaves'][i])-array(spots['ce']['iwaves'][i]),label='Start-End')
#         plot(t,array(spots['cs']['iwaves'][i])-array(spots['cm']['iwaves'][i]),label='Start-Middle')
#         plot(t,array(spots['cm']['iwaves'][i])-array(spots['ce']['iwaves'][i]),label='Middle-End')
#         xlabel('Time (uS)')
#         ylabel('Amplitude')
#         legend(loc='best')
#         xlim(3,10)
#         ylim(-150,150)
#     suptitle(run)
#     tight_layout()
#     if shouldShow: showme()
#     if shouldSave: savefig(filedir+run+'_c.png')
#     clf()

#     for i in range(numSpots):
#         subplot(numSpots,1,i+1)
#         title('Discharge Cycle:'+str(i))
#         plot(t,array(spots['ds']['iwaves'][i])-array(spots['de']['iwaves'][i]),label='Start-End')
#         plot(t,array(spots['ds']['iwaves'][i])-array(spots['dm']['iwaves'][i]),label='Start-Middle')
#         plot(t,array(spots['dm']['iwaves'][i])-array(spots['de']['iwaves'][i]),label='Middle-End')
#         xlabel('Time (uS)')
#         ylabel('Amplitude')
#         legend(loc='best')
#         xlim(3,10)
#         ylim(-150,150)
#     tight_layout()
#     if shouldShow: showme()
#     if shouldSave: savefig(filedir+run+'_d.png')
#     clf()
    
#     for i in range(numSpots):
#         subplot(numSpots,1,i+1)
#         title('Charge Rest Cycle:'+str(i))
#         plot(t,array(spots['crs']['iwaves'][i])-array(spots['cre']['iwaves'][i]),label='Start-End')
#         plot(t,array(spots['crs']['iwaves'][i])-array(spots['crm']['iwaves'][i]),label='Start-Middle')
#         plot(t,array(spots['crm']['iwaves'][i])-array(spots['cre']['iwaves'][i]),label='Middle-End')
#         xlabel('Time (uS)')
#         ylabel('Amplitude')
#         legend(loc='best')
#         xlim(3,10)
#         ylim(-150,150)
#     tight_layout()
#     if shouldShow: showme()
#     if shouldSave: savefig(filedir+run+'_cr.png')
#     clf()
    
#     for i in range(numSpots):
#         subplot(numSpots,1,i+1)
#         title('Discharge Rest Cycle:'+str(i))
#         plot(t,array(spots['drs']['iwaves'][i])-array(spots['dre']['iwaves'][i]),label='Start-End')
#         plot(t,array(spots['drs']['iwaves'][i])-array(spots['drm']['iwaves'][i]),label='Start-Middle')
#         plot(t,array(spots['drm']['iwaves'][i])-array(spots['dre']['iwaves'][i]),label='Middle-End')
#         xlabel('Time (uS)')
#         ylabel('Amplitude')
#         legend(loc='best')
#         xlim(3,10)
#         ylim(-150,150)
#     tight_layout()
#     if shouldShow: showme()
#     if shouldSave: savefig(filedir+run+'_dr.png')
#     clf()
    
######------------------------------------------------------------
######    #Smear Plot
######------------------------------------------------------------    
    # figure(2)
    # subplot(2,1,1)
    # acoo.time_correct(tstart=nwt[0]+offset,tend=nwt[-1]+offset)
    # acoo.tof_map(ccm=cm.bwr)
    # subplot(2,1,2)
    # ta = normT(acoo.ntimes-offset)
    # plot(ta,acoo.ntots,'k')
    # for entry in spots['crs']['acts']:
    #     axvline(x=normT(entry))
    # for entry in spots['drs']['acts']:
    #     axvline(x=normT(entry))
    # showme()
    # clf()
######------------------------------------------------------------
######    #Plot TOF-shift vs Cycle
######------------------------------------------------------------
    
    # fig = figure(0)
    # fig.set_figheight(16)
    # fig.set_figwidth(8)  
    # subplot(4,1,1)
    # suptitle(run)
    # plot(spots['cs']['tshift'],'bo-',label='Charge')
    # plot(spots['ds']['tshift'],'go-',label='Discharge')
    # title('Dis/Charge Starts')
    # ylabel('tshift (uS)')
    # xlabel('Cycle')
    # legend(loc='best')
    # subplot(4,1,2)
    # plot(spots['ce']['tshift'],'bo-',label='Charge')
    # plot(spots['de']['tshift'],'go-',label='Discharge')
    # title('Dis/Charge Ends')
    # ylabel('tshift (uS)')
    # xlabel('Cycle')
    # legend(loc='best')
    # subplot(4,1,3)
    # plot(spots['crs']['tshift'],'bo-',label='Charge')
    # plot(spots['drs']['tshift'],'go-',label='Discharge')
    # title('Dis/Charge Rest Starts')
    # ylabel('tshift (uS)')
    # xlabel('Cycle')
    # legend(loc='best')
    # subplot(4,1,4)
    # plot(spots['cre']['tshift'],'bo-',label='Charge')
    # plot(spots['dre']['tshift'],'go-',label='Discharge')
    # title('Dis/Charge Rest Ends')
    # ylabel('tshift (uS)')
    # xlabel('Cycle')
    # legend(loc='best')
    # tight_layout()
    # if shouldSave: savefig(filedir+run+'.png')
    # if shouldShow: showme()
    # clf()

    
    # fig = figure(0)
    # fig.set_figheight(20)
    # fig.set_figwidth(20)
    # for i in range(numSpots):
    #     subplot(4,1,1)
    #     plot(tofs,spots['cs']['waves'][i]-128,c=colors[i])
    #     plot(t,spots['cs']['iwaves'][i],c=colors[i])
    #     subplot(4,1,2)
    #     plot(tofs,spots['crs']['waves'][i]-128,c=colors[i])
    #     plot(t,spots['crs']['iwaves'][i],c=colors[i])
    #     subplot(4,1,3)
    #     plot(tofs,spots['ds']['waves'][i]-128,c=colors[i])
    #     plot(t,spots['ds']['iwaves'][i],c=colors[i])
    #     subplot(4,1,4)
    #     plot(tofs,spots['drs']['waves'][i]-128,c=colors[i])
    #     plot(t,spots['drs']['iwaves'][i],c=colors[i])
    # showme()
    # clf()
    

    