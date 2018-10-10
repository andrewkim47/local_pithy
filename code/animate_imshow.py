import matplotlib
matplotlib.use('agg')
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation


# create a figure with two subplots
fig, (ax1, ax2, ax3) = plt.subplots(3,1)

# intialize line objects (one in each axes)
# line1, = ax1.plot([], [], lw=2)
# line2, = ax2.plot([], [], lw=2, color='r')
# line3, = ax3.plot([], [], lw=2, color='r')

a=np.random.random((5,5))
line1 = ax1.imshow(a)
line2 = ax2.imshow(a)
line3 = ax3.imshow(a)
line = [line1, line2, line3]

#axes initialize
ax1.set_ylim(0, 5)
ax1.set_xlim(0, 5)
ax2.set_ylim(0, 5)
ax2.set_xlim(0, 5)
ax3.set_ylim(0, 5)
ax3.set_xlim(0, 5)

v1= ax1.axvline(x=0)

a=np.random.random((5,5))


# initialize the data arrays 
xdata, y1data, y2data, y3data = [], [], [], []

def animate(i):
    
    # update the data of both line objects
    # line[0].set_data(xdata, y1data)
    # line[1].set_data(xdata, y2data)
    # line[2].set_data(xdata, y3data)
    v1.set_xdata(i/2)

    return line

anim = animation.FuncAnimation(fig, animate, blit=True, interval=10, repeat=False)
anim.save('files/test.mp4',fps=60)

# anim = animation.FuncAnimation(fig, animate, init_func=init,frames=60 ,blit=True)

# import matplotlib
# matplotlib.use('agg')
# import numpy as np
# import matplotlib.pyplot as plt
# import matplotlib.animation as animation

# def data_gen():
#     t = data_gen.t
#     cnt = 0
#     while cnt < 1000:
#         cnt+=1
#         t += 0.05
#         y1 = np.sin(2*np.pi*t) * np.exp(-t/10.)
#         y2 = np.cos(2*np.pi*t) * np.exp(-t/10.)
#         # adapted the data generator to yield both sin and cos
#         yield t, y1, y2

# data_gen.t = 0

# # create a figure with two subplots
# fig, (ax1, ax2) = plt.subplots(2,1)

# # intialize two line objects (one in each axes)
# line1, = ax1.plot([], [], lw=2)
# line2, = ax2.plot([], [], lw=2, color='r')
# line = [line1, line2]

# # the same axes initalizations as before (just now we do it for both of them)
# for ax in [ax1, ax2]:
#     ax.set_ylim(-1.1, 1.1)
#     ax.set_xlim(0, 5)
#     ax.grid()

# # initialize the data arrays 
# xdata, y1data, y2data = [], [], []
# def run(data):
#     # update the data
#     t, y1, y2 = data
#     xdata.append(t)
#     y1data.append(y1)
#     y2data.append(y2)

#     # axis limits checking. Same as before, just for both axes
#     for ax in [ax1, ax2]:
#         xmin, xmax = ax.get_xlim()
#         if t >= xmax:
#             ax.set_xlim(xmin, 2*xmax)
#             ax.figure.canvas.draw()

#     # update the data of both line objects
#     line[0].set_data(xdata, y1data)
#     line[1].set_data(xdata, y2data)

#     return line

# ani = animation.FuncAnimation(fig, run, data_gen, blit=True, interval=10,
#     repeat=False)
# ani.save('files/test.mp4',fps=60)


# #Generates an MP4 video of a line moving across an imshow

# #http://stackoverflow.com/questions/17212722/matplotlib-imshow-how-to-animate
# import numpy as np
# import matplotlib
# matplotlib.use('agg')
# from matplotlib import pyplot as plt
# from matplotlib import animation
# # from pithy import drop_pre

# filename = 'files/imshow_animate.mp4'

# # First set up the figure, the axis, and the plot element we want to animate
# fig = plt.figure()
# ax = plt.axes(xlim=(0, 6), ylim=(0, 6))
# a=np.random.random((5,5))
# im=plt.imshow(a,interpolation='none')
# vl = ax.axvline(x=0)

# # initialization function: plot the background of each frame
# def init():
#     im.set_data(np.random.random((5,5)))
#     vl = ax.axvline(x=0)
#     return [im]

# # animation function.  This is called sequentially
# def animate(i):
#     vl.set_xdata(x=(i+1)/12.)
#     return [im]

# # # call the animator.
# anim = animation.FuncAnimation(fig, animate, init_func=init,frames=60 ,blit=True)
# anim.save(filename, fps=60)#, extra_args=['-vcodec', 'libx264'])

# print 'heh'
