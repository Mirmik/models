#!/usr/bin/env python3
#coding: utf-8

import sys
sys.path.append("../..")

from occsimple2.geom import point, vector, axis, direction, origin, plane

pnt = point(3,6,7)
pnt0 = point(3,6,89)

pln = plane(point(0,0,1), direction(0,0,1))
print(pnt.mirror(pln))