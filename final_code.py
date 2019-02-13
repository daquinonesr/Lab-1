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
import time
start_time = time.time()
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
print("--- %s seconds ---" % (time.time() - start_time))
orig_size = 800
p = np.array([[0,0],[0,orig_size],[orig_size,orig_size],[orig_size,0],[0,0]])
fig, ax = plt.subplots()
draw_squares(ax,10,p,.9)
ax.set_aspect(1.0)
ax.axis('off')
plt.show()
fig.savefig('squares1.png')
print("--- %s seconds ---" % (time.time() - start_time))
orig_size = 800
p = np.array([[0,0],[0,orig_size],[orig_size,orig_size],[orig_size,0],[0,0]])
fig, ax = plt.subplots()
draw_squares(ax,60,p,.06)
ax.set_aspect(1.0)
ax.axis('off')
plt.show()
fig.savefig('squares2.png')
print("--- %s seconds ---" % (time.time() - start_time))

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
print("--- %s seconds ---" % (time.time() - start_time))
fig, ax = plt.subplots() 
draw_circles(ax, 50, [100,0], 100,.9)
ax.set_aspect(1.0)
ax.axis('off')
plt.show()
fig.savefig('circles2.png')
print("--- %s seconds ---" % (time.time() - start_time))
fig, ax = plt.subplots() 
draw_circles(ax, 80, [100,0], 100,.93)
ax.set_aspect(1.0)
ax.axis('off')
plt.show()
fig.savefig('circles3.png')
print("--- %s seconds ---" % (time.time() - start_time))

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
print("--- %s seconds ---" % (time.time() - start_time))
fig, ax = plt.subplots() 

draw_circles(ax, 35, [100,0], 100,.9)


ax.set_aspect(1.0)
ax.axis('off')
plt.show()
fig.savefig('circles5.png')
print("--- %s seconds ---" % (time.time() - start_time))
fig, ax = plt.subplots() 

draw_circles(ax, 55, [100,0], 100,.93)


ax.set_aspect(1.0)
ax.axis('off')
plt.show()
fig.savefig('circles6.png')
print("--- %s seconds ---" % (time.time() - start_time))

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
print("--- %s seconds ---" % (time.time() - start_time))

def circlea(center,rad):
    n = int(4*rad*math.pi)
    t = np.linspace(0,6.3,n)
    x = center[0]+rad*np.sin(t)
    y = center[1]+rad*np.cos(t)
    return x,y

def draw_circles(ax,n,center,radius):
    if n==0:
        return
    if n>0:
        x,y = circlea(center,radius)
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
draw_circles(ax,3 , [150,150], 150)


ax.set_aspect(1.0)
ax.axis('off')
plt.show()
fig.savefig('circles4.png')
print("--- %s seconds ---" % (time.time() - start_time))

plt.close("all") 
fig, ax = plt.subplots() 
a=100
draw_circles(ax,4 , [150,150], 150)


ax.set_aspect(1.0)
ax.axis('off')
plt.show()
fig.savefig('circlesx.png')
print("--- %s seconds ---" % (time.time() - start_time))

plt.close("all") 
fig, ax = plt.subplots() 
a=100
draw_circles(ax,5 , [150,150], 150)


ax.set_aspect(1.0)
ax.axis('off')
plt.show()
fig.savefig('circlesx1.png')
print("--- %s seconds ---" % (time.time() - start_time))

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
print("--- %s seconds ---" % (time.time() - start_time))

