from numpy import *

p=365.25635 #days
w=2*pi/p
t=273 #days
e=.99999
a=1 #AU
b=0.00447212477463 #AU

def f(E): return E-w*t-e*sin(E)
def df(E): return 1-e*cos(E)
    
def rootf(E,h=1.0*10**-10):
    for i in range(500):
        dE=f(E)/df(E)
        E=E-dE
        if abs(f(E))<h: return E,i
  
root,numiter=rootf(.1)
print "Root=",root
print "Number of iterations=",numiter


