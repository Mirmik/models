#!/usr/bin/env python3
#coding: utf-8

import zencad
from zencad import pnt
import zencad.face
import zencad.solid as solid
import zencad.stl as stl
from zencad.widget import display, show

import math

l = 200 * math.sqrt(2) * 0.9
w = 10

m = zencad.face.polygon([
	pnt(0,0),
	pnt(0,w),
	pnt(l,w),
	pnt(l,0),
])

m = solid.linear_extrude(m, (0,0,1))
stl.make_stl("rem.stl", m)

#display(m)
#show()