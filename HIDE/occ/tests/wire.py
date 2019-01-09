#!/usr/bin/env python3
#coding: utf-8

import sys
sys.path.append("../..")

from occ.trans import *
from occ.geom import plane, point, direction, frame, origin
from occ.wire import circle, square, segment, rectangle
from occ.gui import display, start_display
import occ.solid as solid 
import occ.util as util

#c = rectangle(20,10,center=True)
#s = circle(10)
#d = rectangle(10,5,center=True)

#polygon = c.face() + s.face() - d.face()

#m = util.difference(
#	polygon.linear_extrude(7),
#	solid.cylinder(3, 100, center=True).locframe((0,0,3.5), (0,1,0)),
#	solid.cylinder(3, 100, center=True).locframe((0,0,3.5), (1,0,0))
#)

#m = solid.box(3,6,20).locframe(frame(point(0,0,0),direction(1,0,0)), frame(point(0,0,0),direction(0,0,1)))

h = util.multiple_transform(
	solid.cylinder(3,100).rotateY(util.degree(90)).right(20), 
	(
		[rotateZ(n * util.degree(60)) for n in range(0,6)] + 
		[rotateZ(n * util.degree(60)) * rotateY(util.degree(45)) for n in range(0,6)] +
		[rotateZ(n * util.degree(60)) * rotateY(util.degree(-45)) for n in range(0,6)] +
		[ rotateY(util.degree(-90)), rotateY(util.degree(90)) ]
	)
) + solid.sphere(22)

display(h)
display(origin())
start_display()
