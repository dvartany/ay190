"""
Created on Sun Jan 12 03:53:37 2014

@author: davidvartanyan
"""

import pylab as pb
from pylab import *

from scipy import interpolate

dat=loadtxt("/home/davidvartanyan/Desktop/ws24dat.txt")
x,y=dat[:,0],dat[:,1]

m13=(y[1:]-y[:-1])/(x[1:]-x[:-1])
m1=np.array(m13).tolist() #our slope
m1.append(-.585)
m=np.asarray(m1)
xvec=linspace(0,1,101)


n = len(x)
mm = len(xvec)

#find k such that x[k] < xvec < x[k+1]

# expand x to an nxm, array
xx = pb.resize(x,(mm,n)).transpose()
xxx = xx > xvec

#subtract subsueqent elemnents 
z = xxx[:-1,:] - xxx[1:,:]
#reduce to index array of size mm
k = z.argmax(axis=0)

#now plug in
h = x[k+1] - x[k]
z1 = (xvec - x[k]) / h[k]

k1=np.append(k[:-1],[8])

# Hermite functions
h0 =2*z1**3-3*z1**2+1
h1 =z1**3-2*z1**2+z1
ha1=-2*z1**3+3*z1**2
hb1=z1**3-z1**2

#hermite interpolation
ynew = h0*y[k] + h1*h*m[k] + ha1*y[k+1] - hb1*h*m[k+1]


axis([-.1, 1.2, 0, 1])
y1=np.array(ynew).tolist()
ynew1=ynew[:-1:]
xnew1=xvec[:-1:]

#add linear interpolation for endpoint
ylinend=array([ynew1[-1],.302])
xlinend=array([.99,1.0])
mlinend=(.302-ynew[-2])/.1
ynew2=interpolate.interp1d(xlinend, ylinend, 'linear')

z1=[]
for n in linspace(.99,1,2):
    z1.extend([ynew2(n)])
myarray=np.asarray(z1)
xlinend2=linspace(.99,1,2)

#plot
xlabel('time [s]')
ylabel('apparent magnitude')
text(.3,.8,'Modified Hermite',fontsize=19)
p1,=plot(xlinend2,myarray,'k')
p2,=plot(xnew1,ynew1,'r')
p3,=plot(x,y,'g.')
legend((p1,p2,p3),("linear endpoint fit","piecewise cubic Hermite","data"),loc=(0.01,0.5), frameon=False)
show()
