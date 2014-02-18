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


def analytic(x, v, t,sigma):
    return np.exp(-((x-v*t)-x0)**2/(2*sigma**2))

def ftcs(y):
    y1=np.zeros(len(y))
    for i in range(1,len(y1)-1): #since we call y[j-1] and y[j+1] below,fixing range
        y1[i]=y[i]-v*dt/(2.0*dx)*(y[i+1]-y[i-1])
    return y1

def upwind(y):
    y2=np.zeros(len(y))
    for j in range(1,len(y2)):
        y2[j]=y[j]-v*dt/dx*(y[j]-y[j-1])
    return y2
    
def laxfried(y):
    y1=np.zeros(len(y))
    for i in range(1,len(y1)-1):
        y1[i]=.5*(y[i+1]+y[i-1]) - v*dt/(2*dx)*(y[i+1]-y[i-1])
    return y1

def leapfrog(y):
    y1=np.zeros(len(y))
    for i in range(1,len(y1)-1):
        y1[i]=yold[i] - v*dt/(2*dx)*(y[i+1]-y[i-1])
    return y1
    
def laxwend(y):
    y1=np.zeros(len(y))
    for i in range(1,len(y1)-1):
        y1[i]=y[i] - v*dt/(2*dx)*(y[i+1]-y[i-1]) 
        + (v*dt)**2/(2*dx**2)*(y[i-1]-2* y[i]+y[i+1])
    return y1
    
# set up the grid here. Use a decent number of zones;
# perhaps to get a dx of 0.1
x = np.linspace(0,100,1001)
# parameters
dx = x[1]-x[0]
v = 0.1

n = len(x)
y = np.zeros(n)
cfl = .25 #check error scaling below, 1.0 returns arrays of 0
dt = cfl*dx/v#check error scaling
t = 0.0

# for initial data
sigma = np.sqrt(15.0)/5
x0 = 30.0

#set up initial conditions
y = analytic(x, v, t,sigma)

# evolve (and show evolution)
#mpl.ion()
#mpl.figure()
#mpl.plot(x,y,'x-') # numerical data
#mpl.plot(x,analytic(x,v,t,sigma),'r-') # analytic data
#mpl.show()


yold2 = y
yold = y
ntmax = 200 #change as needed
err=np.zeros(ntmax)
for it in range(ntmax):
    t = (1+np.asarray(it))*dt
    # save previous and previous previous data
    yold2 = yold
    yold = y

    # get new data; ideally just call a function
    #y = ????
    #y=upwind(y)
    #y=ftcs(y)
    y=laxwend(y)
    #y=laxfried(y)
    #y=leapfrog(y)    
    #after update, apply boundary conditions
    # apply_bcs(x,y)
    y=apply_bcs(x,y)

    # get analytic result for time t
    yana = analytic(x,v,t,sigma)
    # compute error estimage
    # err = ??? write error as array
    err[it]=np.abs(np.max(y)-np.max(yana))
    #print "it = ",it,err[it]
    #mpl.clf()
    #mpl.ylim(0,1)
    # plot numerical result
    #mpl.plot(x,y,'k-')
    # plot analytic results
    #mpl.plot(x,yana,'r-')
    #mpl.draw()
    
#plot error
t=np.zeros(ntmax)
for it in range(ntmax):
    t[it] = (1+it)*dt
mpl.semilogy(t,err,'k-')
mpl.xlabel('Time [s]',fontsize=20)
mpl.ylabel('Error',fontsize=20)
print err
mpl.show()



