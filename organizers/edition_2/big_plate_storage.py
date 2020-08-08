#!/usr/bin/env python3
#coding: utf-8

import runpy
from zencad import *
from big_plate_param import *

organizer = runpy.run_path("../base/organizer.py")


m = organizer["storage"](m=vm,n=vn,w=x,h=z,l=y,t=t,d=10,d2=z/2)

x = x*vm+t*(vm+1)
y = z*vn+t*(vn+1)
m = m.move(x/2, -y/2) 

s = cylinder(r =20, h = 3)
s2 = cube(3).move(-3,-3)

for o in [10+25*i for i in range(6)]:
	m -= sqrmirror()(sphere(5).move(x/2,y/2,o))
	#m -= sqrmirror()(s.move(x/2,y/2,o))
	#m += sqrmirror()(s2.move(x/2,y/2,o))

for o in [10+25*i for i in range(6)]:
	m -= sqrmirror()(sphere(5).move(0,y/2,o))

#wideline(segment((), ()))

to_stl(m, "./big_plate_storage.stl", 0.01)
display(m)
show()


