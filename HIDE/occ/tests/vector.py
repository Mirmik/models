#!/usr/bin/env python3
#coding: utf-8

import sys
sys.path.append("../..")

from occsimple2.geom import point, vector, axis, direction, origin, plane

vec1 = vector(5,0,0)
vec2 = vector(1,2,3)

print(vec1 + vec2)
print(vec1 ^ vec2)
print(vec1 * vec2)

print(vec1.magnitude())