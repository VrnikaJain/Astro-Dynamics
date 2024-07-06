import numpy as np

def hohmann_transfer(r1, r2, mu=398600):
    """
    Calculate delta-v for a Hohmann transfer between two circular orbits.
    
    Parameters:
    r1 (float): Radius of the initial orbit (km)
    r2 (float): Radius of the final orbit (km)
    mu (float): Gravitational parameter (km^3/s^2), default is Earth's
    
    Returns:
    tuple: Delta-v1 and Delta-v2 for the transfer (km/s)
    """
    v1_initial = np.sqrt(mu / r1)
    v2_final = np.sqrt(mu / r2)

    v_transfer_1 = np.sqrt(mu * ((2 / r1) - (1 / ((r1 + r2) / 2))))
    v_transfer_2 = np.sqrt(mu * ((2 / r2) - (1 / ((r1 + r2) / 2))))

    delta_v1 = v_transfer_1 - v1_initial
    delta_v2 = v2_final - v_transfer_2

    return delta_v1, delta_v2

def rendezvous(initial_orbit_radius, target_orbit_radius, phase_angle, mu=398600):
    """
    Calculate delta-v for a rendezvous maneuver using Hohmann transfer.
    
    Parameters:
    initial_orbit_radius (float): Radius of the initial orbit (km)
    target_orbit_radius (float): Radius of the target orbit (km)
    phase_angle (float): Phase angle between the spacecraft and the target (degrees)
    mu (float): Gravitational parameter (km^3/s^2), default is Earth's
    
    Returns:
    tuple: Delta-v1, Delta-v2 for the transfer (km/s) and time to wait (seconds)
    """
    delta_v1, delta_v2 = hohmann_transfer(initial_orbit_radius, target_orbit_radius)
    
    transfer_time = np.pi * np.sqrt(((initial_orbit_radius + target_orbit_radius) / 2)**3 / mu)
    angular_velocity_initial = np.sqrt(mu / initial_orbit_radius**3)
    angular_velocity_target = np.sqrt(mu / target_orbit_radius**3)
    
    required_phase_angle = angular_velocity_target * transfer_time
    required_phase_angle_deg = np.degrees(required_phase_angle)
    
    if required_phase_angle_deg > phase_angle:
        # Calculate time to wait to achieve the correct phase angle
        angular_difference = required_phase_angle - np.radians(phase_angle)
        time_to_wait = angular_difference / (angular_velocity_initial - angular_velocity_target)
        print(f"Phase angle too large for direct Hohmann transfer. Required: {required_phase_angle_deg:.2f}°, Given: {phase_angle:.2f}°")
        print(f"Wait approximately {time_to_wait / 3600:.2f} hours to achieve the correct phase angle.")
        return delta_v1, delta_v2, time_to_wait
    else:
        return delta_v1, delta_v2, 0

if __name__ == "__main__":
    initial_orbit_radius = 7000  # km
    target_orbit_radius = 14000  # km
    phase_angle = 30  # degrees

    try:
        delta_v1, delta_v2, time_to_wait = rendezvous(initial_orbit_radius, target_orbit_radius, phase_angle)
        print(f"Delta-v for the first burn: {delta_v1:.3f} km/s")
        print(f"Delta-v for the second burn: {delta_v2:.3f} km/s")
        if time_to_wait > 0:
            print(f"Time to wait for correct phase angle: {time_to_wait / 3600:.2f} hours")
    except ValueError as e:
        print(e)
