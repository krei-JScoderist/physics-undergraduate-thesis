# -*- coding: utf-8 -*-
"""
Created on Tue Dec 10 14:11:01 2024

@author: johns
"""

import rebound
import numpy as np
import matplotlib.pyplot as plt

from rebound import data
sim = rebound.Simulation()
data.add_outer_solar_system(sim) # either this, or add the planets manually
rebound.OrbitPlot(sim)

# We'll integrate the outer Solar System for 1000 years into the future and measure 
# the energy error along the way. We do that at random intervals to make sure we 
# don't have any aliasing with an orbital period. The following function runs the 
# simulation, and then returns the error.

def measure_energy(sim):
    Nsamples = 1000
    tmax = 2.*np.pi*1e3 # 1000 years
    t_samples = tmax*np.sort(np.random.random(Nsamples))
    E0 = sim.energy() # initial energy
    Emax = 0. # maximum energy error
    for t in t_samples:
        # we do not want to change the timestep to reach t exactly, thus 
        # we need to set exact_finish_time=False and slighlty overshoot.
        sim.integrate(t,exact_finish_time=False) 
        E = sim.energy()
        Emax = max(Emax, np.abs((E-E0)/E0))
    return Emax

# To get an idea how our integrators are behaving, we want to run this simulation 
# for various timesteps. So let us set up an array of timesteps from 0.001 to 1 
# orbital periods of Jupiter.

N_dt_samples = 100
dt_samples = sim.particles[2].P * np.logspace(-3,0.,N_dt_samples)

# Let's run the simulations with the standard WH integrator first. We set safe_mode 
# to 0 to speed up the calculation.

Emax_wh = np.zeros(N_dt_samples)
for i, dt in enumerate(dt_samples):
    sim_run = sim.copy() # make a copy of the simulation so we don't need to set a new one up every time
    sim_run.integrator = "whfast"
    sim_run.dt = dt
    sim.ri_whfast.safe_mode = False
    Emax_wh[i] = measure_energy(sim_run)

f,ax = plt.subplots(1,1,figsize=(7,5))
ax.set_xscale("log")
ax.set_yscale("log")
ax.set_xlabel("Timestep [Jupiter years]")
ax.set_ylabel("Relative Energy Error")
ax.plot(dt_samples/sim.particles[1].P,Emax_wh,label="WH")
ax.legend();