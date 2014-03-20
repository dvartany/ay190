import numpy as np

ggrav = 6.67e-8

def NbodyRHS(u,mass,time):
    v = np.zeros(u.shape)
    v[:,0:3] = u[:,3:]
    for i in range(0,len(mass)):
        deltaxyz = u[i,0:3] - u[:,0:3]
        r = np.sqrt(np.sum(deltaxyz*deltaxyz,axis=1))
        r[i] = -1 # avoids divivision by zero
        v[i,3] = -ggrav * np.sum(deltaxyz[:,0] * mass/(r**3))
        v[i,4] = -ggrav * np.sum(deltaxyz[:,1] * mass/(r**3))
        v[i,5] = -ggrav * np.sum(deltaxyz[:,2] * mass/(r**3))
    return v

def NbodyRHS2(u,mass): #used with leapfrog
    v = np.zeros(u.shape)
    for i in range(0,len(mass)):
        deltaxyz = u[i,0:3] - u[:,0:3]
        r = np.sqrt(np.sum(deltaxyz*deltaxyz,axis=1))
        r[i] = -1 # avoids divivision by zero
        v[i,0] = -ggrav * np.sum(deltaxyz[:,0] * mass/(r**3))
        v[i,1] = -ggrav * np.sum(deltaxyz[:,1] * mass/(r**3))
        v[i,2] = -ggrav * np.sum(deltaxyz[:,2] * mass/(r**3))
    return v
    
def NbodyRK4(u,mass,time,dt):
    k1 = NbodyRHS(u,mass,time)
    k2 = NbodyRHS(u+0.5*dt*k1,mass,time)
    k3 = NbodyRHS(u+0.5*dt*k2,mass,time)
    k4 = NbodyRHS(u+dt*k3,mass,time)
    return u+dt/6.*(k1+2*k2+2*k3+k4)
    
def leapfrog(u, mass, dt):
    x_old = u[:,0]
    y_old = u[:,1]
    z_old = u[:,2]
    vx_old = u[:,3]
    vy_old = u[:,4]
    vz_old = u[:,5]
    
    u_new = np.zeros(np.shape(u))
    
    # Calculate acceleration based on the position now
    acc_now = NbodyRHS2(u[:,0:3],mass)
    acc_nx = acc_now[:,0]
    acc_ny = acc_now[:,1]
    acc_nz = acc_now[:,2]
    
    # Calculate the new position
    x_new = x_old + vx_old*dt + 0.5*acc_nx*dt*dt
    y_new = y_old + vy_old*dt + 0.5*acc_ny*dt*dt
    z_new = z_old + vz_old*dt + 0.5*acc_nz*dt*dt
    
    # Assign the new position into the new u array
    u_new[:,0] = x_new
    u_new[:,1] = y_new
    u_new[:,2] = z_new
    
    # Calculate acceleration based on the new position
    acc_future = NbodyRHS2(u_new[:,0:3],mass)
    acc_fx = acc_future[:,0]
    acc_fy = acc_future[:,1]
    acc_fz = acc_future[:,2]
    
    # Calculate the new velocity
    vx_new = vx_old + 0.5*(acc_nx+acc_fx)*dt
    vy_new = vy_old + 0.5*(acc_ny+acc_fy)*dt
    vz_new = vz_old + 0.5*(acc_nz+acc_fz)*dt
    
    # Assign the new velocity into the new u array
    u_new[:,3] = vx_new
    u_new[:,4] = vy_new
    u_new[:,5] = vz_new
    
    return u_new