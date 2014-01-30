import pylab
from numpy import *
from matplotlib.pyplot import *
i=1.j
    
N=100

def w(N):
    return exp(-2*pi*i/N)
k=range(0,N)

b=([(w(N)**k)**z for z in range(0,N)])

def f(x):
    return [dot(b[s],x) for s in range(N)]

#h=pylab.randn(N)
def g(x):
    return fft.fft(x)
#print dot(b[1],x[1])
#print asarray(f(h))
#print fft.fft(h)

from timeit import timeit


#print timeit("f(x)", number=10, setup="from __main__ import f; import pylab; x=pylab.randn(%d)" % N)
print timeit("g(x)", number=10, setup="from __main__ import g; import pylab; x=pylab.randn(%d)" % N)


myfy=[0.000142097473145,0.000245094299316,0.000411033630371,0.000541210174561,0.000643968582153,0.000773906707764,0.00119590759277,0.00136017799377,0.00138807296753,0.00160479545593]
ffty=[7.00950622559e-05,7.20024108887e-05, 7.39097595215e-05, 7.58171081543e-05,7.60555267334e-05, 7.9870223999e-05, 8.20159912109e-05, 8.48770141602e-05, 8.70227813721e-05, 9.20295715332e-05]
z=range(10,110,10)

ax = gca()
text(.5,0.90,'Time to Run vs N',
        horizontalalignment='center',transform=ax.transAxes, fontsize=22)

ylabel(r'Time[s]')
xlabel(r'N')
p1,=plot(z, myfy, 'k')

twinx()
tick_params(axis="y", labelcolor="b")
p2,=plot(z,ffty, 'b')

legend((p1,p2),("myfy","numpy.fft"),loc=(0.7,0.1), frameon=False)


show()
