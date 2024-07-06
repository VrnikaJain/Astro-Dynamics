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

if __name__ == "__main__":
    r1 = 7000  # Initial orbit radius in km
    r2 = 14000  # Final orbit radius in km

    delta_v1, delta_v2 = hohmann_transfer(r1, r2)
    print(f"Delta-v for the first burn: {delta_v1} km/s, Delta-v for the second burn: {delta_v2} km/s")
