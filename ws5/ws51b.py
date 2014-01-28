import itertools
import matplotlib.pyplot as plt
from numpy import *
from pylab import *
from matplotlib import rc, rcParams
from matplotlib.pyplot import *
from lmfit import minimize, Parameters, Parameter, report_fit
import numpy as np  
from numpy import *
from pylab import *
import matplotlib.pyplot as mpl

dat=np.loadtxt("/home/davidvartanyan/Desktop/ws5sigma.dat")
x= log(dat[:,1])
y= dat[:,7]

sx, sy, sx2, sxy =sum(x), sum(y), sum(x**2), sum(x*y)
s=88

a1= (sy*sx2-sx*sxy)/(s*sx2-sx**2)
a2= (s*sxy-sx*sy)/(s*sx2-sx**2)
line= a1+a2*x

xlabel(r'log $\sigma_*/ \mathrm{km\, s}^{-1}$')
ylabel(r'log $M_{BH}/M_{\odot}$')

print a1,a2
plot(x,line,'ro', x,y,'*')
savefig('/home/davidvartanyan/Desktop/ws5bfig.png') 
show()