import numpy as np

def kepler_orbit(semi_major_axis, eccentricity, true_anomaly):
    """
    Calculate the radius at a given true anomaly for an elliptical orbit.
    
    Parameters:
    semi_major_axis (float): Semi-major axis of the orbit (km)
    eccentricity (float): Eccentricity of the orbit
    true_anomaly (float): True anomaly (radians)
    
    Returns:
    float: Radius (km)
    """
    mu = 398600  # Standard gravitational parameter for Earth (km^3/s^2)
    
    r = (semi_major_axis * (1 - eccentricity ** 2)) / (1 + eccentricity * np.cos(true_anomaly))
    
    return r

if __name__ == "__main__":
    semi_major_axis = 7000  # in km
    eccentricity = 0.1
    true_anomaly = np.radians(45)  # converting degrees to radians

    distance = kepler_orbit(semi_major_axis, eccentricity, true_anomaly)
    print(f"Distance from the focal point: {distance} km")
