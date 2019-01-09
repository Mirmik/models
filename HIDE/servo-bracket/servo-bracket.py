#!/usr/bin/env python3
#coding:utf-8
import math

import sys
sys.path.append("../")

from OCC.Display.SimpleGui import *
import occsimple.solid as solid
import occsimple.geom2d as geom2d
import occsimple.wires as wires

from OCC.TopExp import TopExp_Explorer
from OCC.TopAbs import TopAbs_EDGE, TopAbs_FACE
from OCC.TopTools import TopTools_ListOfShape
from OCC.TopoDS import topods, TopoDS_Edge, TopoDS_Compound


from occsimple.stl import *
import occsimple.base
import occsimple.mlib


ear_width = 5
ear_length = 23
#base_length = 42
#radius = 2
#
servo_length = 40.5 + 2
servo_width = 20 + 2
servo_height = 29 + 2
#
#hole_x = 10
#hole_y = 10
#hole_deep = 4
#
servo_holes_width = 10
servo_hole_rad = 4.1 / 2.
#nut_width = 4
#nut_width_l = 6
#
h_central = 4
h_side = 1.8
h_radius = 7
#
thickness = 2
#thickness = thickness
#ear_height = servo_width + thickness
#
bot_holes_offset = 14

def servo_holes():
	return (geom2d.circle(servo_hole_rad)
		.multiply_translate([[0,0], [0,servo_holes_width], [48.5,0], [48.5,servo_holes_width]])
		.linear_extrude(thickness+0.1)
		.rotateX(math.pi/2)
		.translate([-thickness/2, thickness+0.1, servo_width/2+thickness-servo_holes_width/2])
)

#def servo_holes_pack():
#	return (
#		servo_holes()  
#		+ geom2d.rectangle([nut_width_l, nut_width], rounded = (1, [0,1]), center=True)
#		.linear_extrude(2*thickness+servo_length)
#		.rotateY(math.pi/2)
#		.multiply_translate([[0, 0, -servo_holes_width/2], [0, 0, +servo_holes_width/2]])
#		.translate([0, thickness+nut_width/2, servo_width/2+thickness])
#	)


def back_holes():
	return (occsimple.mlib.central_circles_array(h_side, h_side, h_radius, 4)
		.linear_extrude(thickness)
		.rotateX(math.pi / 2)
		.translate([servo_length / 2 + thickness, thickness+servo_height, servo_width/2+thickness])
		.multiply_translate([[-servo_length/4,0,0], [+servo_length/4,0,0]])
)

def bot_holes():
	return (
		occsimple.mlib.central_circles_array(h_central, h_side, h_radius, 4)
		.linear_extrude(thickness)
		.translate([servo_length / 2 + thickness, 0])
		.multiply_translate([
			[0, (thickness+servo_height) -bot_holes_offset],
			[-servo_length/4, (thickness+servo_height) -bot_holes_offset -servo_length/4],
			[+servo_length/4, (thickness+servo_height) -bot_holes_offset -servo_length/4]
		])
	)

def servo_box(internal, thickness):
	return (solid.box([internal[0]+2*thickness, internal[1]+thickness, internal[2]+thickness]) 
		- solid.box(internal).translate([thickness,0,thickness]))

ear = occsimple.mlib.rounded_angle(ear_length, servo_width+thickness, ear_width, thickness, [1,3])

#base = solid.box([,20,30])
#servo_box = base - solid.box(base.size - solid.vector3d([2*thickness, thickness, thickness])).translate([thickness,0,thickness])

def rrr(y, x):
	return (geom2d.rectangle([x, y], rounded = (1.5, [0,1,2,3]))
		.linear_extrude(thickness)
		.rotateY(math.pi/2)
		.translate([0, thickness, x + thickness]))

fst = 10
yst = 10

model = (
	servo_box([servo_length, servo_height, servo_width], thickness)
	+ (geom2d.rectangle([servo_length, 4], rounded = (2, [2,3])).linear_extrude(thickness)
			.translate([thickness, -4]))
	+ ear.translate([-ear_width,0,0])
	+ ear.mirror([1,0,0]).translate([servo_length + thickness * 2 + ear_width, 0, 0])
	#- servo_holes()
	
	#- geom2d.rectangle([hole_x,hole_y], rounded = (3, [0,1,2,3]))
	#	.linear_extrude(servo_length+thickness*2)
	#	.rotateY(math.pi/2)
	#	.translate([0, servo_height/2 + hole_deep, hole_y/2 + (servo_width)/2 + thickness])

	- servo_holes()#.mirror([0,1,-1])
	- servo_holes().mirror([0,1,-1])

	- back_holes()
	- bot_holes()

	- (
		rrr(fst,yst)
		+ rrr(fst,servo_width - yst - thickness * 2)
			.translate([0,0,yst + thickness])
		+ rrr(servo_height - thickness*2 - fst, servo_width - thickness)
			.translate([0,fst + thickness,0])
	).multiply_translate([[0,0,0], [servo_length+thickness,0,0]])

)

#model = geom2d.rectangle([20,40], rounded = (2, [1,2])).right(40).mirror([1,1,0]) + geom2d.rectangle([20,40], rounded = (2, [1,2])).right(40)
#s = solid.box(4)
#model = s.right(20).rotateZ(2*math.pi / 4 * 3)
#model2 = s.right(20).rotateZ(2*math.pi / 4 * 2)
#model3 = model + model2

occsimple.stl.make_stl(model, "servo_bracket.stl", 0.05)

display, start_display, add_menu, add_function_to_menu = init_display()
display.DisplayShape(model.doit())
#display.DisplayShape(model2.doit())
#display.DisplayShape(model3.doit())
start_display()