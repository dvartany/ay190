import numpy as np
from pylab import *

x0=1
x1=np.float32(1.0/3)
thirteenthird= np.float32(13.0/3)
fourthird=np.float32(4.0/3)
onethird=np.float32(1.0/3)

def u(n):
    if n==0: return x0
    if n==1: return x1
    return np.float32(thirteenthird*(u(n-1)) - fourthird*(u(n-2)))

#assign function to list
x = []
for n in range(16):
    x.extend([u(n)])
    
#convert list to array
x1=np.asarray(x)

def f(n):
    return np.float32((onethird)**n)
y=[]
for n in range (16):
    y.extend([f(n)])
x2=np.asarray(y)

zabs=x2-x1
zrel=(x2-x1)/x2
print zabs
print zrel