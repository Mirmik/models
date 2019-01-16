#!/usr/bin/env python3
#coding: utf-8

from zencad import *

t = 3.5

ro = 16.5
ri = ro - t
s = 22
angle = 25

rd = 3.5
rhole= 2.5/2

p1_base = cylinder(h=12.5, r=ro, center=True)
p1 = cylinder(h=12.5, r=ro, center=True) - cylinder(h=12.5, r=ri, center=True) - box(s, 100, 12.5).left(s/2).down(12.5/2)

p1 = p1.fillet(r=0.5).forw(ro).rotateX(deg(25))
p1_base = p1_base.forw(ro).rotateX(deg(25))

hold = (cylinder(h=26, r=9.5/2) - cylinder(h=26, r=rhole)).down(3).rotateX(deg(90)) - p1_base 

m = p1 + hold
m = m - halfspace().down(rd)

display(m)



show()