from pithy import *

def autolabel(rects):
    """
    Attach a text label above each bar displaying its height
    """
    for rect in rects:
        height = rect.get_height()
        ax.text(rect.get_x() + rect.get_width()/2., 1.05*height,
                '{0:.3f}'.format(height),
                ha='center', va='bottom')

N = 6
width = 3
gap = 3

deg = '$^\circ$C'

cold = [
    3718.48297119, #FujCold
    3343.51086617, #EveCold
    3605.37600517, #QuaCold
    4132.39574432, #CopCold
    4154.49571609, #EneCold
    3882.54618645, #EcoCold
]

room = [
    4035.38131714, #FujRoom 
    3437.53314018, #EveRoom 
    4584.34247971, #QuaRoom 
    4465.03448486, #CopRoom 
    4507.02762604, #EneRoom 
    4195.48463821, #EcoRoom 

]

hott = [
    4338.41133118, #FujHott
    3734.52305794, #EveHott
    5046.69046402, #QuaHott
    4772.93157578, #CopHott
    4767.94338226, #EneHott
    4435.22357941, #EcoHott
]
spacing = (width*3 + gap)

x1 = arange(width*(1-1),(width*3+gap)*6,spacing)
x2 = arange(width*(2-1),(width*3+gap)*6,spacing)
x3 = arange(width*(3-1),(width*3+gap)*6,spacing)

print x1
print x2
print x3

tickind = [x2[0]+width/2.+spacing*(i) for i in range(N)]
ticklab = [
    'Fujitsu',
    'EverReady',
    'Quantum',
    'CopperTop',
    'Energizer',
    'EcoAdvanced',
]

# print tickind

fig, ax = plt.subplots()
rects1 = ax.bar(x1, cold, width, color='b')
rects2 = ax.bar(x2, room, width, color='g')
rects3 = ax.bar(x3, hott, width, color='r')
# add some text for labels, title and axes ticks
ax.set_ylabel('Energy (mWh)')
# ax.set_xlabel('Sample')
ax.set_title('Energy')
ax.set_xticks(tickind)
# ax.set_xticks(ind + width)
ax.set_xticklabels(ticklab)
ax.legend(
        (rects1[0], rects2[0],rects3[0]),
        ('6.5'+deg,'20'+deg,'51.5'+deg),
        loc='center right',bbox_to_anchor=(1.27, 0.5))

# autolabel(rects1)
# autolabel(rects2)
xlim(x1[0]-width,x3[-1]+2*width)
ylim(0,5250)
grid(axis='y')
showme()
clf()





