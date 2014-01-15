import scipy
import matplotlib.pyplot as plt
import numpy as np
from pylab import *

ax=gca()
#data for question 3
dat=loadtxt("/home/davidvartanyan/Desktop/ws24dat.txt")

x,y = dat[:,0], dat[:,1]
#define a polynomial that will become our solution
sol = scipy.poly1d([0.0]) 
 
for i in range(0,len(x)): 
    num = 1.0
    denom = 1.0 
    for j in range(0,len(x)): #product over j
        if i != j:
            num *= scipy.poly1d([1.0,-x[j]]) #numerator product x-x_j 
            denom *= x[i]-x[j] #denominator
    sol += (num/denom) * y[i] #sums over i

#our polynomial solution
print 'Our Lagrange interpolation polynomial is...' 
print (sol)
 
xlag = np.arange(0,1.1, 0.001) 
plt.xlabel('time [days]'); plt.ylabel('apparent magnitude')

plt.plot(x,y,'ro') 
plt.plot(xlag, sol(xlag)) 
plt.axis([-.1, 1.2, 0, 3])
text(0.25,0.75,"Cepheid Lagrange Fit",fontsize=20,
        transform=ax.transAxes)

plt.show()

