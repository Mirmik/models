#!/usr/bin/env python3
#coding:utf-8
import math

import sys
sys.path.append("../")

from OCC.Display.SimpleGui import *
from occsimple.solid import *
from occsimple.geom2d import *
from occsimple.stl import *
import occsimple.util

height = 90.
radius = 40.
thickness = 3.5 

rheight = height / 2
rradius = 25

#cup = (
#	cylinder(radius, height) 
#	- cylinder(radius-thickness, height-thickness).up(thickness)
#	+ revol(circle(5).right(rradius), occsimple.base.yaxis(), math.pi)
#		.rotateY(-math.pi/2).translate([radius - 1, 0, rheight])
#)

cup = circle(30).right(40).revol(occsimple.base.yaxis(), math.pi)

model = cup.doit()
display, start_display, add_menu, add_function_to_menu = init_display()
display.DisplayShape(model)
start_display()