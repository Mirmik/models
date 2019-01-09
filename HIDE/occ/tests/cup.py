#!/usr/bin/env python3
#coding: utf-8

import sys
sys.path.append("../..")

import math
import occ.solid as solid
from occ.gui import *

def cup_base(r,h,t):
	return solid.cylinder(r, h) - solid.cylinder(r-t, h-t).up(t)

ruchka = solid.torus_part(30, 5, -math.pi, math.pi, math.pi).rotateY(math.pi/2).forward(40-1).up(90/2)
cup = cup_base(40,90,3.5) + ruchka

display(cup)
start_display()