# -*- coding: utf-8 -*-
"""
Created on Sun Nov  3 09:26:38 2024

@author: johns
"""

import numpy as np
import rebound

# Function to calculate MEGNO for a given semi-major axis and true anomaly
def calculate_megno(a, f, planets):
    """
    Calculate MEGNO and final orbital parameters for a Trojan in a given planetary system.

    Args:
        a (float): Semi-major axis of the Trojan.
        f (float): True anomaly of the Trojan (radians).
        planets (list): List of dictionaries defining the planetary system.

    Returns:
        tuple: MEGNO, final eccentricity, and final angular distance (in degrees).
    """
    sim = rebound.Simulation()
    sim.units = ('AU', 'yrs', 'Msun')
    sim.integrator = "whfast"
    sim.ri_whfast.safe_mode = 0

    # Add central star
    sim.add(m=1.06)
    
    # Add the Trojan body
    sim.add(m=3e-6, a=a, e=0.032, inc=0, f=f)
    
    # Add planets and Trojan host
    for planet in planets:
        sim.add(**planet)

    # Activate MEGNO and configure simulation
    sim.move_to_com()
    sim.init_megno()
    sim.exit_max_distance = 20.0
    orbper = 394.48123 / 365
    sim.dt = 0.01 * orbper
    total_time = 1000 * orbper

    try:
        sim.integrate(total_time, exact_finish_time=0)
        megno = sim.megno()
        final_e = sim.particles[1].e
        final_theta = abs(np.rad2deg(sim.particles[1].theta - sim.particles[2].theta))
        return megno, final_e, final_theta
    except rebound.Escape:
        final_e = sim.particles[1].e
        final_theta = abs(np.rad2deg(sim.particles[1].theta - sim.particles[2].theta))
        return 10.0, final_e, final_theta


# Function to generate MEGNO maps for a system
def generate_megno_maps(grid, a_host, planets, output_file, header):
    """
    Generate MEGNO maps for a specified planetary system.

    Args:
        grid (int): Resolution of the grid (number of values for semi-major axis and true anomaly).
        a_host (float): Semi-major axis of the Trojan host planet.
        planets (list): List of dictionaries defining the planetary system.
        output_file (str): Output filename for the CSV.
        header (str): Header for the CSV file.
    """
    # Grid settings
    a_min = a_host - 0.05 * a_host
    a_max = a_host + 0.05 * a_host
    a_values = np.linspace(a_min, a_max, grid)
    f_values_rad = np.linspace(np.deg2rad(30), np.deg2rad(90), grid)

    # Initialize storage for results
    megno_list = []

    # Calculate MEGNO for each combination of semi-major axis and true anomaly
    for a in a_values:
        for f in f_values_rad:
            megno_value, final_e, final_theta = calculate_megno(a, f, planets)
            megno_list.append([a, f, megno_value, final_e, final_theta])

    # Save results to a CSV file
    megno_array = np.array(megno_list)
    np.savetxt(output_file, megno_array, delimiter=",", header=header, comments="")


# Define planetary systems
systems = [
    {
        "name": "HD 108874 1planet",
        "a_host": 1.04,
        "planets": [{"m": 0.001355532, "a": 1.04, "e": 0.13, "inc": 0}],
        "output_file": "HD 108874 1planet.csv",
        "header": "a1,f1,megno1,final_e1,final_theta1",
    },
    {
        "name": "HD 108874 2planet",
        "a_host": 1.04,
        "planets": [
            {"m": 0.001355532, "a": 1.04, "e": 0.13, "inc": 0},
            {"m": 0.001040501, "a": 2.81, "e": 0.239, "inc": 0},
        ],
        "output_file": "HD 108874 2planet.csv",
        "header": "a2,f2,megno2,final_e2,final_theta2",
    }
]

# Generate MEGNO maps for all systems
grid = 50
for system in systems:
    print(f"Processing {system['name']}...")
    generate_megno_maps(
        grid=grid,
        a_host=system["a_host"],
        planets=system["planets"],
        output_file=system["output_file"],
        header=system["header"],
    )