import fullcontrol as fc
import numpy as np

def calculate_points_on_circle(r, num_points):
    # Calculate the angle between each point using tau
    angle = 2 * np.pi / num_points

    # Calculate the coordinates of each point using numpy
    theta = np.linspace(0, 2*np.pi, num_points, endpoint=False)
    x, y = r * np.cos(theta), r * np.sin(theta)

    # Combine the x and y coordinates into a single array of points
    points = np.column_stack((x, y))

    return points

#create the design
centre = fc.Point(x=100, y=100, z=0)
r = 75

steps = [fc.PlotAnnotation(point=centre, label="centre")]

num_points = 16
points_on_circle = calculate_points_on_circle(r, num_points)

point_list = [fc.Point(x=x + centre.x, y=y + centre.y, z=0) for x, y in points_on_circle]
steps.extend(point_list)

# Draw the lines between the points
for i in range(num_points):
    steps.append(fc.Point(x=point_list[i].x, y=point_list[i].y, z=0))
    steps.append(fc.Point(x=point_list[(i+1)%num_points].x, y=point_list[(i+1)%num_points].y, z=0))

fc.transform(steps, 'plot', fc.PlotControls(color_type='print_sequence'))
