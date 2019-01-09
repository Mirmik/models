#!/usr/bin/env python3
#coding: utf-8

from OCC.Display.SimpleGui import *

import sys
sys.path.append("../..")

import occ.geom as geom
from occ.curve import circle
import occ.curve as curve


display, start_display, add_menu, add_function_to_menu = init_display()
display.DisplayShape(circle(3, plane = geom.planeOXY()).get())
display.DisplayShape(circle(3, plane = geom.planeOXZ()).get())
display.DisplayShape(circle(3, plane = geom.planeOYZ()).get())
display.DisplayShape(circle(3, plane = geom.plane(geom.origin(), geom.direction(1,1,0))).get())
display.DisplayShape(circle(3, plane = geom.plane(geom.origin(), geom.direction(1,0,1))).get())
display.DisplayShape(circle(3, plane = geom.plane(geom.origin(), geom.direction(0,1,1))).get())
display.DisplayShape(circle(3, plane = geom.plane(geom.origin(), geom.direction(1,-1,0))).get())
display.DisplayShape(circle(3, plane = geom.plane(geom.origin(), geom.direction(1,0,-1))).get())
display.DisplayShape(circle(3, plane = geom.plane(geom.origin(), geom.direction(0,1,-1))).get())

display.DisplayShape(curve.lineOX().get())
display.DisplayShape(curve.lineOY().get())
display.DisplayShape(curve.lineOZ().get())
#display.DisplayShape(curve.line(geom.origin(), geom.direction(1,1,0)).get())
#display.DisplayShape(curve.line(geom.origin(), geom.direction(1,0,1)).get())
#display.DisplayShape(curve.line(geom.origin(), geom.direction(0,1,1)).get())
#display.DisplayShape(curve.line(geom.origin(), geom.direction(1,-1,0)).get())
#display.DisplayShape(curve.line(geom.origin(), geom.direction(1,0,-1)).get())
#display.DisplayShape(curve.line(geom.origin(), geom.direction(0,1,-1)).get())

#display.DisplayShape(origin().pnt)
start_display()