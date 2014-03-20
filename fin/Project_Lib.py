import numpy as np
ggrav=6.67e-8

def TotalEnergy(u,mass,time):
    (x,y,z,vx,vy,vz) = u.transpose()
    v2 = vx**2+vy**2+vz**2
    Ekin = 0.5*np.sum(mass*v2)
    Egrav = 0.
    for i in range(0,len(mass)):
        deltax = x[i] - x
        deltay = y[i] - y
        deltaz = z[i] - z
        r = np.sqrt(deltax**2 + deltay**2 + deltaz**2)
        r[i] = 1e300 # avoids division by zero
        Egrav += - ggrav * mass[i] * np.sum(mass/r)
    return Ekin + Egrav

def CalDistEM(u):
    '''
Calculate distance between Earth and Moon
'''
    xearth = u[1,0]
    xmoon = u[2,0]
    yearth = u[1,1]
    ymoon = u[2,1]
    zearth = u[1,2]
    zmoon = u[2,2]
    
    return np.sqrt((xearth-xmoon)**2+(yearth-ymoon)**2+(zearth-zmoon)**2)

def CalEccMoon(dist, time):
    '''
Calculate eccentricity based on apogee and perigee of each cycle.
Assuming the orbital period of the moon is 27 days.
'''
    period = 27*24*3600 # 27 days in second
    t0 = time[0]
    t1 = t0 + period
    ini = 0
    
    ecc = np.array([])
    for i in range(len(time)):
        if time[i] > t1:
            r_a = np.max(dist[ini:i])
            r_p = np.min(dist[ini:i])
            ecc = np.append(ecc, (r_a-r_p)/(r_a+r_p))
            
            ini = i
            t1 += period
        if t1 > time[-1]:
            break
    return ecc