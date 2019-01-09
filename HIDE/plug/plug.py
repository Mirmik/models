#!/usr/bin/env python3
#coding: utf-8

import sys
sys.path.insert(0, "..")

import zencad.solid as solid
import zencad.wire as wire
import zencad.math3
from zencad.widget import *

rs =4
r = 2.8
l = 50

s2r = 3.4

s = solid.sphere(rs) - solid.box(30, 30, 10, center = True).down(7)
c = (solid.cylinder( r, l) + solid.sphere(r).up(l)
	+ solid.sphere(s2r).up(l)
	+ solid.sphere(s2r).up(l/2)
	+ solid.sphere(s2r).up(l/4)
	+ solid.sphere(s2r).up(l/4*3)
) - solid.box(30, 30, 10, center = True).up(7.5 + l)


display(s + c)
show()