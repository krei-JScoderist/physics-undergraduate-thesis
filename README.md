# Orbital Stability of Trojan Planets
This repository contains the code and results from my undergraduate thesis on the **orbital stability of Trojan planets** in exoplanetary systems. The study focuses on simulating Trojan bodies near the L4 and L5 Lagrange points of gas giants, and exploring how their long-term stability depends on planetary mass and initial angular separation.

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



---

## Requirements
- Python 3.8+  
- [REBOUND](https://rebound.readthedocs.io/en/latest/) (`pip install rebound`)  
- NumPy, Matplotlib, Pandas  

