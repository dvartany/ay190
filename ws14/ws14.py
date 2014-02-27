import sys,math
import numpy as np
import matplotlib.pyplot as mpl
import scipy as sp

def apply_bcs(x,y):
    # apply boundary conditions
    # you need to fill in code
    y[0]=y[1]
    y[-1]=y[-2]
    return y

L=100.0
def analytic(x, t, y):
    return 1./8* np.sin(2*np.pi*(x-y*t)/L)


def upwind(y):
    y2=np.zeros(len(y))
    for j in range(1,n-1):
        if y[j]>0:
            y2[j]=y[j]-y[j]*dt/dx*(y[j]-y[j-1])
        else: #upwind method depends on velocity sign
            y2[j]=y[j]-y[j]*dt/dx*(y[j+1]-y[j])
            
    return y2

# set up the grid here. Use a decent number of zones;
# perhaps to get a dx of 0.1
x = np.arange(0,L,.1)
# parameters
dx = x[1]-x[0]


n = len(x)
y = np.zeros(n)

dt =.5#check error scaling
t = 0.0

#set up initial conditions
y = analytic(x, t, y)

# evolve (and show evolution)
#mpl.ion()
#mpl.figure()
#mpl.plot(x,y,'x-') # numerical data
#mpl.show()


yold2 = y
yold = y
ntmax = 400 #change as needed


for it in range(ntmax):
    t = (1+it   )*dt
    # save previous and previous previous data
    yold2 = yold
    yold = y

    # get new data; ideally just call a function
    #y = ????
    y=upwind(y)
    y=apply_bcs(x,y)

    # get analytic result for time t
    #yana = analytic(x,L)
    # compute error estimage
    # err = ??? write error as array
    print "it = ",it
    print "time=", t
    mpl.clf()
    mpl.ylim(-.2,.2)
    #plot numerical result
    mpl.plot(x,y)
    # plot analytic results
    #mpl.plot(x,yana,'r-')
    mpl.draw()
    

#mpl.xlabel('x',fontsize=20)
#mpl.ylabel('y',fontsize=20)
#mpl.plot(x,y)
mpl.show()

