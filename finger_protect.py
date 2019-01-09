#!/usr/bin/env python3
 
from zencad import *

h = 10
t = 0.5

r = 6.5
  
m = (
	(cylinder(r=r, h=h) + sphere(r=r).up(h)) -
	(cylinder(r=r-t, h=h) + sphere(r=r-t).up(h)) -
	box(100,100,100).left(50) -
	box(100,100,100).translate(-50, 0, -100).rotateX(gr(45)).back(2)
)

display(m)
show()