import numpy as np
import numpy.random as random
import matplotlib.pyplot as plt

random.seed(1)
r=random.rand()

#r=1
def rngen(N):
    n=0
    x,y=np.array([]),np.array([])
    #for i in range(n)    
    x=np.append(x,[random.rand(N)-.5])
    y=np.append(y,[random.rand(N)-.5])

    r=x**2+y**2
    for i in r:
        if i < .5**2:
            n+=1
    
    return n
    
x,y=np.array([]),np.array([])
x=np.append(x,[random.rand(10)-.5])
y=np.append(y,[random.rand(10)-.5])

N=10000
print rngen(N)*4./N

err= [np.pi-rngen(N)*4./N for N in np.linspace(1,10000,100)]
x=np.linspace(1,10000,100)
ax=plt.gca()
plt.text(.5,0.90,'Error vs Sample Size',
        horizontalalignment='center',transform=ax.transAxes, fontsize=22)

plt.plot(np.log10(x),err)
plt.xlabel(r'Log(N)')
plt.ylabel(r'Error')
plt.show()
