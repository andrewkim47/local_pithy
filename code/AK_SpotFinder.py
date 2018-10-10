#Code to extract start/middle/end of discharge/charge + rests
#Based on Neware stamping of cycles, so errors come on final and/or special middle cycles
from pithy import *
import json
import libEASI
from time import time
from datetime import datetime as dt
import libneware as lbn
import libtemperature

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

#Set default configurations to grab EASI Data
# run = '20161021_P_LCO_210_C5_1_TR_2_11_30_2_16_2.25_0'
collection = 'mac-mini-129-2'
nw = lbn.neware_data(db='echem_db')

def findSpots(run,acoo_offset = 0,coll=collection,nwlib = nw,iv=None):
    q={'run': run}
    acoo = libEASI.EASI(run=run,q=q,col=collection)
    acoot_all = acoo.times - acoo_offset
    dtus = acoo.meta['dtus']
    delay = float(run.split('_')[-4])
    #snapshotsize
    sssize = shape(acoo.out_NR)[1]
    tofs = linspace(0+delay,dtus*sssize+delay,sssize)
    
    #Collect the Neware Data
    if iv is None:
        unitchanid = acoo.meta['CyclerCode']
        print unitchanid
        ivdata = nw.get_cell(unitchanid)
    else:
        ivdata = iv
    nwt = array(ivdata['unix_time'])
    nwv = array(ivdata['test_vol'])
    nwi = array(ivdata['test_cur']) * 1000.
    
    nwcc = array(ivdata['test_capchg'])*1000.
    nwdc = array(ivdata['test_capdchg'])*1000.
    
    t00 = nwt[0]
    
    nwhrs = (nwt-t00)/3600.
    
    atimes = []
    nwtimes = []
    nwidxs = []
    ts = []
    vols = []
    curs = []
    
    #neware time, charge starts = nwt_cs
    nwt_css = []
    nwt_cms = []
    nwt_ces = []
    nwt_dss = []
    nwt_dms = []
    nwt_des = []
    nwt_crss = []
    nwt_crms = []
    nwt_cres = []
    nwt_drss = []
    nwt_drms = []
    nwt_dres = []
    
    nwtidx_css = []
    nwtidx_cms = []
    nwtidx_ces = []
    nwtidx_dss = []
    nwtidx_dms = []
    nwtidx_des = []
    nwtidx_crss = []
    nwtidx_crms = []
    nwtidx_cres = []
    nwtidx_drss = []
    nwtidx_drms = []
    nwtidx_dres = []
    
    act_css = []
    act_cms = []
    act_ces = []
    act_dss = []
    act_dms = []
    act_des = []
    act_crss = []
    act_crms = []
    act_cres = []
    act_drss = []
    act_drms = []
    act_dres = []
    
    actidx_css = []
    actidx_cms = []
    actidx_ces = []
    actidx_dss = []
    actidx_dms = []
    actidx_des = []
    actidx_crss = []
    actidx_crms = []
    actidx_cres = []
    actidx_drss = []
    actidx_drms = []
    actidx_dres = []
    
    waves_css = []
    waves_cms = []
    waves_ces = []
    waves_dss = []
    waves_dms = []
    waves_des = []
    waves_crss = []
    waves_crms = []
    waves_cres = []
    waves_drss = []
    waves_drms = []
    waves_dres = []
    
    
    checkcycs = unique(ivdata['cycle'])
    # checkcycs = unique(ivdata['cycle'])[0:12]
    for cyc in checkcycs:
        cycint = int(cyc)
    
        dat = ivdata[ivdata['cycle']==cyc]
        steps = dat['step_type']
        ssteps = steps.shift(-1)
        t = array(dat['unix_time'])
        
        ts.append((t-t[0])/3600.)
        vols.append(dat['test_vol'])
        curs.append(dat['test_cur'])
        
        ccap = dat['test_capchg']
        dcap = dat['test_capdchg']
        #find mid-capacity points
        halfccap = ccap.max()/2.0
        halfccap_idx = np.argmin(abs(ccap-halfccap))#+dat.index.tolist()[0]
        halfdcap = dcap.max()/2.0
        halfdcap_idx = np.argmin(abs(dcap-halfdcap))#+dat.index.tolist()[0]
        
        #Neware Times
        c_idxs = dat[steps==7].index.tolist() #charging
        cs_idx = c_idxs[0]
        ce_idx = c_idxs[-1]
        cm_idx = halfccap_idx
        
        # print halfdcap_idx
        # print c_idxs
        # cm_idx = int((cs_idx+ce_idx)/2)
        
        d_idxs = dat[steps==2].index.tolist() #discharging
        
        try:
            ds_idx = d_idxs[0]
            de_idx = d_idxs[-1]
            dm_idx = halfdcap_idx
            # dm_idx = int((ds_idx+de_idx)/2)
        except IndexError:
            print 'error'
            break
            # ds_idx = d_idxs[0]
            # de_idx = d_idxs[-1]
            # dm_idx = halfdcap_idx
            # dm_idx = int((ds_idx+de_idx)/2)
        
        nwt_cs = nwt[cs_idx]
        nwt_ce = nwt[ce_idx]
        nwt_cm = nwt[cm_idx]
        nwt_ds = nwt[ds_idx]
        nwt_de = nwt[de_idx]
        nwt_dm = nwt[dm_idx]
        
        # ChargeRest Start: step type flips from 7 to 4
        try:
            crs_idx = dat[steps-ssteps == 3].index.tolist()[1] #sometimes there are multiple numbers
        except IndexError:
            crs_idx = dat[steps-ssteps == 3].index.tolist()[0] 
        #ChargeRest End: step type flips from 4 to 2
        cre_idx = dat[steps-ssteps == 2].index.tolist()[0]
        crm_idx = int((crs_idx+cre_idx)/2)
        
        nwt_crs = nwt[crs_idx]
        nwt_crm = nwt[crm_idx]
        nwt_cre = nwt[cre_idx]
        
        #Find when post-discharge rest starts and ends
        #Rest Start: step type flips from 2 to 4
        try:
            drs_idx = dat[steps-ssteps == -2].index.tolist()[-1] #sometimes there are 2 numbers
        except IndexError:
            drs_idx = dre_idx
        #DisChargeRest End: last step in cycle
        dre_idx = dat.index.tolist()[-1]
        drm_idx = int((drs_idx+dre_idx)/2)
        
        nwt_drs = nwt[drs_idx]
        nwt_drm = nwt[drm_idx]
        nwt_dre = nwt[dre_idx]
        
        #find acoustic  matches
        at_cs_idx  = find_nearest(acoot_all,nwt_cs)
        at_cm_idx  = find_nearest(acoot_all,nwt_cm)
        at_ce_idx  = find_nearest(acoot_all,nwt_ce)
        at_ds_idx  = find_nearest(acoot_all,nwt_ds)
        at_dm_idx  = find_nearest(acoot_all,nwt_dm)
        at_de_idx  = find_nearest(acoot_all,nwt_de)
        at_crs_idx = find_nearest(acoot_all,nwt_crs)
        at_crm_idx = find_nearest(acoot_all,nwt_crm)
        at_cre_idx = find_nearest(acoot_all,nwt_cre)
        at_drs_idx = find_nearest(acoot_all,nwt_drs)
        at_drm_idx = find_nearest(acoot_all,nwt_drm)
        at_dre_idx = find_nearest(acoot_all,nwt_dre)
        
        at_cs  = acoot_all[at_cs_idx]
        at_cm  = acoot_all[at_cm_idx]
        at_ce  = acoot_all[at_ce_idx]
        at_ds  = acoot_all[at_ds_idx]
        at_dm  = acoot_all[at_dm_idx]
        at_de  = acoot_all[at_de_idx]
        at_crs = acoot_all[at_crs_idx]
        at_crm = acoot_all[at_crm_idx]
        at_cre = acoot_all[at_cre_idx]
        at_drs = acoot_all[at_drs_idx]
        at_drm = acoot_all[at_drm_idx]
        at_dre = acoot_all[at_dre_idx] 
        
        act_css.append(at_cs)
        act_cms.append(at_cm)
        act_ces.append(at_ce)
        act_dss.append(at_ds)
        act_dms.append(at_dm)
        act_des.append(at_de)
        act_crss.append(at_crs)
        act_crms.append(at_crm)
        act_cres.append(at_cre)
        act_drss.append(at_drs)
        act_drms.append(at_drm)
        act_dres.append(at_dre)
        
        actidx_css.append(at_cs_idx)
        actidx_cms.append(at_cm_idx)
        actidx_ces.append(at_ce_idx)
        actidx_dss.append(at_ds_idx)
        actidx_dms.append(at_dm_idx)
        actidx_des.append(at_de_idx)
        actidx_crss.append(at_crs_idx)
        actidx_crms.append(at_crm_idx)
        actidx_cres.append(at_cre_idx)
        actidx_drss.append(at_drs_idx)
        actidx_drms.append(at_drm_idx)
        actidx_dres.append(at_dre_idx)
        
        
        nwt_css.append(nwt_cs)
        nwt_cms.append(nwt_cm)
        nwt_ces.append(nwt_ce)
        nwt_dss.append(nwt_ds)
        nwt_dms.append(nwt_dm)
        nwt_des.append(nwt_de)
        
        nwtidx_css.append(cs_idx)
        nwtidx_cms.append(cm_idx)
        nwtidx_ces.append(ce_idx)
        nwtidx_dss.append(ds_idx)
        nwtidx_dms.append(dm_idx)
        nwtidx_des.append(de_idx)
        
        nwt_crss.append(nwt_crs)
        nwt_crms.append(nwt_crm)
        nwt_cres.append(nwt_cre)
        nwt_drss.append(nwt_drs)
        nwt_drms.append(nwt_drm)
        nwt_dres.append(nwt_dre)
        
        nwtidx_crss.append(crs_idx)
        nwtidx_crms.append(crm_idx)
        nwtidx_cres.append(cre_idx)
        nwtidx_drss.append(drs_idx)
        nwtidx_drms.append(drm_idx)
        nwtidx_dres.append(dre_idx)
        
        
    maxterror = 90.
    blank = np.zeros(495)+128
    blank = list(blank)
    numSpots = len(nwt_css)
   
    for j in range(numSpots):
        css_error = abs(act_css[j] -nwt_css[j])
        cms_error = abs(act_cms[j] -nwt_cms[j])
        ces_error = abs(act_ces[j] -nwt_ces[j])
        dss_error = abs(act_dss[j] -nwt_dss[j])
        dms_error = abs(act_dms[j] -nwt_dms[j])
        des_error = abs(act_des[j] -nwt_des[j])
        drss_error = abs(act_drss[j] -nwt_drss[j])
        drms_error = abs(act_drms[j] -nwt_drms[j])
        dres_error = abs(act_dres[j] -nwt_dres[j])
        crss_error = abs(act_crss[j] -nwt_crss[j])
        crms_error = abs(act_crms[j] -nwt_crms[j])
        cres_error = abs(act_cres[j] -nwt_cres[j])
        
        if(css_error > maxterror):
            waves_css.append(blanks)
            print 'css Neware-Acoustic time gap=',str(css_error)
        else:
            wave_to_add = list(acoo.out_NR[actidx_css[j]])
            waves_css.append(wave_to_add)
     
        if(cms_error > maxterror):
            waves_cms.append(blanks)
            print 'cms Neware-Acoustic time gap=',str(cms_error)
        else:
            wave_to_add = list(acoo.out_NR[actidx_cms[j]])
            waves_cms.append(wave_to_add)
            
        if(ces_error > maxterror):
            waves_ces.append(blanks)
            print 'ces Neware-Acoustic time gap=',str(ces_error)
        else:
            wave_to_add = list(acoo.out_NR[actidx_ces[j]])
            waves_ces.append(wave_to_add)
            
        if(dss_error > maxterror):
            waves_dss.append(blanks)
            print 'dss Neware-Acoustic time gap=',str(dss_error)
        else:
            wave_to_add = list(acoo.out_NR[actidx_dss[j]])
            waves_dss.append(wave_to_add)
     
        if(dms_error > maxterror):
            waves_dms.append(blanks)
            print 'dms Neware-Acoustic time gap=',str(dms_error)
        else:
            wave_to_add = list(acoo.out_NR[actidx_dms[j]])
            waves_dms.append(wave_to_add)
            
        if(des_error > maxterror):
            waves_des.append(blanks)
            print 'des Neware-Acoustic time gap=',str(des_error)
        else:
            wave_to_add = list(acoo.out_NR[actidx_des[j]])
            waves_des.append(wave_to_add)
            
        if(drss_error > maxterror):
            waves_drss.append(blanks)
            print 'drss Neware-Acoustic time gap=',str(drss_error)
        else:
            wave_to_add = list(acoo.out_NR[actidx_drss[j]])
            waves_drss.append(wave_to_add)
     
        if(drms_error > maxterror):
            waves_drms.append(blanks)
            print 'drms Neware-Acoustic time gap=',str(drms_error)
        else:
            wave_to_add = list(acoo.out_NR[actidx_drms[j]])
            waves_drms.append(wave_to_add)
            
        if(dres_error > maxterror):
            waves_dres.append(blanks)
            print 'dres Neware-Acoustic time gap=',str(dres_error)
        else:
            wave_to_add = list(acoo.out_NR[actidx_dres[j]])
            waves_dres.append(wave_to_add)
            
        if(crss_error > maxterror):
            waves_crss.append(blanks)
            print 'crss Neware-Acoustic time gap=',str(crss_error)
        else:
            wave_to_add = list(acoo.out_NR[actidx_crss[j]])
            waves_crss.append(wave_to_add)
     
        if(crms_error > maxterror):
            waves_crms.append(blanks)
            print 'crms Neware-Acoustic time gap=',str(crms_error)
        else:
            wave_to_add = list(acoo.out_NR[actidx_crms[j]])
            waves_crms.append(wave_to_add)
            
        if(cres_error > maxterror):
            waves_cres.append(blanks)
            print 'cres Neware-Acoustic time gap=',str(cres_error)
        else:
            wave_to_add = list(acoo.out_NR[actidx_cres[j]])
            waves_cres.append(wave_to_add)
        
    spots = dict()
    spots['cs'] = {'terror':list(array(nwt_css)-array(act_css)),'acts':act_css,'waves':waves_css}
    spots['ce'] = {'terror':list(array(nwt_ces)-array(act_ces)),'acts':act_ces,'waves':waves_ces}
    spots['cm'] = {'terror':list(array(nwt_cms)-array(act_cms)),'acts':act_cms,'waves':waves_cms}
    spots['ds'] = {'terror':list(array(nwt_dss)-array(act_dss)),'acts':act_dss,'waves':waves_dss}
    spots['dm'] = {'terror':list(array(nwt_dms)-array(act_dms)),'acts':act_dms,'waves':waves_dms}
    spots['de'] = {'terror':list(array(nwt_des)-array(act_des)),'acts':act_des,'waves':waves_des}
    spots['crs'] = {'terror':list(array(nwt_crss)-array(act_crss)),'acts':act_crss,'waves':waves_crss}
    spots['cre'] = {'terror':list(array(nwt_cres)-array(act_cres)),'acts':act_cres,'waves':waves_cres}
    spots['crm'] = {'terror':list(array(nwt_crms)-array(act_crms)),'acts':act_crms,'waves':waves_crms}
    spots['drs'] = {'terror':list(array(nwt_drss)-array(act_drss)),'acts':act_drss,'waves':waves_drss}
    spots['drm'] = {'terror':list(array(nwt_drms)-array(act_drms)),'acts':act_drms,'waves':waves_drms}
    spots['dre'] = {'terror':list(array(nwt_dres)-array(act_dres)),'acts':act_dres,'waves':waves_dres}
    spots['numSpots'] = numSpots
    return spots
    
