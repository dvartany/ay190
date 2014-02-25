#!/usr/bin/env python

import numpy as np
import scipy as sp
import matplotlib.pyplot as plt
import mpl_toolkits.mplot3d as mpl3d

# global constants
ggrav = 6.67e-8
msun  = 1.99e33
seconds_per_year = 24.*3600*365 # roughly
cm_per_pc = 3.1e18
distance_to_sgrAstar = 8e3 * cm_per_pc

#sun-earth
#system parameters
initial_data_file = "sun_earth.asc"
distance_unit_to_cm = 1.
time_unit_to_s = 1.
mass_unit_to_g = 1.

#sgrAstars
initial_data_file = "sgrAstar.asc"
time_unit_to_s= seconds_per_year #data in years
mass_unit_to_g=msun #data in solar masses
distance_unit_to_cm= 1.0/3600.* np.pi/180.0*distance_to_sgrAstar #arcsec to degrees to radians

Nsteps = 10000
t0 = 0
t1 = 5*seconds_per_year #100*... for sgrAstar
dt = (t1-t0)/Nsteps

final_data_file = "final_positions.asc"

def NbodyRHS(u,mass,time):
    #rhs is a matrix of shape u. 0th column is vx, 1st vy, 2nd vz
    rhs=np.zeros(np.shape(u))
    rhs[:,0]=u[:,3]
    rhs[:,1]=u[:,4]
    rhs[:,2]=u[:,5]
    rhs[:,3:6]=0
    for i in range(len(u[:,1])):
        for j in range(len(u[:,1])):
            if j==i: #i!=j
                continue
            xij=np.array([u[j][0]-u[i][0],u[j][1]-u[i][1],u[j][2]-u[i][2]])  
            mod=np.sqrt(xij[0]**2 + xij[1]**2+xij[2]**2)
            rhs[i,3:6] += -ggrav*mass[j]*xij/mod**3
            
    return rhs
    # [ fill in code ]

def NbodyRK2(u,mass,time,dt):
    k1=dt*NbodyRHS(u, mass, time)
    k2=dt*NbodyRHS(u+0.5*k1, mass, time+0.5*dt)
    unew=u+k2
    return unew
    # [ fill in code ]

def TotalEnergy(u,mass,time):
    Ekin=0
    Epot=0
    for i in range(len(u[:,1])):
        Ekin+=.5*mass[i]*(u[i][3]**2+u[i][4]**2+u[i][5]**2)
    for i in range(len(u[:,1])):
        for j in range(len(u[:,1])):
            if j==i:
                continue
            xij=np.array([u[j][0]-u[i][0],u[j][1]-u[i][1],u[j][2]-u[i][2]])  
            mod=np.sqrt(xij[0]**2 + xij[1]**2+xij[2]**2)
            Epot+=-ggrav*mass[i]*mass[j]/(mod)
    energy=Epot+Ekin
    return energy
    # [ fill in code ]

# main program
#plt.ion()

(x,y,z,vx,vy,vz,mass) = np.loadtxt(initial_data_file, unpack = True)


# convert from unitis in initial data file to cgs
x *= distance_unit_to_cm
y *= distance_unit_to_cm
z *= distance_unit_to_cm
vx *= distance_unit_to_cm / time_unit_to_s
vy *= distance_unit_to_cm / time_unit_to_s
vz *= distance_unit_to_cm / time_unit_to_s
mass *= mass_unit_to_g

xmin = np.amin(x)
xmax = np.amax(x)
ymin = np.amin(y)
ymax = np.amax(y)
zmin = np.amin(z)
zmax = np.amax(z)
rmax = 2.5*max(abs(xmin),abs(xmax),abs(ymin),abs(ymax),abs(zmin),abs(zmax))

# use a single state vector to simplify the ODE code
# indices:
# u[:,0] = x
# u[:,1] = y
# u[:,2] = z
# u[:,3] = vx
# u[:,4] = vy
# u[:,5] = vz
u = np.array((x,y,z,vx,vy,vz)).transpose()
for it in range(0, Nsteps):
    time = t0 + it * dt
    u = NbodyRK2(u,mass,time,dt)
    
    if it % max(1,Nsteps/100) == 0:
      print "it = %d, time = %g years, energy = %g" % \
            (it, time / seconds_per_year,
             TotalEnergy(u,mass,time))
      plt.clf()
      fig = plt.gcf()
      ax = mpl3d.Axes3D(fig)
      ax.scatter(u[:,0],u[:,1],u[:,2])
      ax.set_xlim((-rmax,rmax))
      ax.set_ylim((-rmax,rmax))
      ax.set_zlim((-rmax,rmax))
      plt.draw()


# output result
#file_header = "1:x 2:y 3:z 4:vx 5:vy 6:vz 7:mass"
#np.savetxt(final_data_file, u)
