#!/usr/bin/env python3

from zencad import *

base = box(60, 18, 10, center=True).fillet(3)
m = base + base.rotateZ(deg(90))

m = (m 
	- cylinder(r = 2.7, h=10).down(5) 
	- cylinder(r = 4.5, h=10).up(2) 
	- square(7, center=True).fillet(1.5).extrude(-10)
)
disp(m)
show()
