#!/usr/bin/env python3
#coding: utf-8

import sys
sys.path.append("../..")

import occ.util as util
from occ.geom import point
from occ.edge import segment
from occ.wire import make_wire
from occ.gui import display, start_display

pts = util.points([
	(0,0,0),
	(1,0,0),
	(1,1,0),
	(0,1,0),
])

wr = make_wire([
	segment(pts[0], pts[1]), 
	segment(pts[1], pts[2]),
	segment(pts[2], pts[0])
])

display(wr)

start_display()
