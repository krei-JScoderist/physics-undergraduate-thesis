# -*- coding: utf-8 -*-
"""
Created on Sun Sep 22 15:58:36 2024

@author: johns
"""

import pandas as pd
import numpy as np

# Filter for default parameters
ps_data = pd.read_csv('PS_2024.10.13_06.48.22.csv')
ps_data = ps_data[
    (ps_data['default_flag'] == 1)].copy()        # Use primary parameters
# Convert mass from Jupiter masses to solar masses
ps_data['pl_bmass (Msun)'] = 0.0009546 * ps_data['pl_bmassj']
ps_data.to_csv('default_ps_data.csv', index=False)


# Filter for simulation
ps_data = ps_data[
    (ps_data['sy_snum'] == 1) &             # Single host stars
    (ps_data['sy_pnum'] > 1) &              # More than 1 planet
    (ps_data['pl_bmassj'] >= 0.3) &         # Lower mass limit
    (ps_data['pl_bmassj'] <= 13) &          # Upper mass limit
    (ps_data['pl_orbeccen'] <= 0.25)        # Eccentricity ≤ 0.25
].copy()

ps_data.to_csv('sorted_confirmed_ps_data.csv', index=False)

# Calculate luminosity using the Stefan-Boltzmann law
def luminosity(radius, temp):
    solar_radius_meters = 6.957e8  # Solar radius in meters
    radius_meters = radius * solar_radius_meters
    stefan_boltzmann_constant = 5.67037442e-8  # W/m^2/K^4
    solar_luminosity = 3.828e26  # W
    luminosity = 4 * np.pi * radius_meters**2 * stefan_boltzmann_constant * temp**4
    return luminosity / solar_luminosity  # Return in units of solar luminosity

ps_data['st_lum'] = ps_data.apply(lambda row: luminosity(row['st_rad'], row['st_teff']), axis=1)

# Define function for habitable zone boundaries
def habitable_zone_boundaries(L):
    inner_bound = (L / 1.7753) ** 0.5
    outer_bound = (L / 0.3179) ** 0.5
    return inner_bound, outer_bound

# Calculate habitable zone boundaries
ps_data[['Inner HZ', 'Outer HZ']] = ps_data['st_lum'].apply(habitable_zone_boundaries).apply(pd.Series)

# Check if the planet's orbit is within the habitable zone
ps_data['In HZ'] = ps_data.apply(
    lambda row: row['Inner HZ'] <= row['pl_orbsmax'] <= row['Outer HZ'], axis=1)

# Filter planets inside the habitable zone
ps_data = ps_data[ps_data['In HZ']]
ps_data.to_csv('sorted_confirmed_habitable_ps_data.csv', index=False)