def dumpSpots(spots,filenm):
    with open(filenm, 'w') as outfile:
        json.dump(spots, outfile)
# def smePlot():
#     textx = 10 + delay
#     texty = 255 * .95
#     if lowGain: textx = 3.5 + delay
#     matplotlib.rcParams.update({'font.size': 14})
    
    
#     fig = figure(0)
#     fig.set_figheight(6*(numcyc+4))
#     fig.set_figwidth(40)
#     suptitle(run,x=0.5,y=1.01,fontsize=24)
    
#     for i in range(numcyc):
#         # print i
#         subplot(numcyc+5,4,4*i+1)
#         title('Charge Cycle: '+str(i))
#         plot(tofs,wave_charge_starts[i],'b',label='Start')
#         plot(tofs,wave_charge_middles[i],'g',label='Middle')
#         plot(tofs,wave_charge_ends[i],'r',label='End')
#         # text(textx,texty,'Cycle: '+str(i))
#         xlabel('ToF (uS)')
#         # ylabel('Charge')
#         legend()
#         if lowGain: xlim(xlow,xhigh)
#         ylim(0,255)
#         # xlim(1,7)
#         minorticks_on()
#         grid(b=True, which='major')
#         grid(b=True, which='minor')
        
        
#         subplot(numcyc+5,4,4*i+2)
#         title('Charge Rest Cycle: '+str(i))
#         plot(tofs,wave_chargerest_starts[i],'r',label='Start')
#         plot(tofs,wave_chargerest_middles[i],'g',label='Middle')
#         plot(tofs,wave_chargerest_ends[i],'b',label='End')
#         # text(textx,texty,'Cycle: '+str(i))
#         xlabel('ToF (uS)')
#         # ylabel('Discharge')
#         legend()
#         if lowGain: xlim(xlow,xhigh)
#         ylim(0,255)
#         # xlim(1,7)
#         minorticks_on()
#         grid(b=True, which='major')
#         grid(b=True, which='minor')
        
