##Author: 
##Date Started: 
##Notes: 

#sudo pip install pymodbus

from pymodbus.client.sync import  ModbusSerialClient
from time import sleep

#Modbus registers
#Variable : Modbus Address

def makebin(val,digits=8):
    # charstr = '#0'+ str(digits) +'b'
    # charstr = '#008b'
    # return format(val, charstr)
    v=bin(val)
    return v[2:].zfill(digits)

def readReg(client,addr):
    return client.read_holding_registers(addr,unit = 1).registers[0]

def getBatVol(client):
    addr = 0x0008
    Vbit = readReg(client,addr)
    volts = Vbit * 100. / 2.0 ** 15. #see datasheet
    return volts

def getPanVol(client):
    addr = 0x0009
    Vbit = readReg(client,addr)
    volts = Vbit * 100. / 2.0 ** 15. #see datasheet
    return volts

def getLodVol(client):
    addr = 0x000A
    Vbit = readReg(client,addr)
    volts = Vbit * 100. / 2.0 ** 15. #see datasheet
    return volts

def getChgCur(client): #Amps
    addr = 0x000B
    Cbit = readReg(client,addr)
    Cur = Cbit * 79.16 / 2.0 ** 15. #see datasheet
    return Cur

def getLodCur(client): #Amps
    addr = 0x000C
    Cbit = readReg(client,addr)
    Cur = Cbit * 79.16 / 2.0 ** 15. #see datasheet
    return Cur

def getRemTmp(client): #C
    addr = 0x0010
    Cbit = readReg(client,addr)
    return Cbit

def getMorTmp(client): #C
    addr = 0x0010
    Cbit = readReg(client,addr)
    return Cbit
    
def getLodSte(client): 
    addr = 0x001A
    Cbit = readReg(client,addr)
    states = ['START','LOAD_ON','LVD_WARNING','LVD','FAULT','DISCONNECT']
    return states[Cbit]
    
def getLodFlt(client):
    addr = 0x001B
    Cbit = readReg(client,addr)
    faults = ['external short circuit','overcurrent','FETs shorted','software bug','HVD','heatsink over-temperature','EEPROM setting edit(reset required)','Fault 8']
    return faults[Cbit]

#Charge output power - output power to the battery   
def getPowOut(client): #Watts
    addr = 0x0027
    Cbit = readReg(client,addr)
    return Cbit
    
#Max power voltage of solar array found during last sweep
def getVmpSwe(client): #V
    addr = 0x0028
    Cbit = readReg(client,addr)
    return Cbit
    
#Max power output of solar array found during last sweep
def getPmxSwe(client): #Watts
    addr = 0x0029
    Cbit = readReg(client,addr)
    return Cbit
    
#Today's minimum battery voltage
def getVolMin(client): #V
    addr = 0x002B
    Cbit = readReg(client,addr)
    return Cbit

#Today's maximum battery voltage
def getVolMax(client): #V
    addr = 0x002C
    Cbit = readReg(client,addr)
    return Cbit

#Today's total charge amp-hours
def getAhcDay(client):
    addr = 0x002D
    Cbit = readReg(client,addr)
    return Cbit
    
#Today's total load amp-hours
def getAhlDay(client):
    addr = 0x002E
    Cbit = readReg(client,addr)
    return Cbit
    
def getChgSte(client):
    addr = 0x0011
    Cbit = readReg(client,addr)
    states = ['START', 'NIGHT_CHECK', 'DISCONNECT', 'NIGHT', 'FAULT', 'BULK_CHARGE', 'ABSORPTION', 'FLOAT', 'EQUALIZE']
    return states[Cbit]
    
def getCtrAlm(client):
    addr = 0x0023
    Cbit = readReg(client,addr)
    states = ['RTS open', 'RTS shorted', 'RTS disconnected', 'Ths open', 'Ths shorted', 'SSMPPT hot', 'Current limit', 'Current offset', 'undefined', 'undefined', 'Uncalibrated', 'RTS miswire', 'Undefined', 'Undefined', 'miswire', 'FET open', 'P12', 'high Va current limit', 'Alarm 19', 'Alarm 20', 'Alarm 21', 'Alarm 22', 'Alarm 23', 'Alarm 24']
    return states[Cbit]
    


#battery voltage Adc_vb_f: 0x0008
if __name__ == "__main__":
    # cl = ModbusSerialClient("rtu", port="/dev/tty.usbserial-DN008CBN", baudrate=9600, timeout=1,stopbits = 2)
    cl = ModbusSerialClient("rtu", port="/dev/ttyUSB0", baudrate=9600, timeout=1,stopbits = 2)
    
    
    #print makebin(2**7)
    #print bin(readReg(cl,0x002213D8))
    #print bin(readReg(cl,0x0023))
    #print bin(readReg(cl,0x0024))
    
    # hour_start = [32768 + i * 32 for i in range(32)]
    
    # vmax_start = [32768+10 + i * 32 for i in range(32)]
    
    
    # # for i in hour_start:
    # for i in vmax_start:
    #     a = readReg(cl,i+0)
    #     b = readReg(cl,i+1)
    #     # c = readReg(cl,i+2)
        
    #     print makebin(a),makebin(b)
        
    #     print bin(a)
    #     print bin(b)
    #     print bin(c)
        
    # hour1 = 32768
    # hour2 = 32769
    # hour3 = 32770
    
    # print readReg(cl,hour1)
    # print readReg(cl,hour2)
    # print readReg(cl,hour3)

    for i in range(10):    
        print getBatVol(cl)
        # sleep(.5)
        print getPanVol(cl)
        # sleep(.5)
        print getLodVol(cl)
        # sleep(.5)
        print getChgCur(cl)
        # sleep(.5)
        print getLodCur(cl)
        # sleep(.5)
        print getRemTmp(cl)
        # sleep(.5)
        print getLodSte(cl)
        sleep(.5)
    
    #  0x8000-0x81FF 
    # for i in range(0x8000,0x81FF):
        # print i
