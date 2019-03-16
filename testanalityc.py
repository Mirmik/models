#!/usr/bin/env python3
#coding: utf-8

from zencad import *
import numpy

xcoords = numpy.linspace(-10,10,50)
ycoords = numpy.linspace(-10,15,50)

lines = [ interpolate([point(x, y, 0.01*(x**2 + y**3)) for x in xcoords]) for y in ycoords ]

wires = []

for l in lines:
	trans = translate(0,0,-30)
	sf = l.endpoints()
	w=sew([l, segment(sf[0], trans(sf[0])), trans(l), segment(sf[1], trans(sf[1]))])
	wires.append(w)

for l in lines:
	disp(l.left(30))

disp(loft(wires) - halfspace().down(10))

show()
