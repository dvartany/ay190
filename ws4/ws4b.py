from numpy import *


p=365.25635 #days
w=2*pi/p
t=273#days
e=.99999
a=1 #AU
b=0.00447212477463 #AU


def f(E): return E-w*t-e*sin(E)
def df(E): return 1-e*cos(E)
    
def rootf(E,h):
    n=0
    
    while True:
        dE=f(E)/df(E)
        E_new=E-dE
        relative_error=abs((f(E_new)-f(E))/f(E))
        if relative_error<h:
            return E,n
        E=E_new
        n+=1

def x(E):
    return a*cos(E)
def y(E):
    return b*sin(E)

print rootf(.1,10**-10), x(rootf(.1,10**-10)[0]), y(rootf(.1,10**-10)[0])