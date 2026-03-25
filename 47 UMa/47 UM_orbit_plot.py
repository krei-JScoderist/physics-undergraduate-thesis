# -*- coding: utf-8 -*-
"""
Created on Tue Nov 12 13:15:49 2024

@author: johns
"""

import rebound
import numpy as np
import matplotlib.pyplot as plt

sim = rebound.Simulation()
sim.units = ('AU', 'yrs', 'Msun')

sim.add(m=1.06)
sim.add(m=0.002415138, a=2.1, e=0.032)  # Trojan host
sim.add(m=0.0005154777, a=3.6, e=0.098)
sim.add(m=0.001565525, a=11.6, e=0.16)
sim.add(m=3e-6, a=2.1, e=0.032, inc=0, f=np.deg2rad(60))  # Trojan body

times = np.linspace(0, 1000 * 2 * np.pi, int(1000e2))  # Simulate for 1000 orbits
xorbit = []
yorbit = []

sim.ri_whfast.safe_mode = 0
sim.dt = 0.01 * 2 * np.pi  # Timestep of 1% of the orbit period
sim.move_to_com()
ps = sim.particles
for time in times:
    sim.integrate(time, exact_finish_time=0)
    xorbit.append(ps[4].x)
    yorbit.append(ps[4].y)

theta = np.linspace(0, 2 * np.pi, 100)  # 100 points around the circle
inner = 0.939871383571698
xinner = inner * np.cos(theta)
yinner = inner * np.sin(theta)
outer = 2.22105359985882
xouter = outer * np.cos(theta)
youter = outer * np.sin(theta)

fig1 = rebound.OrbitPlot(sim, unitlabel="[AU]")
fig1.particles.set_color(["k", "k", "k", "orangered"])
fig1.orbits[3].set_linewidth(0)
fig1.primary.set_color("gold")
plt.plot(xorbit, yorbit, color='peachpuff')
plt.plot(xinner, yinner, 'C0')
plt.plot(xouter, youter, 'C0')
plt.savefig("47 UMa orbit plot.png")
plt.show()

fig2 = rebound.OrbitPlot(sim, unitlabel="[AU]", xlim=[-3,3], ylim=[-3,3])
fig2.particles.set_color(["k", "k", "k", "orangered"])
fig2.orbits[3].set_linewidth(0)
fig2.primary.set_color("gold")
plt.plot(xorbit, yorbit, color='peachpuff')
plt.plot(xinner, yinner, 'C0')
plt.plot(xouter, youter, 'C0')
plt.savefig("47 UMa orbit plot zoom.png")
plt.show()