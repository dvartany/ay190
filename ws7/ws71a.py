import numpy as np
import random
import matplotlib.pyplot as plt

sr=random.SystemRandom()
r=sr.random()


    
def rngen(N):
    n=0
    x=np.asarray([sr.random()-.5 for i in range(N)])
    y=np.asarray([sr.random()-.5 for i in range(N)])
    r=x**2+y**2
    for i in r:
        if i < .5**2:
            n+=1
    
    return n
N=10000

x=np.asarray([sr.random()-.5 for i in range(N)])
y=np.asarray([sr.random()-.5 for i in range(N)])
print rngen(N)*4./N

err= [np.abs(np.pi-rngen(N)*4./N) for N in range(1,10000,100)]
t=np.linspace(1,10000,100)
ax=plt.gca()
plt.text(.5,0.90,'System.Random Error vs Sample Size',
        horizontalalignment='center',transform=ax.transAxes, fontsize=22)

plt.plot(np.log10(t),err)
plt.xlabel(r'Log(N)')
plt.ylabel(r'Error')
plt.show()