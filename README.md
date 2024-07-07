# Astrodynamics Library Documentation

# Introduction
The Astrodynamics Library is a comprehensive Python package designed for performing astrodynamics calculations and simulations. It includes modules for orbital mechanics, trajectory optimization, and mission planning, providing essential tools for space mission design and analysis. This document outlines the structure, functionality, and usage of each module within the library.

## Directory Structure
```
astrodynamics/
|-- setup.py
|-- orbital_mechanics/
|   |-- __init__.py
|   |-- kepler_orbit.py
|   |-- hohmann_transfer.py
|   |-- perturbations.py
|-- trajectory_optimization/
|   |-- __init__.py
|   |-- lamberts_problem.py
|   |-- low_thrust.py
|-- mission_planning/
|   |-- __init__.py
|   |-- launch_window.py
|   |-- rendezvous.py
|-- utils/
|   |-- __init__.py
|   |-- constants.py
|   |-- conversions.py
|-- tests/
    |-- test_kepler_orbit.py
    |-- test_hohmann_transfer.py
    |-- test_lamberts_problem.py
    |-- test_perturbations.py
    |-- test_low_thrust.py
    |-- test_launch_window.py
    |-- test_rendezvous.py
```

# Modules
## Orbital Mechanics
#### Kepler Orbit (`orbital_mechanics/kepler_orbit.py`)
The `kepler_orbit` module provides functions for calculating properties of Keplerian orbits:
- `kepler_orbit(semi_major_axis, eccentricity, true_anomaly)`: Computes the distance from the central body to a spacecraft in a Keplerian orbit.

#### Hohmann Transfer (`orbital_mechanics/hohmann_transfer.py`)
The `hohmann_transfer` module facilitates calculations related to Hohmann transfers between circular orbits:
- `hohmann_transfer(r1, r2, mu=398600)`: Computes the delta-v required for a Hohmann transfer.

#### Perturbations (`orbital_mechanics/perturbations.py`)
The `perturbations` module includes functions for modeling perturbative effects on orbits:
- `atmospheric_drag(r, v, Cd, A, m)`: Calculates acceleration due to atmospheric drag.
- `gravitational_perturbation(r, mu=398600, J2=1.08263e-3, Re=6371)`: Computes acceleration due to J2 gravitational perturbations.

## Trajectory Optimization
#### Lambert's Problem (`trajectory_optimization/lamberts_problem.py`)
The `lamberts_problem` module provides functions for solving Lambert's problem, used in determining orbits between two points:
- `lamberts_problem(r1, r2, tof)`: Solves Lambert's problem to compute initial and final velocities.

#### Low-Thrust Trajectory Optimization (`trajectory_optimization/low_thrust.py`)
The `low_thrust` module facilitates optimization of trajectories under continuous low-thrust conditions:
- `low_thrust_trajectory(r0, v0, thrust, isp, mass, t_span, mu=398600)`: Computes a low-thrust trajectory using numerical integration.

## Mission Planning
#### Launch Window (`mission_planning/launch_window.py`)
The `launch_window` module calculates optimal launch windows for space missions:
- `calculate_launch_window(departure_date, target_date)`: Determines the launch window given departure and target dates.
#### Rendezvous (`mission_planning/rendezvous.py`)
The `rendezvous` module provides functions for planning and executing rendezvous maneuvers between spacecraft:
- `rendezvous(initial_orbit_radius, target_orbit_radius, phase_angle, mu=398600)`: Computes delta-v requirements for rendezvous maneuvers.

## Utilities
#### Constants (`utils/constants.py`)
The `constants` module defines constants used throughout the library:
- `MU_EARTH`: Standard gravitational parameter for Earth.
- `R_EARTH`: Radius of Earth.
#### Conversions (`utils/conversions.py`)
The `conversions` module includes functions for unit conversions:
- `degrees_to_radians(degrees)`: Converts degrees to radians.
- `radians_to_degrees(radians)`: Converts radians to degrees.

## Testing
The library includes comprehensive unit tests located in the `tests` directory. To run the tests, navigate to the `astrodynamics` directory and execute:
```bash
pytest
