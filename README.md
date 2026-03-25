# Short-Term Orbital Dynamics of Hypothetical Habitable Zone Trojans

## Undergraduate Physics Thesis
Author: John Sen B. Prudente  
Institution: University of the Philippines Baguio  
Year: 2024

## Overview
This repository contains the code, datasets, and analysis used for my undergraduate thesis on the orbital stability of hypothetical Trojan planets located in the habitable zones of multi-planet exoplanetary systems.

The study investigates the short-term orbital dynamics of Earth-mass Trojan bodies co-orbiting gas giants using N-body simulations. Simulations were performed using the REBOUND framework with the WHFast integrator, and orbital stability was evaluated using the MEGNO chaos indicator.

Selected systems include:
- 47 UMa
- HD 108874

## Repository Structure

exoplanet_filtering/
Scripts and data processing used to filter suitable exoplanet systems from the NASA Exoplanet Archive.

47UMa_system/
Simulation setup and outputs for Trojan stability analysis in the 47 UMa planetary system.

HD108874_system/
Simulation setup and outputs for Trojan stability analysis in the HD 108874 planetary system.

analysis/
Post-processing scripts used to generate plots, stability maps, and statistical analysis of the simulation results.

## Methods
1. Exoplanet systems were filtered using data from the NASA Exoplanet Archive.
2. Systems were selected based on:
   - multi-planet configuration
   - gas giant mass range
   - low orbital eccentricity
   - location within the stellar habitable zone.
3. N-body simulations were run using the REBOUND package with the WHFast symplectic integrator.
4. Orbital stability was analyzed using the MEGNO chaos indicator.

## Tools Used
- Python
- REBOUND N-body simulation package
- NumPy
- Pandas
- Matplotlib

## Thesis
The full thesis manuscript is included in this repository.
