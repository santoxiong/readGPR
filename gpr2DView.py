# -*- coding: utf-8 -*-
"""
Created on Fri May  6 11:19:28 2022

@author: zhaodi
"""

from matplotlib import cm

# viridis = cm.get_cmap('gray', 256)
viridis = cm.get_cmap('viridis', 256)
import threading

import os

os.environ['KMP_DUPLICATE_LIB_OK'] = 'True'

# import torch
import numpy as np
# import pandas as pd
import matplotlib.pyplot as plt


def file_name(file_dir, fileType='.mat'):
    L = []
    for root, dirs, files in os.walk(file_dir):
        for file in files:
            if os.path.splitext(file)[1] == fileType:
                L.append(os.path.join(root, file))
    return L


def toggle_loc(event):
    global lx, ly, ch
    loc = event
    print(loc)
    y = event.ydata.astype(np.int32)
    x = event.xdata.astype(np.int32)
    ax_histx.imshow(dataALL[y, :, :].T, aspect='auto', cmap='gray')
    ayHistyLx.set_ydata(y)
    # ax.add_artist(lines.Line2D([y-1, 0],[dataALL.shape[1]-1,y-1]))
    # ax.add_artist(lines.Line2D([x,0],[x,dataALL.shape[0]]))

    ax_histy.imshow(dataALL[:, x, :], aspect='auto', cmap='gray')
    # ax_histy.imshow(dataALL[:,0,:], aspect='auto')
    # ax_histy.set_title(x)

    axHistxLy.set_xdata(x)

    lx.set_ydata(y)
    ly.set_xdata(x)
    txt.set_text('x=%1.2d  y=%1.2d  ch=%d' % (x, y, cIndex[ch]))
    txt.set_x(x / minLen - 0.115)
    txt.set_y(1 - y / 2048 - 0.1)
    plt.pause(1)


def nextChannel(event):
    global ch
    # fig0.clf()
    ch += 1
    ch = ch % 12
    ax.imshow(dataALL[:, :, cIndex[ch]], aspect='auto', cmap='gray')
    ax_histx.set_title(cIndex[ch])
    plt.pause(1)


# %%
path = os.getcwd()

files = file_name(path, '.bin')

file = files[0]

# sigPro = sigProcess()

pcdALL = []
zoom = 10
cIndex = [0, 1, 3, 2, 4, 5, 7, 6, 8, 9, 11, 10]
tIndex = [116, 118, 116, 118, 115, 116, 124, 124, 121, 121, 120, 120]

dataALL = []
dataLen = []
for itr, file in enumerate(files):
    data = np.fromfile(file, dtype=np.int16)  # 读取二进制文件
    data.shape = int(data.shape[0] / 2048), 2048
    data = data.T.astype(np.double) / 65535 + 1
    data = data / 2
    data = np.mat(data)[tIndex[itr]:-130 + tIndex[itr]:1, 0:-1]

    dataALL.append(np.expand_dims(np.array(data), 2))
    dataLen.append(data.shape[1])

    # ax = plt.figure().add_subplot(projection='3d')

    # color_raw = o3d.cpu.pybind.geometry.Image(data.astype(np.uint8).copy())
    # depth_raw = o3d.cpu.pybind.geometry.Image(np.ones(data.shape).astype(np.uint8)*(itr+1)*10)
    # rgbd_image = o3d.geometry.RGBDImage.create_from_color_and_depth(color_raw, depth_raw)

    # pcd1 = o3d.io.read_point_cloud("D:/RoadDet/RDDS/data/pcd_file_101658/0.pcd")

    # data = data
minLen = min(dataLen)
for i, data in enumerate(dataALL):
    dataALL[i] = data[:, :minLen]
dataALL = np.concatenate(dataALL, 2)

# %%

# import numpy as np
# import matplotlib.pyplot as plt
from mpl_toolkits.axes_grid1 import make_axes_locatable

# import matplotlib.lines as lines


fig0, ax = plt.subplots(figsize=(10, 5))
ch = 0
# the scatter plot:
ax.imshow(dataALL[:, :, ch], aspect='auto', cmap='gray')

# Set aspect of the main axes.
# ax.set_aspect(1.)

# create new axes on the right and on the top of the current axes
divider = make_axes_locatable(ax)
# below height and pad are in inches
ax_histx = divider.append_axes("top", 1.2, pad=0.1, sharex=ax)
ax_histy = divider.append_axes("right", 1.2, pad=0.1, sharey=ax)

# make some labels invisible
ax_histx.xaxis.set_tick_params(labelbottom=False)
ax_histy.yaxis.set_tick_params(labelleft=False)

axHistxLy = ax_histx.axvline(color='k', ls=':')  # the vert line
ayHistyLx = ax_histy.axhline(color='k', ls=':')  # the horiz line

lx = ax.axhline(color='k', ls='-.')  # the horiz line
ly = ax.axvline(color='k', ls='-.')  # the vert line
txt = ax.text(0.7, 0.7, '', transform=ax.transAxes)

loc = None

# class SnaptoCursor(object):
#     """
#     Like Cursor but the crosshair snaps to the nearest x,y point
#     For simplicity, I'm assuming x is sorted
#     """

#     def __init__(self, ax, x, y):
#         self.ax = ax
#         self.lx = ax.axhline(color='k')  # the horiz line
#         self.ly = ax.axvline(color='k')  # the vert line
#         self.x = x
#         self.y = y
#         # text location in axes coords
#         self.txt = ax.text(0.7, 0.9, '', transform=ax.transAxes)

#     def mouse_move(self, event):

#         if not event.inaxes:
#             return

#         x, y = event.xdata, event.ydata

#         indx = min(np.searchsorted(self.x, [x])[0], len(self.x) - 1)
#         x = self.x[indx]
#         y = self.y[indx]
#         # update the line positions
#         self.lx.set_ydata(y)
#         self.ly.set_xdata(x)

#         self.txt.set_text('x=%1.2f, y=%1.2f' % (x, y))
#         print('x=%1.2f, y=%1.2f' % (x, y))
#         plt.draw()


ax_histx.set_title(cIndex[ch])
# fig.canvas.mpl_connect('draw_event', toggle_pause)
fig0.canvas.mpl_connect('button_press_event', toggle_loc)
# fig0.canvas.mpl_connect('button_press_event', toggle_loc)
fig0.canvas.mpl_connect('key_press_event', nextChannel)

plt.show()
# ax_histx.set_aspect(1.5)
