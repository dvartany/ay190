#!/usr/bin/env python

import numpy as np
import scipy as sp
import matplotlib.pyplot as plt

# set up grid
xmin = 0.0
xmax = 1.0
npoints = 10
# set up grid
x = np.linspace(xmin,xmax,npoints)
# dx based on x[1] and x[0]
dx = x[1]-x[0]

# boundary values
A = 0.0 # inner boundary
B = 0.1 # outer boundary

def calc_rhs(u,xx):
    # rhs routine
    # rhs[0] is rhs for y
    # rhs[1] is rhs for u
    rhs = np.zeros(2)
    rhs[0] = u 
    rhs[1] = 12*xx-4

    return rhs

def integrate_RK2(z,x):
    # RK2 integrator
    
    # make an array for all points
    # entry 0 contains y
    # entry 1 contains y'
    yy = np.zeros((npoints,2))

    yy[0,0] = A # boundary value A for y at x=0
    yy[0,1] = z # guessed boundary value for y' at x=0

    for i in range(npoints-1): #RK2 
        yy[i+1,:] = yy[i,:] + dx*calc_rhs(yy[i,1]+.5*dx*calc_rhs(yy[i,1],x[i,])[1],x[i]+.5*dx)

    return yy

# get initial guess for derivative
z0 = -1100000.0
z1 = -10000000.0
yy0 = integrate_RK2(z0,x)
yy1 = integrate_RK2(z1,x)
phi0 = yy0[npoints-1,0] - B
phi1 = yy1[npoints-1,0] - B
dphidz = (phi1-phi0)/(z1-z0)# dphi/dz

i = 0
itmax = 100
err = 1.0e99
criterion = 1.0e-12

z0 = z1
phi0 = phi1
while (err > 1.0e-12 and i < itmax):
    z1 = z0 - phi0/dphidz # secant update
    yy = integrate_RK2(z1,x)
    phi1 = yy[npoints-1,0] - B
    dphidz = (phi1-phi0)/(z1-z0) # dphi/dz numerical
    err = np.abs(phi1) # your error measure
    z0 = z1
    phi0 = phi1
    i = i+1

    print i,z1,phi1
plt.subplot(2,1,1)
p1,=plt.plot(x,yy[:,0],"r-")
p2,=plt.plot(x,2.0*x**3 - 2*x**2 + 0.1*x,"k-")
plt.xlabel("x")
plt.ylabel("y[x]")
plt.legend((p1,p2),("RK2 Solution", "Exact Solution"),loc=(0.34,0.5), frameon=False)
plt.subplot(2,1,2)
plt.xlabel('x')
plt.ylabel('Error')
p3,=plt.plot(x,(2.0*x**3- 2*x**2+ 0.1*x -yy[:,0]))
plt.show()




