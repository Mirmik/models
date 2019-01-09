#!/usr/bin/env python3
#coding: utf-8

from OCC.Display.SimpleGui import *

import sys
sys.path.append("../..")

from occ.trans import *
import occ.geom as geom
import occ.curve as curve
import math

import occ.solid as solid

a0 = curve.line(geom.point(0,0,0), geom.direction(0,0,1))
b0 = curve.line(geom.point(10,0,0), geom.direction(0,0,1))
c0 = curve.line(geom.point(10,10,0), geom.direction(0,0,1))
d0 = curve.line(geom.point(0,10,0), geom.direction(0,0,1))

a1 = curve.line(geom.point(0,0,0), geom.direction(0,1,0))
b1 = curve.line(geom.point(10,0,0), geom.direction(0,1,0))
c1 = curve.line(geom.point(10,0,10), geom.direction(0,1,0))
d1 = curve.line(geom.point(0,0,10), geom.direction(0,1,0))

a2 = curve.line(geom.point(0,0,0), geom.direction(1,0,0))
b2 = curve.line(geom.point(0,0,10), geom.direction(1,0,0))
c2 = curve.line(geom.point(0,10,10), geom.direction(1,0,0))
d2 = curve.line(geom.point(0,10,0), geom.direction(1,0,0))

d3 = curve.curve(geom.circle(10).translated(5,5,20))

b = solid.box(10,10,10) + solid.cylinder(5,8).up(10).right(5).forward(5)

display, start_display, add_menu, add_function_to_menu = init_display()
display.DisplayShape(a0.native())
display.DisplayShape(b0.native())
display.DisplayShape(c0.native())
display.DisplayShape(d0.native())

display.DisplayShape(a1.native())
display.DisplayShape(b1.native())
display.DisplayShape(c1.native())
display.DisplayShape(d1.native())

display.DisplayShape(a2.native())
display.DisplayShape(b2.native())
display.DisplayShape(c2.native())
display.DisplayShape(d2.native())

display.DisplayShape(b.native())
display.DisplayShape(d3.native())

#display.DisplayShape(curve.lineOX().native())
#display.DisplayShape(curve.lineOY().native())
#display.DisplayShape(curve.lineOZ().native())

start_display()