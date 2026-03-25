# -*- coding: utf-8 -*-
"""
Created on Fri Nov 15 12:21:12 2024

@author: johns
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# Read and process orbit data
df1 = pd.read_csv('47 UM 1planet.csv')
df2 = pd.read_csv('47 UM 2planet.csv')
df3 = pd.read_csv('47 UM 3planet.csv')
orbit_data = pd.concat([df1, df2, df3], axis=1)

# Convert angular data to degrees
f_deg = np.rad2deg(orbit_data[['f1', 'f2', 'f3']])

# Axis limits
a_min, a_max = orbit_data['a1'].min(), orbit_data['a1'].max()
f_min, f_max = f_deg['f1'].min(), f_deg['f1'].max()

# Common plotting functions
def plot_subplot(ax, pivot_data, cmap, vmin, vmax, title, xlabel, ylabel, cbar_label, colorbar=True):
    cax = ax.imshow(pivot_data, vmin=vmin, vmax=vmax, cmap=cmap, origin="lower", aspect='auto', 
                    extent=[a_min, a_max, f_min, f_max])
    ax.scatter(2.1, 60, color='blue', s=100, marker="x")
    ax.text(2.11, 60, '$L_4$', color='white', fontsize=12)
    ax.set_xlabel(xlabel)
    ax.set_ylabel(ylabel)
    ax.set_title(title)
    ax.set_facecolor('gray')
    if colorbar:
        fig.colorbar(cax, ax=ax, label=cbar_label)

# MEGNO Plots ===================================================================
fig, axs = plt.subplots(1, 3, figsize=(18, 6), gridspec_kw={'width_ratios': [1, 1, 1.2]})
cmap_megno = "RdYlGn_r"

for i, (f_col, a_col, megno_col, title) in enumerate(zip(['f1', 'f2', 'f3'], ['a1', 'a2', 'a3'], 
                                                           ['megno1', 'megno2', 'megno3'], 
                                                           ['47 UMa b', '47 UMa b, c', '47 UMa b, c, d'])):
    pivot_data = orbit_data.pivot(index=f_col, columns=a_col, values=megno_col)
    plot_subplot(axs[i], pivot_data, cmap_megno, vmin=1.9, vmax=4, title=title, 
                 xlabel="Semi-Major Axis [AU]", ylabel="True Anomaly [θ]", cbar_label='MEGNO', colorbar=(i == 2))

plt.tight_layout()
plt.savefig("47 UMa System - MEGNO.png", bbox_inches='tight', pad_inches=0)
plt.show()

# Eccentricity Plots ===================================================================
fig, axs = plt.subplots(1, 3, figsize=(18, 6), gridspec_kw={'width_ratios': [1, 1, 1.2]})
cmap_stable = plt.get_cmap('viridis')
cmap_stable.set_under('gray')

# Process eccentricity
for i, (megno_col, ecc_col) in enumerate(zip(['megno1', 'megno2', 'megno3'], 
                                              ['final_e1', 'final_e2', 'final_e3'])):
    orbit_data.loc[(orbit_data[megno_col] <= 1.9) | (orbit_data[megno_col] >= 2.1), ecc_col] = -1

for i, (f_col, a_col, ecc_col, title) in enumerate(zip(['f1', 'f2', 'f3'], ['a1', 'a2', 'a3'], 
                                                       ['final_e1', 'final_e2', 'final_e3'], 
                                                       ['47 UMa b', '47 UMa b, c', '47 UMa b, c, d'])):
    pivot_data = orbit_data.pivot(index=f_col, columns=a_col, values=ecc_col)
    plot_subplot(axs[i], pivot_data, cmap_stable, vmin=0, vmax=0.5, title=title, 
                 xlabel="Semi-Major Axis [AU]", ylabel="True Anomaly [θ]", cbar_label='Eccentricity', colorbar=(i == 2))

plt.tight_layout()
plt.savefig("47 UMa System - Final Eccentricity.png", bbox_inches='tight', pad_inches=0)
plt.show()

# Angular Distance Plots ===================================================================
fig, axs = plt.subplots(1, 3, figsize=(18, 6), gridspec_kw={'width_ratios': [1, 1, 1.2]})

# Process angular distance
for i, (megno_col, theta_col) in enumerate(zip(['megno1', 'megno2', 'megno3'], 
                                               ['final_theta1', 'final_theta2', 'final_theta3'])):
    orbit_data.loc[(orbit_data[megno_col] <= 1.9) | (orbit_data[megno_col] >= 2.1), theta_col] = -1

for i, (f_col, a_col, theta_col, title) in enumerate(zip(['f1', 'f2', 'f3'], ['a1', 'a2', 'a3'], 
                                                         ['final_theta1', 'final_theta2', 'final_theta3'], 
                                                         ['47 UMa b', '47 UMa b, c', '47 UMa b, c, d'])):
    pivot_data = orbit_data.pivot(index=f_col, columns=a_col, values=theta_col)
    plot_subplot(axs[i], pivot_data, cmap_stable, vmin=0, vmax=None, title=title, 
                 xlabel="Semi-Major Axis [AU]", ylabel="True Anomaly [θ]", cbar_label='Angular Distance [θ]', colorbar=(i == 2))

plt.tight_layout()
plt.savefig("47 UMa System - Final Angular Distance.png", bbox_inches='tight', pad_inches=0)
plt.show()