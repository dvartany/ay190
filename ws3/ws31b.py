import scipy
import matplotlib.pyplot as plt
import numpy as np
from pylab import *

x=linspace(0,np.pi,100)
h=x[1:]-x[:-1]
arg=.5*(x[1:]+x[:-1])

mdpt=np.sum(h*arg*np.sin(arg))

def mdpt2(i): 
    return sum(h[:i]*arg[:i]*np.sin(arg[:i]))

y=[]
for n in linspace(1,9,9):
    y.extend([mdpt2(n)])

trapt=.5*np.sum(h*(x[1:]*np.sin(x[1:])+x[:-1]*np.sin(x[:-1])))

def trapt2(i):
    return .5*sum(h[:i]*(x[1:][:i]*np.sin(x[1:][:i])+x[:-1][:i]*np.sin(x[:-1][:i])))

yt=[]
for n in linspace(1,9,9):
    yt.extend([trapt2(n)])

simp=1./6*np.sum(h*(x[1:]*np.sin(x[1:])+x[:-1]*np.sin(x[:-1])+arg*4*np.sin(arg)))

arg1, arg2=x[1:],x[:-1]
def simp2(i):
    return 1./6*np.sum(h[:i]*(x[1:][:i]*np.sin(x[1:][:i])+x[:-1][:i]*np.sin(x[:-1][:i])+arg[:i]*4*np.sin(arg[:i])))

ys=[]
for n in linspace(1,9,9):
    ys.extend([simp2(n)])

print mdpt-pi, trapt-pi, simp-pi, 1./16.