#         subplot(numcyc+5,4,4*i+3)
#         title('Discharge Cycle: '+str(i))
#         plot(tofs,wave_discharge_starts[i],'b',label='Start')
#         plot(tofs,wave_discharge_middles[i],'g',label='Middle')
#         plot(tofs,wave_discharge_ends[i],'r',label='End')
#         # text(textx,texty,'Cycle: '+str(i))
#         xlabel('ToF (uS)')
#         # ylabel('Discharge')
#         legend()
#         if lowGain: xlim(xlow,xhigh)
#         ylim(0,255)
#         # xlim(1,7)
#         minorticks_on()
#         grid(b=True, which='major')
#         grid(b=True, which='minor')
        
#         subplot(numcyc+5,4,4*i+4)
#         title('Discharge Rest Cycle: '+str(i))
#         plot(tofs,wave_dischargerest_starts[i],'r',label='Start')
#         plot(tofs,wave_dischargerest_middles[i],'g',label='Middle')
#         plot(tofs,wave_dischargerest_ends[i],'b',label='End')
#         # text(textx,texty,'Cycle: '+str(i))
#         xlabel('ToF (uS)')
#         # ylabel('Discharge')
#         legend()
#         if lowGain: xlim(xlow,xhigh)
#         ylim(0,255)
#         # xlim(1,7)
#         minorticks_on()
#         grid(b=True, which='major')
#         grid(b=True, which='minor')    
        
