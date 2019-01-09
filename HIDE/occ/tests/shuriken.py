#!/usr/bin/env python3
#coding: utf-8

import sys
sys.path.append("../..")

import math
import occ.solid as solid
import occ.util as util
import occ.wire as wire
import occ.algo as algo
import occ.stl as stl
from occ.gui import *

l = 55
r = 18
c = 10

pts = util.points([
	(0, l, 0),
	(r, r, 0),
	(l, 0, 0),
	(r, -r, 0),
	(0, -l, 0),
	(-r, -r, 0),
	(-l, 0, 0),
	(-r, r, 0),
]) 

m = wire.polysegment(pts, closed = True).face() - wire.circle(10).face()
m = m.linear_extrude(4)

stl.make_stl(m, "shuriken.stl", 0.01)

display(m)
start_display()