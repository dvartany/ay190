# -*- coding: utf-8 -*-
"""
Created on Fri Jan 10 18:34:59 2014

@author: davidvartanyan
"""

import scipy
import matplotlib.pyplot as plt
import numpy as np
from pylab import *

from scipy import interpolate

dat=loadtxt("/home/davidvartanyan/Desktop/ws24dat.txt")

x,y = dat[:,0], dat[:,1]

#scipy's library lent the following
f = interpolate.interp1d(x, y, 'linear')
g = interpolate.interp1d(x, y, 'quadratic')

z1=[]
for n in linspace(0,1,100):
    z1.extend([f(n)])
myarray=np.asarray(z1)

#write as list then array        
z=[]
for n in np.linspace(0,1,100):
    z.extend([g(n)])
myarray2=np.asarray(z)

xlabel('time [s]')
ylabel('apparent magnitude')
text(.02,.5,'Linear and Quadratic Fits',fontsize=19)
time= linspace(0,1,100)
p1,= plot(x,y,'ro')
p2,=plot(time, myarray,'r',label=r'linear')
p3,=plot(time, myarray2,'b',label=r'quadratic')
legend((p2,p3),("linear","quadratic"),loc=(0.7,0.3), frameon=False)
show()