#     #TofMap
#     subplot(numcyc+5,1,numcyc+1)
#     acoo.time_correct(thresh=300,tstart=nwt[0]+acoo_offset,tend=nwt[-1]+acoo_offset)
#     acoo.tof_map(ccm=cm.bwr,interp='none')
#     for entry in normT(nwt_charge_starts):
#         axvline(x=entry,c='k')
#     for entry in normT(nwt_discharge_starts):
#         axvline(x=entry,c='k')
#     for entry in normT(nwt_charge_ends):
#         axvline(x=entry,c='g',ls='--')
#     for entry in normT(nwt_discharge_ends):
#         axvline(x=entry,c='g',ls='--')
#     # for entry in normT(act_charge_starts):
#     #     axvline(x=entry,c='k',ls='--')
#     # for entry in normT(act_charge_middles):
#     #     axvline(x=entry,c='k',ls='--')
#     # for entry in normT(act_charge_ends):
#     #     axvline(x=entry,c='k',ls='--')
#     # for entry in normT(act_chargerest_starts):
#     #     axvline(x=entry,c='k',ls='--')
#     # for entry in normT(act_chargerest_middles):
#     #     axvline(x=entry,c='k',ls='--')
#     # for entry in normT(act_chargerest_ends):
#     #     axvline(x=entry,c='k',ls='--')
#     # for entry in normT(act_discharge_starts):
#     #     axvline(x=entry,c='k',ls='--')
#     # for entry in normT(act_discharge_middles):
#     #     axvline(x=entry,c='k',ls='--')
#     # for entry in normT(act_discharge_ends):
#     #     axvline(x=entry,c='k',ls='--')
#     # for entry in normT(act_dischargerest_starts):
#     #     axvline(x=entry,c='k',ls='--')
#     # for entry in normT(act_dischargerest_middles):
#     #     axvline(x=entry,c='k',ls='--')
#     # for entry in normT(act_dischargerest_ends):
#     #     axvline(x=entry,c='k',ls='--')
    
