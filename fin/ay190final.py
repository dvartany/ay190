#!/usr/bin/env python

import numpy as np
import matplotlib.pyplot as plt
import mpl_toolkits.mplot3d as mpl3d
from Integrator import *
from Project_Lib import *
# global constants
ggrav = 6.67e-8
msun = 1.99e33
seconds_per_year = 24.*3600*365 # roughly
cm_per_pc = 3.1e18


#sun-earth
# system parameters
initial_data_file = "sun_earthecc.asc" #semoon, sun_earth, sun_earthecc
distance_unit_to_cm = 1.
time_unit_to_s = 1. 
mass_unit_to_g = 1.

Nsteps = 4e3
t0 = 0
t1 = 80*seconds_per_year #adjust with Nsteps for resolution
dt = (t1-t0)/Nsteps

final_data_file = "final_positions.asc"
    
# main program
plt.ion()

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
u= np.array((x,y,z,vx,vy,vz)).transpose()
u_RK4= np.array((x,y,z,vx,vy,vz)).transpose()
u_LF=np.array((x,y,z,vx,vy,vz)).transpose()
r_orbE=np.zeros(Nsteps)
r_orbm=np.zeros(Nsteps)
E_RK4=np.zeros(Nsteps)
E_LF=np.zeros(Nsteps)
t=np.zeros(Nsteps)
ufin=np.zeros((np.shape(u)[0],np.shape(u)[1],Nsteps))

for it in range(0, int(Nsteps)):
    time = t0 + it * dt
    #u= NbodyRK4(u,mass,time,dt)
    u=NbodyRK4(u,mass,time,dt)
    #u_LF=leapfrog(u_LF,mass,dt)
    u_RK4=NbodyRK4(u_RK4,mass,time,dt)
    t[it]=time
    E_RK4[it]=TotalEnergy(u_RK4,mass,time)
    #E_LF[it]=TotalEnergy(u_LF,mass,time)
    #r_orbE[it]=(u[1][0]**2+u[1][1]**2+u[1][2]**2)**0.5
    #r_orbm[it]=(u[2][0]**2+u[2][1]**2+u[2][2]**2)**0.5
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
    ufin[:,:,it]=u  
#plot orbit


#plot orbital radius vs time
#plt.clf()
#t=np.linspace(t0,t1,Nsteps)
#plt.plot(t/seconds_per_year,(r_orbm-r_orbE),'k')
#plt.xlabel('Time [years]',fontsize=20)
#plt.ylabel('Moon Orbital Radius [cm]',fontsize=20)
#plt.savefig('moonorb.pdf')

##################
#calculate eccentricity (only for Earth-moon system with 0 inclination)
#xs,ys,zs=ufin[2,0]-ufin[1,0],ufin[2,1]-ufin[1,1],ufin[2,2]-ufin[1,2]
#a,b=np.max(np.sqrt(xs**2+ys**2+zs**2)),np.min(np.sqrt(xs**2+ys**2+zs**2))
#print (a-b)/(a+b)

##################
#plot 3D orbits
#plt.clf()
#fig = plt.figure()
#ax = fig.gca(projection='3d')
#ax.set_xlim((-rmax,rmax))
#ax.set_ylim((-rmax,rmax))
#ax.set_zlim((-rmax,rmax))
#for i in range(np.shape(ufin)[0]):
#    ax.plot(xs,ys,zs)
#plt.draw()
#plt.savefig('final_orbits.pdf')

###################
#plot energy errors for different integrators
plt.clf()
p1,=plt.plot(t/seconds_per_year,np.abs((E_RK4-E_RK4[0])/E_RK4[0]),'k')
#p2,=plt.plot(t/seconds_per_year,np.abs((E_LF-E_LF[0])/E_LF[0]))
plt.xlabel('Time [years]',fontsize=20)
plt.ylabel('Energy Error[ergs]',fontsize=20)
plt.yscale("log")
plt.xlim(0,80)
#plt.legend((p1,p2),("RK4","LF"),loc=(0.,0.),frameon=False)
plt.savefig('E_4e3ecc.pdf')
#file_header = "1:x 2:y 3:z 4:vx 5:vy 6:vz 7:mass"
#np.savetxt(final_data_file, u, header=file_header)


        