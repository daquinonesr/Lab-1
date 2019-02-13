#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Feb 12 23:16:27 2019

@author: diegoquinones
Full code
"""
import numpy as np
import matplotlib.pyplot as plt
import math 

def draw_squares(ax,n,p,w):
    if n>0:
        i1 = [1,2,3,0,1]
        q = p*w + p[i1]*(1-w)
        ax.plot(p[:,0],p[:,1],color='k')
        draw_squares(ax,n-1,q,w)

plt.close("all") 
orig_size = 800
p = np.array([[0,0],[0,orig_size],[orig_size,orig_size],[orig_size,0],[0,0]])
fig, ax = plt.subplots()
draw_squares(ax,11,p,.2)
ax.set_aspect(1.0)
ax.axis('off')
plt.show()
fig.savefig('squares.png')
orig_size = 800
p = np.array([[0,0],[0,orig_size],[orig_size,orig_size],[orig_size,0],[0,0]])
fig, ax = plt.subplots()
draw_squares(ax,10,p,.9)
ax.set_aspect(1.0)
ax.axis('off')
plt.show()
fig.savefig('squares1.png')
orig_size = 800
p = np.array([[0,0],[0,orig_size],[orig_size,orig_size],[orig_size,0],[0,0]])
fig, ax = plt.subplots()
draw_squares(ax,60,p,.06)
ax.set_aspect(1.0)
ax.axis('off')
plt.show()
fig.savefig('squares2.png')

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
        draw_circles(ax,n-1,center,radius*w,w)
      
plt.close("all") 
fig, ax = plt.subplots() 
draw_circles(ax, 3, [100,0], 100,.5)
ax.set_aspect(1.0)
ax.axis('off')
plt.show()
fig.savefig('circles.png')
fig, ax = plt.subplots() 
draw_circles(ax, 50, [100,0], 100,.9)
ax.set_aspect(1.0)
ax.axis('off')
plt.show()
fig.savefig('circles2.png')
fig, ax = plt.subplots() 
draw_circles(ax, 80, [100,0], 100,.93)
ax.set_aspect(1.0)
ax.axis('off')
plt.show()
fig.savefig('circles3.png')

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

def draw_squares(ax,n,p,w,size):
    if n>0:
        q = p+w*size + p+w*size
        ax.plot(p[:,0],p[:,1],color='k')
        draw_squares(ax,n-1,q,w,size)

        

plt.close("all") 
orig_size = 800
p = np.array([[0,0],[0,orig_size],[orig_size,orig_size],[orig_size,0],[0,0]])
fig, ax = plt.subplots()
draw_squares(ax,3,p,.2,800)
ax.set_aspect(1.0)
ax.axis('off')
plt.show()
fig.savefig('squares.png')

def binary(ax,n,p,w,orig_size):
    if n>0:
        p = np.array([[0,0],[orig_size/2,orig_size/2],[orig_size,0]])
        binary(ax,n-1,p,w,orig_size/2)
        ax.plot(p[:,0],p[:,1],color='k') 
        binary(ax,n-1,p,w,orig_size/2)

plt.close("all") 
orig_size = 800
p = np.array([[0,0],[orig_size,orig_size],[orig_size,0]])
fig, ax = plt.subplots()
binary(ax,2,p,.2,800)
ax.set_aspect(1.0)
ax.axis('off')
plt.show()
fig.savefig('squares.png')

