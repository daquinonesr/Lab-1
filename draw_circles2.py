#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Feb  4 10:30:12 2019

@author: diegoquinones
"""

import matplotlib.pyplot as plt
import numpy as np
import math 

def circle(center,rad):
    n = int(4*rad*math.pi)
    t = np.linspace(0,6.3,n)
    x = center[0]+rad*np.sin(t)
    y = center[1]+rad*np.cos(t)
    return x,y

def draw_circles(ax,n,center,radius,w):
    if n>0:
        x,y = circle(center,radius)
        ax.plot(x,y,color='k')
        center[0]=radius*w
        draw_circles(ax,n-1,center,radius*w,w)

      
plt.close("all") 
fig, ax = plt.subplots() 

draw_circles(ax, 6, [100,0], 100,.65)


ax.set_aspect(1.0)
ax.axis('off')
plt.show()
fig.savefig('circles4.png')
fig, ax = plt.subplots() 

draw_circles(ax, 35, [100,0], 100,.9)


ax.set_aspect(1.0)
ax.axis('off')
plt.show()
fig.savefig('circles5.png')
fig, ax = plt.subplots() 

draw_circles(ax, 55, [100,0], 100,.93)


ax.set_aspect(1.0)
ax.axis('off')
plt.show()
fig.savefig('circles6.png')

