from pithy import *

def getCenter(x,y,w,h):
    xc = x+w/2.
    yc = y+h/2.
    r = w/4.+h/4.
    # print 'x='+str(xc)+';'
    # print 'y='+str(yc)+';'
    # print 'r='+str(r)+';
    # print str(xc)+','+str(yc)+','+str(r)
    outstr = 'x0 = '+str(xc)+';\n' + 'y = '+str(yc)+';\n'+'ra = '+str(r)+';'
    # print outstr
    return [xc,yc,r]
    # return outstr
    
    
def getOval(arra,rplus=0):
    xc = arra[0]
    yc = arra[1]
    r  = arra[2]+rplus
    
    x = xc-r
    y = yc-r
    w = 2*r
    h = 2*r
    # print str(x)+','+str(y)+','+str(w)+','+str(h)
    outstr = 'makeOval('+str(x)+','+str(y)+','+str(w)+','+str(h)+');'
    return outstr
    # return [x,y,w,h]
    
    
# print getCenter(257, 279, 453, 453)

# print getOval(getCenter(257, 279, 453, 453),180)

print getOval(getCenter(257, 279, 453, 453),-150)

# print getOval(getCenter(191, 254, 534, 534),155)


