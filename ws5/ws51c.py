# -*- coding: utf-8 -*-
"""
Created on Mon Jan 27 13:36:37 2014

@author: davidvartanyan
"""

from numpy import *
from matplotlib.pyplot import *

dat=loadtxt("/home/davidvartanyan/Desktop/ws5sigma.dat")
x= log(dat[:,1])
y= dat[:,7]
errx= log(dat[:,2])
erry= dat[:,9]

xs, ys=sorted(x), sorted(x)

def deriv(i):
    if [xs[i+1] != xs[i]]:
        return (ys[i+1]-ys[i])/(xs[i+1])
    if [xs[i+1] == xs[i]]: return 0

errx1,erry1=errx[:-1], erry[:-1]

#additional error to y from error in x
def erryex(i):
    return (deriv(i)*errx1[i])
z=[]
z.append([erryex(i) for i in range(87)])
z1=asarray(z[0])

errysq = erry1**2+ z1**2

s, sx, sy=sum(errysq**-1), sum(x[:-1]/(errysq)), sum(y[:-1]/(errysq))
sx2, sxy=sum(x[:-1]**2/(errysq)), sum(x[:-1]*y[:-1]/(errysq))

a1= (sy*sx2-sx*sxy)/(s*sx2-(sx)**2)
a2= (s*sxy-sx*sy)/(s*sx2-(sx)**2)
line= a1+a2*x[:-1]

print a1,a2

xlabel(r'log $\sigma_*/ \mathrm{km\, s}^{-1}$')
ylabel(r'log $M_{BH}/M_{\odot}$')


plot(x[:-1],line,'-', x[:-1],y[:-1],'*')
savefig('/home/davidvartanyan/Desktop/ws5cfig.png')
show()
