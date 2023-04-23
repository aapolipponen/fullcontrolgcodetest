import numpy as np
import fullcontrol as fc

def naca_airfoil(naca_num, num_points):
    """
    Generates the coordinates of a NACA airfoil.
    
    Parameters:
        naca_num (str): The four-digit NACA airfoil number.
        num_points (int): The number of points to generate.
        
    Returns:
        list: A list of fc.Point objects containing the coordinates of the NACA airfoil.
    """
    m = int(naca_num[0]) / 100  # Maximum camber
    p = int(naca_num[1]) / 10   # Location of maximum camber
    t = int(naca_num[2:]) / 100 # Maximum thickness
    
    x = np.linspace(0, 1, num_points)
    y_c = np.zeros_like(x)
    y_t = 5*t * (0.2969*np.sqrt(x) - 0.126*x - 0.3516*x**2 + 0.2843*x**3 - 0.1015*x**4)
    
    # Calculate camber line and upper/lower surfaces
    if p == 0 or m == 0:
        yc = np.zeros_like(x)
        xu = x
        xl = x
    else:
        yc = np.where(x < p, m/p**2 * (2*p*x - x**2), m/(1-p)**2 * ((1-2*p) + 2*p*x - x**2))
        theta = np.arctan(np.gradient(yc, x))
        xu = x - y_t*np.sin(theta)
        xl = x + y_t*np.sin(theta)
    
    yu = yc + y_t*np.cos(theta)
    yl = yc - y_t*np.cos(theta)
    
    # Generate fc.Point objects
    steps = []
    for i in range(num_points):
        steps.append(fc.Point(x=xu[i], y=yu[i], z=0))
    for i in range(num_points-1, -1, -1):
        steps.append(fc.Point(x=xl[i], y=yl[i], z=0))
    
    return steps

# Example usage
naca_num = '2412'
num_points = 100
steps = naca_airfoil(naca_num, num_points)
fc.transform(steps, 'plot', fc.PlotControls(color_type='print_sequence'))
