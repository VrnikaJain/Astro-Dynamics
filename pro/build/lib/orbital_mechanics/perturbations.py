import numpy as np

def atmospheric_drag(r, v, Cd, A, m, rho0=1.225, H=8500):
    """
    Calculate acceleration due to atmospheric drag.
    
    Parameters:
    r (float): Altitude above Earth's surface (km)
    v (float): Velocity (km/s)
    Cd (float): Drag coefficient
    A (float): Cross-sectional area (m^2)
    m (float): Mass (kg)
    rho0 (float): Sea-level atmospheric density (kg/m^3), default is 1.225
    H (float): Scale height (m), default is 8500
    
    Returns:
    float: Acceleration due to drag (km/s^2)
    """
    rho = rho0 * np.exp(-r * 1000 / H)  # Convert r to meters
    drag = 0.5 * Cd * A * rho * (v * 1000)**2 / m  # Convert v to m/s
    return drag / 1000  # Convert to km/s^2

def gravitational_perturbation(r, mu=398600, J2=1.08263e-3, Re=6371):
    """
    Calculate acceleration due to J2 gravitational perturbation.
    
    Parameters:
    r (numpy.ndarray): Position vector (km)
    mu (float): Gravitational parameter (km^3/s^2), default is Earth's
    J2 (float): Second zonal harmonic of Earth's gravitational potential
    Re (float): Earth's radius (km)
    
    Returns:
    numpy.ndarray: Acceleration due to J2 perturbation (km/s^2)
    """
    x, y, z = r
    r_mag = np.linalg.norm(r)
    factor = (3/2) * J2 * mu * Re**2 / r_mag**5

    ax = factor * x / r_mag * (5 * (z**2 / r_mag**2) - 1)
    ay = factor * y / r_mag * (5 * (z**2 / r_mag**2) - 1)
    az = factor * z / r_mag * (5 * (z**2 / r_mag**2) - 3)
    
    return np.array([ax, ay, az])

if __name__ == "__main__":
    r = 700  # km
    v = 7.8  # km/s
    Cd = 2.2
    A = 10  # m^2
    m = 1000  # kg

    drag_acceleration = atmospheric_drag(r, v, Cd, A, m)
    print(f"Acceleration due to drag: {drag_acceleration} km/s^2")

    position = np.array([7000, 0, 0])  # km
    j2_perturbation = gravitational_perturbation(position)
    print(f"J2 perturbation acceleration: {j2_perturbation} km/s^2")
