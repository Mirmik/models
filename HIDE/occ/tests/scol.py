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

m = solid.cylinder(65 + 7, 15) - solid.cylinder(65, 15) - solid.box(300,300,15)

stl.make_stl(m, "scol.stl")

display(m)
start_display()