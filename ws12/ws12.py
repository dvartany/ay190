import numpy as np
from matplotlib.pyplot import *
from scipy import interpolate

dat=np.loadtxt("/home/davidvartanyan/presupernova.dat")
rad=dat[:,2]
rho1=dat[:,4]
i=0
while rad[i]/10**9 < 1:
    i+=1
xlim([rad[0],rad[i]])
#loglog(rad[0:i],rho1[0:i],'k')
npoints=1000
radmin=rad[0]
radmax=10**9
radius=np.linspace(0.1,
                   radmax,npoints)
dr=radius[1]-radius[0]

tck = interpolate.splrep(rad,rho1)
rho2= interpolate.splev(radius,tck,der=0)

#xlabel('radius [$cm$]')
#ylabel('Density [$g/cm^3$]')
#show()



ggrav = 6.67e-8

#######################################
# function definitions
def tov_RHS(x,rho,z):
    
    # RHS function
    
    rhs = np.zeros(2)
    rhs[0] = z
    rhs[1] = 4*np.pi*ggrav*rho- 2*z/x
    
    return rhs

def tov_integrate_FE(rad,dr,rho,z,phi):

    # Forward-Euler Integrator

    new = np.zeros(2)
    old = np.zeros(2)
    old[0] = phi #dphi/dr-> phi
    old[1] = z #dz/dr -> z

    # forward Euler integrator
    new = old + dr*tov_RHS(rad, rho, z)
    
    # assign outputs
    phinew = new[0]
    znew = new[1]
    
    return (phinew,znew)

#######################################
# set up variables
z1f   = np.zeros(npoints)
phif  = np.zeros(npoints)
# set up boundary values
z1f[0] = 0.0
phif[0] = 0.0

for n in range(npoints-1):
    
    (phif[n+1],z1f[n+1]) = tov_integrate_FE(radius[n],
                                              dr,rho2[n],z1f[n],phif[n])
dm=4*np.pi*radius**2*rho2*dr
M=np.sum(dm)


phiBC2=-ggrav*M/radius[npoints-1]

phiana=2./3*np.pi*ggrav*rho2*(radius**2-3*((10**9.)**2))
phifin=phif+phiBC2-phif[npoints-1]

#p1,=loglog(radius,-phifin)
#p2,=loglog(radius,-phiana)
xlabel('radius[cm]')
#ylabel('Phi')
#legend([p1,p2], ['Numerical Potential', 'Analytical Potential'])
ylabel('Error')
loglog(radius,np.abs((phiana-phifin)/phiana))
show()

#radmax2=np.asarray([10**9]*len(radius))
#origin=np.asarray([4.2118*10**20]*len(radius))
#plot(radius,phif+origin)

#print .67*np.pi*ggrav*rho2*(radius**2-3*radmax2**2)
#print  -0.67*np.pi*ggrav*rho2*(radius**2-3*radmax2**2)