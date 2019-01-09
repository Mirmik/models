#!/usr/bin/env python3
#coding: utf-8

from OCC.Display.SimpleGui import *

import sys
sys.path.append("../..")

import math

from occ.geom import origin, axisOX, direction, point
from occ.trans import translate
import occ.solid as solid
import occ.curve as curve

b = solid.box(4,4,4).translate(-10,0,0)
s = solid.sphere(5).translate(0,10,0)
c = solid.cylinder(3,5).rotateX(math.pi/2)
p = solid.part_sphere(5, 0, math.pi/2, math.pi/2).translate(10,0,0)
t = solid.torus(8,3).up(10)

model = b + c + s + p + t

display, start_display, add_menu, add_function_to_menu = init_display()
display.DisplayShape(model.get())
display.DisplayShape(curve.curveOX().get())
display.DisplayShape(curve.curveOY().get())
display.DisplayShape(curve.curveOZ().get())
#display.DisplayShape(curve.bezier([point(0,0,10), point(0,0,20), point(0,10,0), point(-10,10,0)]).get())

#display.DisplayShape(origin().pnt)
start_display()