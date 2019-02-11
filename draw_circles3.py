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

def draw_circles(ax,n,center,radius):
    if n==0:
        return
    if n>0:
        x,y = circle(center,radius)
        ax.plot(x+5,y,color='k')
    if n>1:
        n=n-1

        draw_circles(ax,n,center,radius/3)
        draw_circles(ax,n,[center[0]+radius*2/3,center[1]],radius/3)
        
        draw_circles(ax,n,[center[0]-radius*2/3,center[1]],radius/3)
        
        draw_circles(ax,n,[center[0],center[1]+radius*2/3],radius/3)
        draw_circles(ax,n,[center[0],center[1]-radius*2/3],radius/3)


                    

        
    

      
plt.close("all") 
fig, ax = plt.subplots() 
a=100
draw_circles(ax,4 , [150,150], 150)


ax.set_aspect(1.0)
ax.axis('off')
plt.show()
fig.savefig('circles4.png')


