#!/usr/bin/env python3
#coding: utf-8

import sys
sys.path.append("../..")

import math
import occ.solid as solid
import occ.util as util
import occ.wire as wire
import occ.algo as algo
import occ.trans as trans
import occ.stl as stl
from occ.gui import *

w = 130
h = 150
t = 2.5

wd = 20
hd = 40

z = 20

screw_radius = 1.5

m = solid.box(w, h, t).translate(-w/2,-h/2,0)
c = util.multiple_transform(solid.box(wd,hd,t).translate(-wd/2,-hd/2,0), [
	trans.translate(-w/2+wd/2,+h/2-hd/2 - z,0),
	trans.translate(+w/2-wd/2,+h/2-hd/2 - z,0),
	trans.translate(-w/2+wd/2,-h/2+hd/2 + z,0),
	trans.translate(+w/2-wd/2,-h/2+hd/2 + z,0),
])

r = util.multiple_transform(
		util.multiple_transform(
			solid.cylinder(screw_radius, t), [
				trans.translate(0,9,0),
				trans.translate(0,-9,0),
			]
		),
		[
			trans.translate(-w/2+wd+5,+h/2-hd/2 - z,0),
			trans.translate(+w/2-wd-5,+h/2-hd/2 - z,0),
			trans.translate(-w/2+wd+5,-h/2+hd/2 + z,0),
			trans.translate(+w/2-wd-5,-h/2+hd/2 + z,0),
		]
	)

model = m - c - r

stl.make_stl(model, "atombase.stl")

display(model)
start_display()