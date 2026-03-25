# -*- coding: utf-8 -*-
"""
Created on Mon Nov 25 10:53:31 2024

@author: johns
"""

import numpy as np
import pandas as pd

# Read the data from CSV files
data1 = pd.read_csv('../47 UMa/47 UM total.csv')
data2 = pd.read_csv('../HD 108874/HD 108874 total.csv')

# Function to calculate the stable fraction
def calculate_stable_fraction(data, column_name):
    stable_count = data[column_name].value_counts().get(1, 0)  # Count of 1s (stable)
    total_count = len(data[column_name])  # Total entries
    if total_count > 0:
        return stable_count / total_count
    return 0  # Avoid division by zero

# Function to calculate the centroid of the stable region
def centroid_stable_region(data, a_column, f_column, stable_column):
    a = data[a_column]
    f = np.rad2deg(data[f_column])
    stability = data[stable_column]
    
    weighted_sum_a = np.sum(a * stability)  # Weighted sum of semi-major axis
    weighted_sum_f = np.sum(f * stability)  # Weighted sum of true anomaly
    total_weight = np.sum(stability)  # Total weight (sum of stability values)
    
    if total_weight > 0:
        centroid_a = weighted_sum_a / total_weight  # Centroid of a
        centroid_f = weighted_sum_f / total_weight  # Centroid of f
    else:
        centroid_a = centroid_f = 0  # Avoid division by zero
    
    return centroid_a, centroid_f  # Return the centroids

# Calculate stable fractions for each table
stable_fraction_1 = calculate_stable_fraction(data1, 'stable1')  # 47 UMa - 1 planet
stable_fraction_2 = calculate_stable_fraction(data1, 'stable2')  # 47 UMa - 2 planets
stable_fraction_3 = calculate_stable_fraction(data1, 'stable3')  # 47 UMa - 3 planets
stable_fraction_4 = calculate_stable_fraction(data2, 'stable1')  # HD 108874 - 1 planet
stable_fraction_5 = calculate_stable_fraction(data2, 'stable2')  # HD 108874 - 2 planets

# Calculate centroid point
centroid_point_1 = centroid_stable_region(data1, 'a1', 'f1', 'stable1')  # 47 UMa - 1 planet
centroid_point_2 = centroid_stable_region(data1, 'a2', 'f2', 'stable2')  # 47 UMa - 2 planets
centroid_point_3 = centroid_stable_region(data1, 'a3', 'f3', 'stable3')  # 47 UMa - 3 planets
centroid_point_4 = centroid_stable_region(data2, 'a1', 'f1','stable1')  # HD 108874 - 1 planet
centroid_point_5 = centroid_stable_region(data2, 'a2', 'f2','stable2')  # HD 108874 - 2 planets

# Create a summary table with the calculated stable fractions
summary_table = pd.DataFrame({
    'Planet configurations': [
        '47 UMa - 1 planet', 
        '47 UMa - 2 planets', 
        '47 UMa - 3 planets', 
        'HD 108874 - 1 planet', 
        'HD 108874 - 2 planets'
    ],
    'Stable Fraction': [
        stable_fraction_1, 
        stable_fraction_2, 
        stable_fraction_3, 
        stable_fraction_4, 
        stable_fraction_5
    ],
    'Centroid Point': [
        centroid_point_1,
        centroid_point_2,
        centroid_point_3,
        centroid_point_4,
        centroid_point_5,
    ]
})

# Display the summary table
summary_table.to_csv('summary_table.csv', index=False)



