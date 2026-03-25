# -*- coding: utf-8 -*-
"""
Created on Sun Nov 10 13:20:22 2024

@author: johns
"""

import numpy as np
import matplotlib.pyplot as plt

# Create a 3D plot
ax = plt.figure(figsize=[7,7]).add_subplot(projection='3d')

# Star parameters
ax.scatter(0, 0, 0, color='gold', s=10)

theta = np.linspace(0, 2 * np.pi, 100)  # 100 points around the ellipse
# Planet parameters
a1 = 2.1  
e1 = 0.032
inc1 = np.deg2rad(0)  

a2 = 3.6
e2 = 0.098
inc2 = np.deg2rad(0)

a3 = 11.6
e3 = 0.16
inc3 = np.deg2rad(0)

# Planet 1
semi_minor_axis1 = a1 * np.sqrt(1 - e1**2)
x_orbit1 = a1 * (np.cos(theta) - e1)  
y_orbit1 = semi_minor_axis1 * np.sin(theta)  
z_orbit1 = np.zeros_like(x_orbit1)  

# Apply rotation matrix for inclination (around the x-axis)
rotation_matrix1 = np.array([
    [1, 0, 0],
    [0, np.cos(inc1), -np.sin(inc1)],
    [0, np.sin(inc1), np.cos(inc1)]
])

orbit_coordinates1 = np.vstack([x_orbit1, y_orbit1, z_orbit1])
rotated_orbit1 = np.dot(rotation_matrix1, orbit_coordinates1)
planet_position1 = np.array([a1 * (1 - e1), 0, 0])
planet_position_rotated1 = np.dot(rotation_matrix1, planet_position1)

ax.plot(rotated_orbit1[0], rotated_orbit1[1], rotated_orbit1[2], color='k')
ax.scatter(planet_position_rotated1[0], planet_position_rotated1[1], planet_position_rotated1[2], color='k', s=10)

# Habitable Zone
inner = 0.939871383571698
outer = 2.22105359985882

inner_xorbit = inner * np.cos(theta)  
inner_yorbit = inner * np.sin(theta)  
inner_zorbit = 0

inner_orbit = np.vstack([inner_xorbit, inner_yorbit])
ax.plot(inner_orbit[0], inner_orbit[1], color='C0', label='Inner HZ')

outer_xorbit = outer * np.cos(theta)  
outer_yorbit = outer * np.sin(theta)  
outer_zorbit = 0

outer_orbit = np.vstack([outer_xorbit, outer_yorbit])
ax.plot(outer_orbit[0], outer_orbit[1], color='C0', label='Outer HZ')

# Trojans
true_anomaly_range = np.linspace(np.deg2rad(30), np.deg2rad(90), 50)
semi_major_axis_range = np.linspace(a1-(0.05*a1), a1+(0.05*a1), 50)

for i in range(len(true_anomaly_range)):
    for j in range(len(semi_major_axis_range)):
        theta_L4 = true_anomaly_range[i]
        a1 = semi_major_axis_range[j]  # Current semi-major axis value
        semi_minor_axis1 = a1 * np.sqrt(1 - e1**2)  # Adjust semi-minor for eccentricity
        
        # Calculate L4 position with the varying semi-major axis
        x_L4 = a1 * (np.cos(theta_L4) - e1)  # Adjusted for eccentricity
        y_L4 = semi_minor_axis1 * np.sin(theta_L4)  # Adjusted for eccentricity
        z_L4 = 0  # Flat in this case
        L4_position = np.array([x_L4, y_L4, z_L4])
        
        ax.scatter(L4_position[0], L4_position[1], L4_position[2], color='orangered', s=0.5)

# # PLanet 2
# semi_minor_axis2 = a2 * np.sqrt(1 - e2**2)
# x_orbit2 = a2 * (np.cos(theta) - e2)  
# y_orbit2 = semi_minor_axis2 * np.sin(theta) 
# z_orbit2 = np.zeros_like(x_orbit2)  

# rotation_matrix2 = np.array([
#     [1, 0, 0],
#     [0, np.cos(inc2), -np.sin(inc2)],
#     [0, np.sin(inc2), np.cos(inc2)]
# ])

# orbit_coordinates2 = np.vstack([x_orbit2, y_orbit2, z_orbit2])
# rotated_orbit2 = np.dot(rotation_matrix2, orbit_coordinates2)
# planet_position2 = np.array([a2 * (1 - e2), 0, 0])
# planet_position_rotated2 = np.dot(rotation_matrix2, planet_position2)

# ax.plot(rotated_orbit2[0], rotated_orbit2[1], rotated_orbit2[2], color='k')
# ax.scatter(planet_position_rotated2[0], planet_position_rotated2[1], planet_position_rotated2[2], color='k', s=10)

# # Planet 3
# semi_minor_axis3 = a3 * np.sqrt(1 - e3**2)
# x_orbit3 = a3 * (np.cos(theta) - e3)  
# y_orbit3 = semi_minor_axis3 * np.sin(theta) 
# z_orbit3 = np.zeros_like(x_orbit3)  

# rotation_matrix3 = np.array([
#     [1, 0, 0],
#     [0, np.cos(inc3), -np.sin(inc3)],
#     [0, np.sin(inc3), np.cos(inc3)]
# ])

# orbit_coordinates3 = np.vstack([x_orbit3, y_orbit3, z_orbit3])
# rotated_orbit3 = np.dot(rotation_matrix3, orbit_coordinates3)
# planet_position3 = np.array([a3 * (1 - e3), 0, 0])
# planet_position_rotated3 = np.dot(rotation_matrix3, planet_position3)

# ax.plot(rotated_orbit3[0], rotated_orbit3[1], rotated_orbit3[2], color='k')
# ax.scatter(planet_position_rotated3[0], planet_position_rotated3[1], planet_position_rotated3[2], color='k', s=10)

limit = 2
ax.set(xlim=[-limit, limit], xticks=[-limit, 0, limit], xlabel=('x [AU]'),
       ylim=[-limit, limit], yticks=[-limit, 0, limit], ylabel=('y [AU]'),
       zlim=[-0.01, 0.01], zticks=[-0.01, 0., 0.01], zlabel=('z [AU]')
)

for axis in [ax.xaxis, ax.yaxis, ax.zaxis]:
    axis.pane.fill = False
    axis.set_rotate_label(False)
    
ax.grid(False)
ax.set_box_aspect(None, zoom=0.80)
plt.savefig("47 UMa trojans.png")
plt.show()