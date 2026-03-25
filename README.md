# Short-Term Orbital Dynamics of Hypothetical Habitable Zone Trojans

## Undergraduate Physics Thesis
Author: John Sen B. Prudente  
Institution: University of the Philippines Baguio  
Year: 2024

---

## Overview
Trojan planets are co-orbital bodies that share the same orbital path as a larger planet, residing near the stable Lagrange points. Their potential existence in exoplanetary systems is an active area of astrophysics research.  
In this project, I use the `REBOUND` N-body simulation package (Rein & Tamayo) to explore the stability ranges of hypothetical Trojan planets under different initial conditions.

---

## Methods
- **Simulation Tool**: [REBOUND](https://rebound.readthedocs.io/en/latest/) (Rein & Tamayo, 2012–2015)  
- **Integrator**: WHFast Integrator
- **Parameters explored**:
  - Mass of the gas giant (1–3 MJ)  
  - Initial angular distance of Trojan test particles (30°–90°)  
  - Multi-planet scenarios (selected cases)  

---

## Results (Summary)
- Stability regions were mapped by varying the mass of the gas giant and the angular distance of Trojan bodies.  
- **Higher-mass gas giants** produced narrower stable angular ranges, while **lower-mass gas giants** allowed broader ranges of stability.  
- Example:  
  - A 2.53 MJ planet: stable Trojans found in ~40–90° separation.  
  - A 1.42 MJ planet: stable Trojans found in ~50–90°.  

(Plots and figures are available in the `results/` folder.)  

---

## Repository Structure

exoplanet_filtering/
Scripts and data processing used to filter suitable exoplanet systems from the NASA Exoplanet Archive.

47UMa_system/
Simulation setup and outputs for Trojan stability analysis in the 47 UMa planetary system.

HD108874_system/
Simulation setup and outputs for Trojan stability analysis in the HD 108874 planetary system.

analysis/
Post-processing scripts used to generate plots, stability maps, and statistical analysis of the simulation results.

---

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

