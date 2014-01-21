from numpy import *
from scipy import special as sp

[legendre_roots,legendre_weights]=sp.p_roots(2,0)

#create intervals dE=5
t= linspace(0,150, 31.)

#from Wolfram Alpha
k=20#in 1/MeV
h=1.97327*10**-11 #in Mev cm


#define our integrad with change of variables
def f(x,n):
    return 2.5*(2.5*x+.5*(t[int(n)]+t[int(n+1)]))**2./(exp(.05*(2.5*x+.5*(t[int(n)]+t[int(n+1)])))+1)

#convert to 31xn dimensional array whose ith element is the ith integral in (0,150,31)
z=[]
for i in linspace(0,29,30):
    z.extend([f(legendre_roots,i)])    

#sum over rows and columns
b1=sum(z,axis=0)
c1=sum(b1,axis=0)

print sum(legendre_weights*b1)