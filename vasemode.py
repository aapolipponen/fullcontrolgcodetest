from math import cos, tau
import fullcontrol as fc
layers = 50
segments_per_layer = 64
centre = fc.Point(x=50, y=50, z=0)
layer_height = 0.4
steps = []
for i in range(layers*segments_per_layer+1):
    # find useful measures of completion
    layer_fraction = (i%segments_per_layer)/segments_per_layer
    total_fraction = (int(i/segments_per_layer)+layer_fraction)/layers
    # calculate polar details
    angle = layer_fraction*tau
    radius = 20+5*cos(tau*(total_fraction))
    centre.z = layer_height*layers*total_fraction
    # add point
    steps.append(fc.polar_to_point(centre, radius, angle))
fc.transform(steps, 'plot', fc.PlotControls(zoom=0.8))