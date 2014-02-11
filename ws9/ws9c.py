
import numpy
import scipy.linalg
import time


A=numpy.loadtxt("/home/davidvartanyan/Desktop/LSE5_m.dat")
B=numpy.loadtxt("/home/davidvartanyan/Desktop/LSE5_bvec.dat")

#A = numpy.array([[3.,2.,-1.],[-1.,3.,2.],[1.,-1.,-1.]])
#B = numpy.array([10,5,-1])

start = time.clock()
X = scipy.linalg.solve(A, B)
finish = time.clock()
print 'time for solution is ', finish - start,'s'
print 'residual', scipy.linalg.norm(numpy.dot(A, X) - B)/scipy.linalg.norm(A)
#print X
#print numpy.c_[A,B]