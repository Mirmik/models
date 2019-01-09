#!/usr/bin/env python2
#coding: utf-8

import sys
sys.path.append('../python-model-lib')

from solid import *
from solid.utils import *

from solidlib import *

ear_width = 8
ear_length = 23
#deep = 34
base_length = 42
radius = 2
width = 2

servo_length = 40.5 + 2
servo_width = 20 + 2
servo_height = 29 + 2

ear_height = servo_width + width

hole_x = 10
hole_y = 10
hole_deep = 5

servo_holes_width = 10
servo_hole_rad = 4.1 / 2.
nut_width = 3
nut_width_l = 6

h_central = 4
h_side = 1.8
h_radius = 7

def box(internal, width):
	return (cube([internal[0]+2*width,internal[1]+width,internal[2]+width]) 
		- translate([width,0,width])(cube(internal)))

ear = rounded_angle(ear_length,servo_width+width,ear_width,width, [1,3])

servo_holes = chain(
		linear_extrude(width+0.1),
		rotate([90,0,0]),
		translate([-width/2, width+0.1, servo_width/2+width-servo_holes_width/2]),
	) (multiply_translate([[0,0], [0,servo_holes_width], [48.5,0], [48.5,servo_holes_width]])(circle(r = servo_hole_rad)))

back_holes = chain(
		linear_extrude(width+0.1),
		rotate([90,0,0]),
		translate([servo_length / 2, width+0.1+servo_height, servo_width/2+width]),
		multiply_translate([[-h_radius,0,0], [+h_radius,0,0]]),
	) (central_circles_array(h_central, h_side, h_radius, 4)),

servo_holes_pack = union()(
	servo_holes 
	+ chain(
		linear_extrude(2*width+servo_length),
		rotate([0,90,0]),
		multiply_translate([[0, 0, -servo_holes_width/2], [0, 0, +servo_holes_width/2]]),	
		translate([0, width+nut_width/2+width/2, servo_width/2+width]),
	)(rounded_square([nut_width_l, nut_width], 1, [0,1], center=True)))


model = (
	union() (
		translate([-ear_width,0,0])(ear),
		translate([servo_length + width * 2 + ear_width, 0, 0])(mirror([1,0,0])(ear)),
		box([servo_length,servo_height,servo_width], width),
	)
	- translate([0, servo_height/2 + hole_deep, hole_y/2 + (servo_width)/2 + width]) (
		rotate([0,90,0])(linear_extrude(servo_length+width*2)(rounded_square([hole_x,hole_y], 3, [0,1,2,3]))))
	
	- servo_holes_pack
	- mirror([0,1,-1])(servo_holes_pack)
	- back_holes
)

#model = box([base_length, deep, ear_height], width)
#model = bothole
model_text = scad_render(model, file_header='$fn = 40;')

print(model_text)

file = open("servo-bracket-gen.scad","w")
file.write(model_text)
file.close