#     ylabel('ToF (uS)')
#     xlabel('Cycle Time (hr)' )
#     minorticks_on()
#     grid(b=True, which='major')
#     grid(b=True, which='minor')
    
#     subplot(numcyc+5,1,numcyc+2)
#     ta = normT(acoo.ntimes-acoo_offset)
#     plot(ta,acoo.ntots,'k')
#     for entry in normT(nwt_charge_starts):
#         axvline(x=entry,c='k')
#     for entry in normT(nwt_charge_ends):
#         axvline(x=entry,c='k',ls='--')
#     for entry in normT(nwt_discharge_starts):
#         axvline(x=entry,c='g')
#     for entry in normT(nwt_discharge_ends):
#         axvline(x=entry,c='g',ls='--')
#     xlim(nwhrs[0],nwhrs[-1])

#     # Current
#     subplot(numcyc+5,1,numcyc+3)
#     plot(nwhrs,nwi,'k')
#     title('Current Match')
#     xlabel('Cycle Time (Hrs)')
#     ylabel('Current (mA)')
#     for entry in normT(nwt_charge_starts):
#         axvline(x=entry,c='k')
#     for entry in normT(nwt_discharge_starts):
#         axvline(x=entry,c='k')
#     for entry in normT(nwt_charge_ends):
#         axvline(x=entry,c='g',ls='--')
#     for entry in normT(nwt_discharge_ends):
#         axvline(x=entry,c='g',ls='--')
#     # # Charge
#     plot(normT(nwt_charge_starts),nwi[nwtidx_charge_starts],'b^')
#     plot(normT(nwt_charge_middles),nwi[nwtidx_charge_middles],'g^')
#     plot(normT(nwt_charge_ends),nwi[nwtidx_charge_ends],'r^')
#     plot(normT(act_charge_starts),imaxs,'bx')
#     plot(normT(act_charge_middles),imaxs,'gx')
#     plot(normT(act_charge_ends),imaxs,'rx')
    
