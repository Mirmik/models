#!/usr/bin/env python3
#coding:utf-8

from zencad import *

l = 150
w = 75
z = 30
r = 55/2

m = box(l,w,z)
m = m - cylinder(r=r, h=l).rotateY(gr(90)).translate(0,w/2,z)

display(m)
show()