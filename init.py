import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Define the function to be integrated
def f(r, theta, z):
    return r*np.sin(theta)*z

# Set the limits of integration
r_limits = [0, 2]
theta_limits = [0, np.pi]
z_limits = [-1, 1]

# Set the number of subdivisions in each direction
r_steps = 100
theta_steps = 100
z_steps = 100

# Create arrays to store the coordinates of the subdivisions
r_coords = np.linspace(r_limits[0], r_limits[1], r_steps)
theta_coords = np.linspace(theta_limits[0], theta_limits[1], theta_steps)
z_coords = np.linspace(z_limits[0], z_limits[1], z_steps)

# Create an array to store the function values
f_vals = np.zeros((r_steps, theta_steps, z_steps))

# Compute the function values
for i, r in enumerate(r_coords):
    for j, theta in enumerate(theta_coords):
        for k, z in enumerate(z_coords):
            f_vals[i,j,k] = f(r, theta, z)

# Perform the triple integral
integral = np.sum(f_vals) * (r_limits[1] - r_limits[0])/r_steps * (theta_limits[1] - theta_limits[0])/theta_steps * (z_limits[1] - z_limits[0])/z_steps

print("The integral is:", integral)

# Plot the function
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# Plot the wireframe
ax.plot_wireframe(r_coords, theta_coords, z_coords, f_vals, rstride=10, cstride=10)

# Set the plot limits
ax.set_xlim(r_limits)
ax.set_ylim(theta_limits)
ax.set_zlim(z_limits)

# Set the plot labels
ax.set_xlabel('r')
ax.set_ylabel('theta')
ax.set_zlabel('z')

plt.show()