#     plot(normT(nwt_chargerest_starts),nwi[nwtidx_chargerest_starts],'r*')
#     plot(normT(nwt_chargerest_middles),nwi[nwtidx_chargerest_middles],'g*')
#     plot(normT(nwt_chargerest_ends),nwi[nwtidx_chargerest_ends],'b*')
#     plot(normT(act_chargerest_starts),izeros,'ro')
#     plot(normT(act_chargerest_middles),izeros,'go')
#     plot(normT(act_chargerest_ends),izeros,'bo')
#     # # Discharge
#     plot(normT(nwt_discharge_starts),nwi[nwtidx_discharge_starts],'bv')
#     plot(normT(nwt_discharge_middles),nwi[nwtidx_discharge_middles],'gv')
#     plot(normT(nwt_discharge_ends),nwi[nwtidx_discharge_ends],'rv')
#     plot(normT(act_discharge_starts),imins,'bx')
#     plot(normT(act_discharge_middles),imins,'gx')
#     plot(normT(act_discharge_ends),imins,'rx')
    
#     plot(normT(nwt_dischargerest_starts),nwi[nwtidx_dischargerest_starts],'rd')
#     plot(normT(nwt_dischargerest_middles),nwi[nwtidx_dischargerest_middles],'gd')
#     plot(normT(nwt_dischargerest_ends),nwi[nwtidx_dischargerest_ends],'bd')
#     plot(normT(act_dischargerest_starts),izeros,'ro')
#     plot(normT(act_dischargerest_middles),izeros,'go')
#     plot(normT(act_dischargerest_ends),izeros,'bo')
#     xlim(nwhrs[0],nwhrs[-1])
#     minorticks_on()
#     grid(b=True, which='major')
#     grid(b=True, which='minor')
    
    
#     subplot(numcyc+5,1,numcyc+4)
#     plot(nwhrs,nwv,'k')
#     title('Potential')
#     xlabel('Cycle Time (Hrs)')
#     ylabel('Voltage (V))')
#     xlim(nwhrs[0],nwhrs[-1])
#     minorticks_on()
#     grid(b=True, which='major')
#     grid(b=True, which='minor')
#     for entry in normT(nwt_charge_starts):
#         axvline(x=entry,c='k')
#     for entry in normT(nwt_discharge_starts):
#         axvline(x=entry,c='k')
#     for entry in normT(nwt_charge_ends):
#         axvline(x=entry,c='g',ls='--')
#     for entry in normT(nwt_discharge_ends):
#         axvline(x=entry,c='g',ls='--')
    
#     subplot(numcyc+5,1,numcyc+5)
#     plot(nwhrs,nwcc,'r',label='Charge')
#     plot(nwhrs,nwdc,'b',label='Discharge')
#     legend()
#     title('Capacity')
#     xlabel('Cycle Time (Hrs)')
#     ylabel('Charge (mAhr)')
#     xlim(nwhrs[0],nwhrs[-1])
#     minorticks_on()
#     grid(b=True, which='major')
#     grid(b=True, which='minor')
#     tight_layout()
#     if shouldSave: savefig(filedir+run+'_v5sme.png',bbox_inches="tight")
#     if shouldShow: showme()
#     clf()
    

# # spots = findSpots(run) 

# # for i in range(len(spots['cs']['acts'])):
# #     plot(spots['cs']['waves'][i]+i*150)
# # showme()
# # clf()