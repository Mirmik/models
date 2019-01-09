#!/usr/bin/env python3

from zencad import *
import evalcache

lazy.diag=True

m = box(50)
m = m.fillet(refs=[
	point3(30,0,50.000),
	point3(50.000,20.904,49.965)
], r=3, epsilon=0.1)

display(m)
show()