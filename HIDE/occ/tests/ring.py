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

inrad = 15
obr = 2 
rad = inrad + obr
ang = 60
sphrad = 5

pts = util.points([
	(0,0,0), 
	(40 * math.sin(util.degree(ang/2)),40 * math.cos(util.degree(ang/2)),0), 
	(40 * math.sin(util.degree(-ang/2)),40 * math.cos(util.degree(-ang/2)),0)
])

c = solid.cylinder(40,10).down(10+1.8) 
d = wire.polysegment(pts, True).face().linear_extrude(20).down(10) #- solid.box(20,20,20).down(10)
b = solid.torus(rad, obr) - d
s1 = solid.sphere(sphrad).translate(rad * math.sin(util.degree(ang/2)),rad * math.cos(util.degree(ang/2)),0)
s2 = solid.sphere(sphrad).translate(rad * math.sin(util.degree(-ang/2)),rad * math.cos(util.degree(-ang/2)),0)

#m = b
m = (b + s1 + s2) - c 

stl.make_stl(m, "ring.stl", 0.01)

display(m)
start_display()