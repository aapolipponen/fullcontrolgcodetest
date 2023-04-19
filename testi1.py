import fullcontrol as fc
import math

#create the design
steps = []

centre = fc.Point(x=100, y=100, z=0)
centre_point = centre
origin = centre
layer1radius = 75

r = layer1radius

centre_point = fc.Point(x=100, y=100, z=0)
radius = r
start_angle = 0
segments = 64
clockwise = True
steps = fc.circleXY(centre_point, radius, start_angle, segments, clockwise)
steps.append(fc.PlotAnnotation(point=steps[-1], label="start/end"))
steps.append(fc.PlotAnnotation(point=steps[1], label="first point after start"))
steps.append(fc.PlotAnnotation(point=centre_point, label="centre"))

def calculate_points_on_circle(r, num_points):
    # Calculate the angle between each point using tau
    angle = 2 * math.pi / num_points

    # Calculate the coordinates of each point
    points = []
    for i in range(num_points):
        x = r * math.cos(i * angle)
        y = r * math.sin(i * angle)
        points.append((x, y))

    return points

num_points = 8
points_on_circle = calculate_points_on_circle(r, num_points)

point_list = []
for i in range(num_points):
    x = points_on_circle[i][0] + centre.x
    y = points_on_circle[i][1] + centre.y
    point = fc.Point(x=x, y=y, z=0)
    point_list.append(point)

# Print the resulting list of fc.Point objects
for point in point_list:
    print(point)

for point in point_list:
    steps.append(fc.Point(x=point.x, y=point.y, z=point.z))
    


fc.transform(steps, 'plot', fc.PlotControls(color_type='print_sequence'))

#gcode_controls = fc.GcodeControls(save_as='my_design')
#fc.transform(steps, 'gcode', gcode_controls)