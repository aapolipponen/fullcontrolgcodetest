import fullcontrol as fc
import numpy as np

def NACA_airfoil(m, p, t, c, num_points):
    """
    Returns the x, y coordinates of a four-digit NACA airfoil.
    :param m: maximum camber, as a fraction of the chord length.
    :param p: location of maximum camber, as a fraction of the chord length.
    :param t: maximum thickness, as a fraction of the chord length.
    :param c: chord length.
    :param num_points: number of points to generate for the airfoil.
    """
    # Calculate the parameters for the NACA airfoil equation.
    a0 = 0.2969
    a1 = -0.1260
    a2 = -0.3516
    a3 = 0.2843
    a4 = -0.1015

    # Create the x-coordinates.
    x = np.linspace(0, c, num_points)

    # Create the y-coordinates.
    yt = 5*t*c*(0.2969*np.sqrt(x/c) - 0.1260*(x/c) - 0.3516*(x/c)**2 + 0.2843*(x/c)**3 - 0.1015*(x/c)**4)
    yc = np.zeros_like(x)
    dyc_dx = np.zeros_like(x)
    theta = np.zeros_like(x)

    # Calculate camber and camber gradient if the maximum camber is greater than 0.
    if m > 0:
        if p > 0 and p < 1:
            # Use the standard camber equation.
            yc[:int(p*num_points)] = m/(p**2)*(2*p*x[:int(p*num_points)] - x[:int(p*num_points)]**2/c)
            yc[int(p*num_points):] = m/((1-p)**2)*((1-2*p) + 2*p*x[int(p*num_points):]/c - x[int(p*num_points):]**2/c)
            dyc_dx[:int(p*num_points)] = 2*m/(p**2)*(p - x[:int(p*num_points)]/c)
            dyc_dx[int(p*num_points):] = 2*m/((1-p)**2)*(p - x[int(p*num_points):]/c)
        else:
            # Use a modified camber equation if the location of maximum camber is not given.
            yc = m*(x/c)**0.5*(1-x/c)
            dyc_dx = 0.5*m/c*(c-2*x)**0.5*(x/c)**-0.5
        theta = np.arctan(dyc_dx)

    # Calculate the upper and lower surface coordinates.
    xu = x - yt*np.sin(theta)
    yu = yc + yt*np.cos(theta)
    xl = x + yt*np.sin(theta)
    yl = yc - yt*np.cos(theta)

    # Reverse the order of the lower surface coordinates.
    xl = np.flip(xl)
    yl = np.flip(yl)

    # Combine the upper and lower surface coordinates.
    xcoords = np.concatenate([xu, xl])
    ycoords = np.concatenate([yu, yl])

    # Create a list of fc.Point objects.
    points = [fc.Point(x=int(xcoords[i]*1000), y=int(ycoords[i]*1000), z=0)
