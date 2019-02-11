import numpy as np
import matplotlib.pyplot as plt

def draw_squares(ax,n,p,w,orig_size):
    if n>0:
        p = np.array([[0,0],[orig_size/2,orig_size/2],[orig_size,0]])
        draw_squares(ax,n-1,p,w,orig_size/2)
        ax.plot(p[:,0],p[:,1],color='k') 
        draw_squares(ax,n-1,p,w,orig_size/2)

plt.close("all") 
orig_size = 800
p = np.array([[0,0],[orig_size,orig_size],[orig_size,0]])
fig, ax = plt.subplots()
draw_squares(ax,2,p,.2,800)
ax.set_aspect(1.0)
ax.axis('off')
plt.show()
fig.savefig('squares.png')



