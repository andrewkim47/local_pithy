from pithy import *

TDKshh= [9.16344619e-04,2.49032242e-04,1.86401575e-07]
def TDKR2T(r,shh=TDKshh):
    tinv = shh[0] + shh[1] * log(r) + shh[2] * (log(r)**3)
    return 1.0/tinv

HONshh= [7.76655496e-04,2.73964154e-04,7.22722438e-08]
def HONR2T(r,shh=HONshh):
    tinv = shh[0] + shh[1] * log(r) + shh[2] * (log(r)**3)
    return 1.0/tinv

def temps(As):
    Rs = []
    Ts = []
    
    for i in [0,1,2]:
        Rs.append(vdiv(As[i],4980))
        Ts.append(TDKR2T(Rs[i])-273)
    
    Rs.append(vdiv(As[3],9940))
    Ts.append(HONR2T(Rs[3])-273)
    
    return Ts,Rs

def temps2(As):
    Rs = []
    Ts = []
    
    for i in [0,1,2]:
        Rs.append(vdiv2(As[i],4980))
        Ts.append(TDKR2T(Rs[i])-273)
    
    Rs.append(vdiv2(As[3],9940))
    Ts.append(HONR2T(Rs[3])-273)
    
    return Ts,Rs
    
def vdiv(A,R2):
    R1 = R2 * (4095./array(A)-1)
    return R1

def vdiv2(A,R2):
    R1 = R2 * (1024./array(A)-1)
    return R1


# data = [512,512,512,430]
# print temps2(data)[0]


# print HONR2T(vdiv2(462,9970))-273 #water 1
# print HONR2T(vdiv2(455,9970))-273 #water 2
# print HONR2T(vdiv2(468,9970))-273 #single

print HONR2T(vdiv2(280,4900))-273 #single
print TDKR2T(vdiv2(280,4900))-273 #single


# print HONR2T(vdiv(1250,4900))-273 #single
# print TDKR2T(vdiv(1250,4900))-273 #single

# print HONR2T(vdiv(1300,4900))-273 #single
# print TDKR2T(vdiv(1300,4900))-273 #single




