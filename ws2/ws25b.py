# -*- coding: utf-8 -*-
"""
Created on Wed Jan 15 00:01:10 2014

@author: davidvartanyan
"""

import pylab as P
from pylab import *
import numpy as np
from scipy import interpolate

dat=loadtxt("/home/davidvartanyan/Desktop/ws24dat.txt")
x,y=dat[:,0],dat[:,1]

xnew =np.linspace(0,1,100001)
tck = interpolate.splrep(x,y)
ynew2= interpolate.splev(xnew,tck,der=0)

xlabel('time [s]')
ylabel('apparent magnitude')
text(.2,.6,'Cubic Spline',fontsize=19)
p1,=plot(x,y,'go')
p2,=plot(xnew,ynew2,'r')
legend((p1,p2),("data","cubic spline"),loc=(0.65,0.2), frameon=False)
show()