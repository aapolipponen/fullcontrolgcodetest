import numpy as np
import matplotlib.pyplot as plt
from math import cos, tau
import fullcontrol as fc

# Define the airfoil parameters
c = 1.0  # chord length
t = 0.12  # maximum thickness as a fraction of chord length
m = 0.02  # maximum camber as a fraction of chord length

# Generate the x-coordinates of the airfoil shape
x = np.linspace(0, c, 100)

# Calculate the camber line
if m == 0:
    # If there is no camber, the camber line is a straight line
    z = np.zeros_like(x)
else:
    # If there is camber, calculate the camber line
    z = (m/c**2) * (2*c*x - x**2)

# Calculate the thickness distribution
yt = (t/0.2) * c * (0.2969 * np.sqrt(x/c) - 0.1260 * (x/c) - 0.3516 * (x/c)**2 + 0.2843 * (x/c)**3 - 0.1015 * (x/c)**4)

# Calculate the upper and lower surfaces of the airfoil
xu = x - yt*np.sin(np.arctan(z))
zu = z + yt*np.cos(np.arctan(z))

xl = x + yt*np.sin(np.arctan(z))
zl = z - yt*np.cos(np.arctan(z))

# Combine the upper and lower surfaces
x = np.concatenate((xu, np.flip(xl)))
z = np.concatenate((zu, np.flip(zl)))

# Plot the airfoil shape
plt.plot(x, z)
plt.gca().set_aspect('equal')
plt.show()
