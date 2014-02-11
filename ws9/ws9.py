from numpy import *

datA1=loadtxt("/home/davidvartanyan/Desktop/LSE4_m.dat")
datb1=loadtxt("/home/davidvartanyan/Desktop/LSE4_bvec.dat")
print "determinant sign and natural log..."
print linalg.slogdet(datA1)
#print linalg.det(datA1)
a= array([len(datA1[i]) for i in range(len(datA1))])

print "Checking for squareness..."
for i in range(len(datA1)):
    if a[i] != len(datA1):
        print "False"
  
print "What a square of length..."
print len(datA1)