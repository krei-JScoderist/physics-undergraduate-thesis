# -*- coding: utf-8 -*-
"""
Created on Sat Nov 30 14:00:48 2024

@author: johns
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

orbit_data = pd.read_csv('megno_results.csv')

# Convert angular data to degrees
orbit_data['f_deg'] = np.rad2deg(orbit_data['f'])  # Create a new column with true anomaly in degrees

# Axis limits
a_min, a_max = orbit_data['a'].min(), orbit_data['a'].max()
f_min, f_max = orbit_data['f_deg'].min(), orbit_data['f_deg'].max()

chunk_size = 2500
integration_times = [10**x for x in range(3, 7)]  # Define integration times

# Loop through integration times and corresponding chunks
for x, integration_time in enumerate(integration_times, start=3):
    subset = orbit_data[orbit_data['integration_time'] == integration_time].iloc[:chunk_size]
    
    # Reshape data into a pivot table (grid) format for heatmap
    heatmap_data = subset.pivot_table(
        index="f_deg",    # y-axis (true anomaly in degrees)
        columns="a",      # x-axis (semi-major axis)
        values="megno"    # Heatmap intensity (MEGNO values)
    )
    
    # Ensure proper sorting of axes
    heatmap_data = heatmap_data.sort_index(axis=0).sort_index(axis=1)

    # Plot the heatmap
    plt.figure(figsize=(10, 8))
    plt.imshow(heatmap_data, vmin=1.9, vmax=4, aspect="auto", cmap="RdYlGn_r", origin="lower",
               extent=[a_min, a_max, f_min, f_max])
    plt.colorbar(label="MEGNO")
    plt.ylabel("True Anomaly [deg]")
    plt.xlabel("Semi-Major Axis [AU]")
    plt.title(rf"Stability Region for Integration Time $10^{x}$")  # Dynamically update title
    plt.savefig(f"10^{x}.png", bbox_inches='tight', pad_inches=0)
    plt.show()
