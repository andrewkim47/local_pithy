from pithy import *
from urllib import urlopen as uo
import ast
from time import sleep,time
import os
import datetime
# from pymongo import MongoClient as mc

#MongoDB setup
#128.112.72.89 - Spike
#"192.81.219.77 - DO
# client = mc("128.112.72.89",27017)
# db = client.test_db
# ad = db['temperature_data']


UNO = "http://localhost:9021" #needs NodeForwarder 

def awrite(val):
    uo(UNO+"/write/"+str(val)).read()
    sleep(.5)

def aread():
    return uo(UNO+"/read/").read()
    
awrite('F1')
sleep(3)
awrite('F0')