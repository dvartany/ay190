import numpy as np
import scipy as sp
import matplotlib.pyplot as plt
import sys

# global constants
ggrav = 6.67e-8
msun  = 1.99e33

# EOS parameters
# for white dwarfs:
polyG = 4.0/3.0
polyK = 1.244e15*0.5**polyG


#######################################
# function definitions
def tov_RHS(rad,rho,m):
    
    # RHS function
    
    rhs = np.zeros(2)
    if(rad > 1.0e-10):
        rhs[0] = -ggrav*m*rho/rad**2
        rhs[1] = 4*np.pi*rho*rad**2
    else:
        rhs[0] = 0.0
        rhs[1] = 0.0

    return rhs

def P2rho(pressure):
    return (pressure/polyK)**(1.0/polyG)



def tov_integrate_FE(rad,h,p,rho,m):

    # RK2 integrator

    new = np.zeros(2)
    old = np.zeros(2)
    old[0] = p
    old[1] = m

    # 
    k1 = h*tov_RHS(rad,rho,m)
    k2 = h * tov_RHS(rad+.5*h,P2rho(p+.5*k1[0]),m+.5*k1[0])
    #k2[1] = dr * tov_RHS(rad+.5*dr,P2rho(p+.5*k1[0]),m+.5*k1[1])[1]
    new = old + k2

    
    # assign outputs
    pnew = new[0]
    mnew = new[1]
    
    return (pnew,mnew)

#######################################

# set up grid
npoints = 1000
radmax = 2.0e8 # 2000 km
radius = np.linspace(0, radmax, npoints)
h = radius[1]-radius[0]

# set up variables
press = np.zeros(npoints)
rho   = np.zeros(npoints)
mass  = np.zeros(npoints)

# set up central values
rho[0]   = 1.0e10
press[0] = polyK * rho[0]**polyG
mass[0]  = 0.0

# set up termination criterion
press_min = 1.0e-10 * press[0]

nsurf = 0
for n in range(npoints-1):
    
    (press[n+1],mass[n+1]) = tov_integrate_FE(radius[n],
                                              h,
                                              press[n],
                                              rho[n],mass[n])
    # check for termination criterion
    if(press[n+1] < press_min and nsurf==0):
        nsurf = n

    if(n+1 > nsurf and nsurf > 0):
        press[n+1] = press[nsurf]
        rho[n+1]   = rho[nsurf]
        mass[n+1]  = mass[nsurf]

    # invert the EOS to get density
    rho[n+1] = (press[n+1]/polyK)**(1/polyG)

print radius[nsurf]/1.0e5
print mass[nsurf]/msun
plt.xlabel("Radius[cm]")
plt.ylabel(r'$P/P_c$,  $\rho/\rho_c$')
p1,=plt.plot(radius,rho/rho[0],'r')
p2,=plt.plot(radius,mass/mass[999],'b')
plt.twinx()
plt.ylabel("$M/M_{tot}$",color="b")
p3,=plt.plot(radius,press/press[0],'g')
plt.legend((p1,p2,p3),("Density", "Mass","Pressure"),loc=(0.34,0.5), frameon=False)
plt.show()