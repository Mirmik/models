#!/usr/bin/env python3

from zencad import *

pnts = [(0,0), (0,10), (10,20)]
tangs = [(0,0), (0,0), (1,0)]
m0 = interpolate(pnts, tangs)
m1 = interpolate(pnts)

display(m0)
display(m1)
show()