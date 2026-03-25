# -*- coding: utf-8 -*-
"""
Created on Wed Nov 20 11:38:53 2024

@author: johns
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import pearsonr, spearmanr

# Data
orbit_data = pd.read_csv('47 UM megno.csv')
f_rad = orbit_data['f']
initial_distances = np.rad2deg(f_rad)
final_distances = orbit_data['final_theta']

# Scatter Plot
plt.figure(figsize=(8, 6))
plt.scatter(initial_distances, final_distances, color='blue', label='Trojan Data')
plt.plot(initial_distances, initial_distances, color='red', linestyle='--', label='y=x')
plt.xlabel('Initial Angular Distance (°)')
plt.ylabel('Final Angular Distance (°)')
plt.title('Initial vs Final Angular Distance')
plt.legend()
plt.grid()
plt.show()

# Pearson Correlation
pearson_corr, _ = pearsonr(initial_distances, final_distances)
print(f"Pearson Correlation Coefficient: {pearson_corr:.2f}")

# Spearman Correlation
spearman_corr, _ = spearmanr(initial_distances, final_distances)
print(f"Spearman Correlation Coefficient: {spearman_corr:.2f}")
