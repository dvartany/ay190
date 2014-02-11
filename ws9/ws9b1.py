#print("Importing...")
from numpy import *
#print("Running...")
import time
#define coefficient constant arrays
A=loadtxt("/home/davidvartanyan/Desktop/LSE1_m.dat")
B=loadtxt("/home/davidvartanyan/Desktop/LSE1_bvec.dat")
a=c_[A,B]
 
#creates arrays to use in the for() loops
rows=a.shape[0]
columns=a.shape[1]
answer=zeros(rows)
 
print("-----")

start = time.clock()
 
#eliminate variables
for i in arange(0,columns): #variable to eliminate
   for j in arange(i+1,rows): #rows to eliminate said variable from
     tmp=a[i]*(-a[j][i]/a[i][i]) #multiply row
     a[j]=tmp+a[j] #add
 

#back substitute
for i in (arange(rows).shape[0]-arange(rows)-1):
 
   #subtract terms
   if(i<columns-2):
     a[i][columns-1]=a[i][columns-1]-(sum(a[i])-a[i][i]-a[i][columns-1])
 
   #calculate ith variable
   answer[i]=a[i][columns-1]/(a[i][i])
   #substitute variable by
   #multiply rows starting with i-1, column i by answer[i]
   for j in arange(0,i):
     a[j][i]=a[j][i]*answer[i]

finish= time.clock() 
#print out the answer 
#print(answer)

print 'time for solution is ', finish - start,'s'