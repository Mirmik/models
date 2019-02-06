#!/usr/bin/env python3
#coding:utf-8

from zencad import *

m = cylinder(r = 30, h = 40) - cylinder(r = 10, h = 40) 
#p = point(20, 5, 0)

m = chamfer(m, 1, [(0,10,40), (30,10,40)])
disp(m)

show()

