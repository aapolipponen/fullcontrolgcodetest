import fullcontrol as fc

# create points
point1 = fc.Point(x=100, y=100, z=0)
point2 = fc.Point(x=200, y=200, z=0)

# create a line
line = fc.Line(start=point1, end=point2, color="#ff0000")

# create a scene
scene = fc.Scene(objects=[line])

# display the scene
fc.display(scene)
