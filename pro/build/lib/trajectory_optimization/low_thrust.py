import numpy as np
from scipy.integrate import solve_ivp

def low_thrust_trajectory(r0, v0, thrust, isp, mass, t_span, mu=398600):
    """
    Calculate low-thrust trajectory.
    
    Parameters:
    r0 (numpy.ndarray): Initial position vector (km)
    v0 (numpy.ndarray): Initial velocity vector (km/s)
    thrust (float): Thrust (N)
    isp (float): Specific impulse (s)
    mass (float): Initial mass (kg)
    t_span (tuple): Time span for integration (s)
    mu (float): Gravitational parameter (km^3/s^2), default is Earth's
    
    Returns:
    dict: Solution with time, position, and velocity
    """
    g0 = 9.80665  # Standard gravitational acceleration (m/s^2)
    
    def equations(t, y):
        r = y[:3]
        v = y[3:6]
        m = y[6]
        
        r_norm = np.linalg.norm(r)
        a_gravity = -mu * r / r_norm**3
        a_thrust = thrust / m * (v / np.linalg.norm(v))
        
        drdt = v
        dvdt = a_gravity + a_thrust
        dmdt = -thrust / (isp * g0)
        
        return np.concatenate((drdt, dvdt, [dmdt]))
    
    y0 = np.concatenate((r0, v0, [mass]))
    sol = solve_ivp(equations, t_span, y0, rtol=1e-9, atol=1e-9)
    
    return sol

if __name__ == "__main__":
    r0 = np.array([7000, 0, 0])  # km
    v0 = np.array([0, 7.8, 0])  # km/s
    thrust = 0.01  # N
    isp = 3000  # s
    mass = 500  # kg
    t_span = (0, 86400)  # 1 day in seconds

    trajectory = low_thrust_trajectory(r0, v0, thrust, isp, mass, t_span)
    print(f"Trajectory time points: {trajectory.t}")
    print(f"Final position: {trajectory.y[:3, -1]} km")
    print(f"Final velocity: {trajectory.y[3:6, -1]} km/s")
    print(f"Final mass: {trajectory.y[6, -1]} kg")
