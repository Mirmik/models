#!/usr/bin/env python3
#coding: utf-8

import math
import zencad
from zencad import *

import base

m1 = base.shpingalet_base(54, True)
m2 = base.shpingalet_base(10, False)

scn = Scene()
scn.add(m1.back(54/2).unlazy(), color = color(0.6,0.8,0))
scn.add(m2.forw(10/2).unlazy(), color = color(0.8,0.6,0))

to_stl(m1, "m1.stl", 0.001)
to_stl(m2, "m2.stl", 0.001)

show(scn)