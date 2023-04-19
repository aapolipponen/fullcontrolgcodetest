import fullcontrol as fc
import numpy as np

def calculate_points_on_circle(r, num_points):
    # Calculate the angle between each point using tau
    angle = 2 * np.pi / num_points

    # Calculate the coordinates of each point using numpy
    theta = np.arange(num_points) * angle
    x = r * np.cos(theta)
    y = r * np.sin(theta)

    # Combine the x and y coordinates into a single array of points
    points = np.column_stack((x, y))

    return points

#create the design
centre = fc.Point(x=100, y=100, z=0)
r = 75

steps = fc.circleXY(centre, r, 0, 64, True)
steps.append(fc.PlotAnnotation(point=steps[-1], label="start/end"))
steps.append(fc.PlotAnnotation(point=steps[1], label="first point after start"))
steps.append(fc.PlotAnnotation(point=centre, label="centre"))

num_points = 8
points_on_circle = calculate_points_on_circle(r, num_points)

point_list = [fc.Point(x=x + centre.x, y=y + centre.y, z=0) for x, y in points_on_circle]

steps.extend(point_list)

fc.transform(steps, 'plot', fc.PlotControls(color_type='print_sequence'))
