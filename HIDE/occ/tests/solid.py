#!/usr/bin/env python3
#coding: utf-8

from OCC.Display.SimpleGui import *

import sys
sys.path.append("../..")

from occ.solid import box, wedge, sphere, part_sphere, cylinder, torus, cone
from occ.geom import origin, planeOXY
from occ.util import union
import math

from occ.stl import make_stl

def king(r1,r2,r3,r31,r4,h1,h2,h3):
	return union(
		cylinder(r1,h1),
		cone(r1,r2,h2).up(h1),
		cone(r2,r31,h3/2).up(h1+h2),
		cone(r31,r3,h3/2).up(h1+h2+h3/2),
		torus(r3,r4).up(h1+h2+h3),
		box(3,3,10,center_xy=True).up(h1+h2+h3),
		cone(0,4,7).up(h1+h2+h3)
	)

b = king(r1=10, r2=6, r3=4, r31=3.5, r4=2, h1=4, h2=4, h3 = 25).mirror(planeOXY())

make_stl(b, "king.stl",300)

display, start_display, add_menu, add_function_to_menu = init_display()
display.DisplayShape(b.doit())
#display.DisplayShape(origin().pnt)
start_display()