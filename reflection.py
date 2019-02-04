#!/usr/bin/env python3
#coding:utf-8

from zencad import *

m = box(10)
#p = point(20, 5, 0)

r = m.fillet(1, refs=[(5, 30, 0), (5,0,0), (0,5,0)])
disp(r, Color(1,0,0))

show()

