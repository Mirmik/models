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

m = solid.cylinder(1.5, 10)

stl.make_stl(m, "cylinder.stl", 0.01)

display(m)
start_display()