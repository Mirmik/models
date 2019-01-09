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

thickness = 2

m = solid.cylinder(35/2, 35) - solid.cylinder(35/2 - thickness, 35 - thickness).up(thickness)

stl.make_stl(m, "minicup.stl", 0.01)

display(m)
start_display()