# -*- coding: utf-8 -*-
"""
Created on Fri Jan 17 11:44:09 2014

@author: davidvartanyan
"""

from numpy import *
from scipy import special as sp

[laguerre_roots,laguerre_weights]=sp.l_roots(2,0)

#from Wolfram Alpha
k=20 #in MeV
h=1.97327*10**-11 #in Mev cm

def f(x):
    return x**2*exp(x)/(exp(x)+1)

print sum(laguerre_weights*f(laguerre_roots))