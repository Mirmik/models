#!/usr/bin/env python3.5
#coding: utf-8

from zencad import *

servo_length = 40.5 + 2
servo_width = 20 + 2
servo_height = 29 + 2

thickness = 2

#zzz = execfile("another.py")["zzz"]

def servo_box(x, y, z, t):
	return box(x+2*t, y+t, z+t) - box(x,y,z).translate(t,0,t)

model = (
	  servo_box(servo_length, servo_height, servo_width, thickness) 
	+ linear_extrude(rectangle(servo_length, 4).fillet(2,[0,3]), (0,0,thickness)).translate(thickness, -4, 0)
)

display(model)
show()