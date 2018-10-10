import numpy as np
import matplotlib
matplotlib.use('agg')
from matplotlib import pyplot as plt
from matplotlib import animation

x = np.linspace(0, 6, 100)
y = np.sin(x)

# First set up the figure, the axis, and the plot element we want to animate
fig = plt.figure()
ax = plt.axes(xlim=(0,6),ylim=(-2,2))
vl = ax.axvline(x=0)
line, = ax.plot([], [], lw=2)

# initialization function: plot the background of each frame
def init():
    line.set_data(x,y)
    return line,

# animation function.  This is called sequentially
def animate(i):
    vl.set_xdata(i/10.)
    return line,

# call the animator.  blit=True means only re-draw the parts that have changed.
anim = animation.FuncAnimation(fig, animate, init_func=init,frames=60, interval=60, blit=True)
anim.save('files/basic_animation.mp4', fps=60)
