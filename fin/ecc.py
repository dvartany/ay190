import numpy as np
import Integrator as Int
import Project_Lib as Lib
import matplotlib.pyplot as pl

# global constants
ggrav = 6.67e-8
msun = 1.99e33
mearth = 5.97e27
mmoon = 7.342e25
au = 1.5e13
dmoon = 3.844e10
seconds_per_year = 24.*3600*365

# Set up array of initial inclination
theta = np.array([0.,10.,20.,30.,45.,
                  55.,65.,80.,90.])
# Convert it into radian
theta *= np.pi/180.

max_ecc = np.zeros(len(theta))

for it in range(len(theta)):
    # system parameters
    Nsteps = 50000
    t0 = 0
    t1 =18* seconds_per_year
    dt = (t1-t0)/Nsteps
    t = np.linspace(t0, t1, num = Nsteps)

    # setup initial parameters for the system
    mass = np.array([msun, mearth, mmoon])
    x = np.zeros(3)
    y = np.zeros(3)
    z = np.zeros(3)
    vx = np.zeros(3)
    vy = np.zeros(3)
    vz = np.zeros(3)
    
    # Put both Earth and moon at perigee
    x[0] = 0.*au # Sun
    x[1] = 1.*au # Earth
    x[2] = x[1] + dmoon*np.cos(theta[it]) # Put moon at theta inclination
    z[2] = dmoon*np.sin(theta[it])
    
    vy[0] = 0.
    vy[1] = np.sqrt(ggrav*msun/au)
    vy[2] = np.sqrt(ggrav*mearth/dmoon) + vy[1]
    
    u = np.array((x,y,z,vx,vy,vz)).transpose()
    
    # Array recording distance between Earth-Moon
    dist = np.zeros(Nsteps)
    dist[0] = Lib.CalDistEM(u)
    
    for i in range(1, Nsteps):
        print i, "and", it
        time = t0 + i*dt
        u = Int.NbodyRK4(u, mass, time, dt)

        dist[i] = Lib.CalDistEM(u)
    
    # Use helper function to calculate eccentricity
    ecc = Lib.CalEccMoon(dist,t)
    max_ecc[it] = np.max(ecc)

np.savetxt('max_ecc.dat', max_ecc)

#pl.plot(t/seconds_per_year, dist, 'b-')
#pl.show()

pl.plot(theta*180./np.pi, max_ecc, 'ro')
pl.xlabel("Initial Inclination (deg)")
pl.ylabel("Max Eccentricity")
pl.yscale('log')
pl.savefig('ecc5.pdf')
