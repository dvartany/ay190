# -*- coding: utf-8 -*-
"""
Created on Thu Jan  9 10:33:41 2014

@author: davidvartanyan
"""

import numpy as np

x0=1
x1=np.float32(1.0/3)
thirteenthird= np.float32(13.0/3)
fourthird=np.float32(4.0/3)

def u(n):
    if n==0: return x0
    if n==1: return x1
    return thirteenthird*(u(n-1)) - fourthird*(u(n-2))
x = []
for n in range(16):
    x.extend([u(n)])

print x 

