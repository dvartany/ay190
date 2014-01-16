import scipy
import matplotlib.pyplot as plt
import numpy as np
from pylab import *

ax = gca()

def g(x):
    return x**3-5*x**2+x

#true derivative
def gp(x):
    return 3*x**2-10*x+1

q=[]
for n in linspace(-2,6,100):
    q.extend([gp(n)])
q1=np.asarray(q)  

#forward difference, h
def D(f,h=1):
    def df(x):
         deriv=(f(x+h)-f(x))/h
         return deriv
    return df

#assign an f to our definition of D
df= D(g)
#discretize over a list

a= [df(x) for x in linspace(-2,6,100)]

#fwd, h/2
def DP(j,h=.5):
     def dp(x):
         deriv=(j(x+h)-j(x))/h
         return deriv
     return dp

dg= D(g)
dp=DP(g)
ap = [dp(x) for x in linspace(-2,6,100)]

arraya = np.asarray(a)
arrayap= np.asarray(ap)

#central difference, h
def D1(z,h=1):
    def dz(x):
         deriv2=.5*(z(x+h)-z(x-h))/h
         return deriv2
    return dz
#cent, h/2
def D2(z,h=.5):
    def d2(x):
         deriv3=.5*(z(x+h)-z(x-h))/h
         return deriv3
    return d2
    
dz = D1(g)
d2=D2(g)
a1= [dz(x) for x in linspace (-2,6,100)]
a2= [d2(x) for x in linspace (-2,6,100)]

arraya1=np.asarray(a1)
arraya2=np.asarray(a2)

abserrc=q1-arraya1
abserrd=q1-arraya2

abserra= q1-arraya 
abserrb= q1-arrayap 
conv = abserrb/abserra

xco= linspace(-2,6,100)



xlabel(r'x')
ylabel('Absolute Error')
p1,=plot(xco, abserra,'r', linewidth=2)
p2,=plot(xco, abserrb, 'b', linewidth=2)
legend((p1,p2),("h=1","h=.5"),loc=(0.7,0.85), frameon=False)
text(0.05,0.2,"Absolute Error: Forward Difference",fontsize=16,
        horizontalalignment="left",rotation="horizontal",
        transform=ax.transAxes)
draw()
raw_input()
#creates as two separate figures
figure()
xlabel(r'x')
ylabel('Absolute Error')
p1,=plot(xco, abserrc,'r', linewidth=2)
p2,=plot(xco, abserrd, 'b', linewidth=2)
legend((p1,p2),("h=1","h=.5"),loc=(0.7,0.75), frameon=False)
text(0.2,0.5,"Absolute Error: Central Difference",fontsize=16,
        horizontalalignment="left",rotation="horizontal",
        transform=ax.transAxes)
draw()
raw_input()
figure()
xlabel(r'x')
ylabel('Derivative')
p1,=plot(xco, arraya1,'r', linewidth=2)
p2,=plot(xco, arraya, 'b', linewidth=2)
legend((p1,p2),("Central Derivative, $h=1$","Forward Derivative, $h=1$"),loc=(0.34,0.5), frameon=False)
text(0.3,0.9,"Derivative Estimates",fontsize=16,
        horizontalalignment="left",rotation="horizontal",
        transform=ax.transAxes)
draw()
show()


