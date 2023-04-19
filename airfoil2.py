import fullcontrol as fc
import math

def naca_airfoil(c, t, m, p, resolution, y_multiplier):
    """
    Returns a list of fc.Point objects that define a NACA airfoil with the specified parameters.
    """
    # Define the chord line and half thickness distribution
    x = [i / resolution for i in range(resolution + 1)]
    z = [(m / (p ** 2)) * (2 * p * c_i - c_i ** 2) if c_i <= p else (m / ((1 - p) ** 2)) * ((1 - 2 * p) * c_i + 2 * p * c - c - 2 * p * c_i ** 2 + c_i ** 2) for c_i in x]
    yt = [(t / 0.2) * ((0.2969 * math.sqrt(c_i)) - (0.1260 * c_i) - (0.3516 * c_i ** 2) + (0.2843 * c_i ** 3) - (0.1036 * c_i ** 4)) * c for c_i in x]

    # Calculate the camber line
    yc = [(m / (p ** 2)) * (2 * p * c_i - c_i ** 2) if c_i <= p else (m / ((1 - p) ** 2)) * ((1 - 2 * p) * c_i + 2 * p * c - c - 2 * p * c_i ** 2 + c_i ** 2 - t * c) for c_i in x]

    # Calculate the upper and lower surfaces of the airfoil
    xu = [fc.Point(x=i * c, y=z[i] + yt[i] * y_multiplier, z=0) for i in range(resolution + 1)]
    xl = [fc.Point(x=i * c, y=yc[i] - yt[i] * y_multiplier, z=0) for i in range(resolution + 1)][::-1]

    # Combine the surfaces to form the airfoil
    points = xu + xl[1:-1]

    return points

# Generate the airfoil points and print out the coordinates
points = naca_airfoil(c=1, t=0.12, m=0.02, p=0.4, resolution=32, y_multiplier=32)
for point in points:
    print(f"x={point.x}, y={point.y}, z={point.z}")

steps = []
steps.extend(points)
fc.transform(steps, 'plot', fc.PlotControls(color_type='print_sequence'))
