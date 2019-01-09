#!/usr/bin/env python3
#coding: utf-8

import math
import sys
sys.path.append("../..")

from occsimple2.geom import point, vector, axis, direction, origin, plane, frame
from occsimple2.geom import axisOX, axisOY, axisOZ 
from occsimple2.trans import translate, rotate, mirror, scale, rotateX, rotateY, rotateZ, transformation
from occsimple2.trans import mirrorX, mirrorY, mirrorZ, planeXY, planeXZ, planeYZ

frm = frame(point(0,0,7), direction(0,0,1), direction(1,0,0))
pln = plane(point(0,0,7), direction(0,0,1), direction(1,0,0))
#print(frm.dirs())

#trsf = transformation(frm)
#trsf = transformation().set_rotation(axisOX(), 0.5*math.pi)
trsf = translate(5,5,5).invert()

#print(vector(0,0,3).transformed(trsf))
print(point(0,1,1).transformed(trsf))

#print(frm.location())
#print(pln.dirs())