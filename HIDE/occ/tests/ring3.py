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

r = 40 / 2
s = 3

up = r * math.sin(util.degree(60)) 
side = r * math.cos(util.degree(60))

t0 = solid.torus(r, s)
t1 = solid.torus(r, s).rotateX(util.degree(-60)).up(up).forward(side)
t2 = solid.torus(r, s).rotateX(util.degree(60)).up(up).backward(side)

m = t0 + t1 + t2

stl.make_stl(m, "ring3.stl", 0.01)

display(m)
start_display()