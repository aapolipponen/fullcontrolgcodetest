import fullcontrol as fc
from math import tau, sin



initial_settings = {
    "extrusion_width": 0.8,
    "extrusion_height": 0.3,
    "e_units": "mm3",
    "dia_feed": 1.75,
    "primer": "no_primer",
    "print_speed": 200,
    "travel_speed": 400
}
gcode_controls = fc.GcodeControls(printer_name='custom', initialization_data=initial_settings)
starting_procedure_steps = []
starting_procedure_steps.append(fc.ManualGcode(text='\n; #####\n; ##### beginning of start procedure\n; #####'))
starting_procedure_steps.append(fc.ManualGcode(text='G28 ; home'))
starting_procedure_steps.append(fc.GcodeComment(text='heat bed 10 degrees too hot'))
starting_procedure_steps.append(fc.Buildplate(temp=60, wait=True))
starting_procedure_steps.append(fc.GcodeComment(text='allow bed to cool to the correct temp and heat up nozzle'))
starting_procedure_steps.append(fc.Hotend(temp=220, wait=False))
starting_procedure_steps.append(fc.Buildplate(temp=50, wait=True))
starting_procedure_steps.append(fc.Hotend(temp=220, wait=True))
starting_procedure_steps.append(fc.Fan(speed_percent=100))
starting_procedure_steps.append(fc.Extruder(relative_gcode=True))
starting_procedure_steps.append(fc.Point(x=10, y=10, z=0.4))
starting_procedure_steps.append(fc.ManualGcode(text='; #####\n; ##### end of start procedure\n; #####\n'))


# create the design
design_steps = []

layer2z = 25
layer3z = 50
layer4z = 75

centre_point = fc.Point(x=75, y=75, z=0)
radius = 50
start_angle = 0
arc_angle = 1*tau
segments = 64
clockwise = True

centre_point2 = fc.Point(x=75, y=75, z=layer2z)
radius2 = 35
start_angle2 = 0
arc_angle2 = 1*tau
segments2 = 64
clockwise2 = True



design_steps.extend(fc.arcXY(centre_point, radius, start_angle, arc_angle, segments))
design_steps.append(fc.PlotAnnotation(point=design_steps[-1], label="end"))
design_steps.append(fc.PlotAnnotation(point=design_steps[0], label="start"))
design_steps.append(fc.PlotAnnotation(point=centre_point, label="centre"))
design_steps.append(fc.Point(x=110, y=75, z=layer2z))
design_steps.extend(fc.travel_to(fc.Point(x=25, y=75, z=0)))
design_steps.append(fc.Point(x=40, y=75, z=layer2z))
design_steps.extend(fc.travel_to(fc.Point(x=75, y=125, z=0)))
design_steps.append(fc.Point(x=75, y=110, z=layer2z))
design_steps.extend(fc.travel_to(fc.Point(x=75, y=25, z=0)))
design_steps.append(fc.Point(x=75, y=40, z=layer2z))
design_steps.extend(fc.travel_to(fc.Point))


design_steps.extend(fc.arcXY(centre_point2, radius2, start_angle2, arc_angle2, segments2))
design_steps.append(fc.PlotAnnotation(point=design_steps[-1], label="end"))
design_steps.append(fc.PlotAnnotation(point=design_steps[0], label="start"))
design_steps.append(fc.PlotAnnotation(point=centre_point2, label="centre"))

fc.transform(design_steps, 'plot', fc.PlotControls(color_type='print_sequence'))


#steps = starting_procedure_steps + design_steps
#gcode_controls = fc.GcodeControls(save_as='my_design')
#fc.transform(steps, 'gcode', gcode_controls)