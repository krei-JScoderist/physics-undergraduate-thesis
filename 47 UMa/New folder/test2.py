# -*- coding: utf-8 -*-
"""
Created on Thu Nov 21 04:01:02 2024

@author: johns
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


def process_data(files, output_file):
    """
    Load and process orbital data from CSV files.

    Args:
        files (list of str): List of input CSV filenames.
        output_file (str): Output CSV filename for concatenated data.

    Returns:
        pd.DataFrame: Processed DataFrame with stability columns added.
    """
    # Load and combine CSV files
    dataframes = [pd.read_csv(file) for file in files]
    orbit_data = pd.concat(dataframes, axis=1)

    # Add stability columns for MEGNO values
    for i in range(1, len(files) + 1):
        orbit_data[f'stable{i}'] = orbit_data[f'megno{i}'].apply(lambda x: 1 if abs(x - 2) < 0.1 else 0)

    # Save the processed data to a CSV file
    orbit_data.to_csv(output_file, index=False)
    return orbit_data


def plot_heatmaps(data, params, titles, colormap, colorbar_label, output_file):
    """
    Plot heatmaps for the provided data.

    Args:
        data (list of dict): Each dict contains keys: `index`, `columns`, `values`, and `scatter_point`.
        params (tuple): Contains a_min, a_max, f_min, f_max for plot extents.
        titles (list of str): Titles for subplots.
        colormap (str): Colormap for the heatmaps.
        colorbar_label (str): Label for the colorbar.
        output_file (str): Filename to save the plot.
    """
    a_min, a_max, f_min, f_max = params

    # Enable constrained layout
    fig, axs = plt.subplots(1, 3, figsize=(18, 6), constrained_layout=True)

    for i, d in enumerate(data):
        pivot_data = d['data'].pivot(index=d['index'], columns=d['columns'], values=d['values'])
        cax = axs[i].imshow(
            pivot_data, cmap=colormap, origin="lower", aspect="auto",
            extent=[a_min, a_max, f_min, f_max], vmin=d.get('vmin', None), vmax=d.get('vmax', None)
        )
        axs[i].scatter(*d['scatter_point'], color="blue", s=100, marker="x")
        axs[i].text(d['scatter_point'][0] + 0.01, d['scatter_point'][1], "$L_4$", color="white", fontsize=12)
        axs[i].set_xlabel("Semi-Major Axis [AU]")
        axs[i].set_title(titles[i])
        if i == 0:
            axs[i].set_ylabel("True Anomaly [θ]")
        axs[i].set_facecolor("gray")

    # Add a single shared colorbar
    fig.colorbar(cax, ax=axs, label=colorbar_label, location="right", pad=0.005)

    # Save and show the plot
    plt.savefig(output_file, bbox_inches="tight", pad_inches=0)
    plt.show()


# Parameters
files = ['47 UM 1planet.csv', '47 UM 2planet.csv', '47 UM 3planet.csv']
output_file = "47 UM total.csv"
scatter_point = (2.1, 60)

# Process Data
orbit_data = process_data(files, output_file)

# General Parameters
a_min, a_max = orbit_data['a1'].min(), orbit_data['a1'].max()
f_min, f_max = np.rad2deg(orbit_data['f1']).min(), np.rad2deg(orbit_data['f1']).max()

# MEGNO Heatmaps
megno_data = [
    {"data": orbit_data, "index": f"f{i}", "columns": f"a{i}", "values": f"megno{i}", "scatter_point": scatter_point, "vmin": 1.9, "vmax": 4}
    for i in range(1, 4)
]
plot_heatmaps(megno_data, (a_min, a_max, f_min, f_max), ["47 UMa b", "47 UMa b, c", "47 UMa b, c, d"], "RdYlGn_r", "MEGNO", "47 UMa System - MEGNO.png")

# Filter stable orbits
stable_orbit_data = [
    orbit_data[orbit_data[f'stable{i}'] == 1] for i in range(1, 4)
]

# Eccentricity Heatmaps
eccentricity_data = [
    {"data": stable_orbit_data[i], "index": f"f{i + 1}", "columns": f"a{i + 1}", "values": f"final_e{i + 1}", "scatter_point": scatter_point, "vmin": 0, "vmax": 1}
    for i in range(3)
]
plot_heatmaps(eccentricity_data, (a_min, a_max, f_min, f_max), ["47 UMa b", "47 UMa b, c", "47 UMa b, c, d"], "viridis", "Eccentricity", "47 UMa System - Final Eccentricity.png")

# Angular Distance Heatmaps
angular_distance_data = [
    {"data": stable_orbit_data[i], "index": f"f{i + 1}", "columns": f"a{i + 1}", "values": f"final_theta{i + 1}", "scatter_point": scatter_point}
    for i in range(3)
]
plot_heatmaps(angular_distance_data, (a_min, a_max, f_min, f_max), ["47 UMa b", "47 UMa b, c", "47 UMa b, c, d"], "viridis", "Angular Distance [θ]", "47 UMa System - Final Angular Distance.png")
