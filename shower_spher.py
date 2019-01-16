#!/usr/bin/env python3
#coding: utf-8

from zencad import *

r=7.5

m = sphere(r=r) - cylinder(r=3.1/2, h = 100 , center=True) - halfspace().down(r-3)
m = m.up(r-3) - cylinder(r=7/2, h=4)

display(m)
show()