# -*- coding: utf-8 -*-
"""
Created on Sat Nov 30 13:34:27 2024

@author: johns
"""

import numpy as np
import rebound

# Function to calculate MEGNO for a given semi-major axis and true anomaly
def calculate_megno(a, f, total_time):
    """
    Calculate MEGNO and final orbital parameters for a Trojan in a given planetary system.

    Args:
        a (float): Semi-major axis of the Trojan.
        f (float): True anomaly of the Trojan (radians).
        total_time (float): Total integration time.

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
    
    # Add planets
    sim.add(m=0.002415138, a=2.1, e=0.032, inc=0)
    sim.add(m=0.0005154777, a=3.6, e=0.098, inc=0)
    
    # Activate MEGNO and configure simulation
    sim.move_to_com()
    sim.init_megno()
    sim.exit_max_distance = 20.0
    orbper = 1078 / 365
    sim.dt = 0.01 * orbper

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
def generate_megno_maps(grid, integration_time, output_file):
    """
    Generate MEGNO maps for a specified planetary system and save to a CSV file.

    Args:
        grid (int): Resolution of the grid (number of values for semi-major axis and true anomaly).
        integration_time (float): Total integration time.
        output_file (str): Output filename for the CSV.
    """
    # Grid settings
    a_host = 2.1
    a_min = a_host - 0.05 * a_host
    a_max = a_host + 0.05 * a_host
    a_values = np.linspace(a_min, a_max, grid)
    f_values_rad = np.linspace(np.deg2rad(30), np.deg2rad(90), grid)

    # Initialize storage for results
    megno_list = []

    # Calculate MEGNO for each combination of semi-major axis and true anomaly
    for a in a_values:
        for f in f_values_rad:
            megno_value, final_e, final_theta = calculate_megno(a, f, integration_time)
            megno_list.append([a, f, integration_time, megno_value, final_e, final_theta])

    # Append results to the output CSV file
    megno_array = np.array(megno_list)
    with open(output_file, "ab") as f:
        np.savetxt(f, megno_array, delimiter=",", comments="")


# Main execution block
grid = 50
output_file = "megno_results.csv"
header = "a,f,integration_time,megno,final_e,final_theta"

# Create or overwrite the CSV file with the header
with open(output_file, "w") as f:
    f.write(header + "\n")

# Process each integration time and save results
for integration_time in [10**n for n in range(3, 7)]:
    print(f"Processing integration time: {integration_time} years...")
    generate_megno_maps(grid=grid, integration_time=integration_time, output_file=output_file)

print(f"Results saved to {output_file}.")