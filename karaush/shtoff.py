#!/usr/bin/env python3

from zencad import *

a = 150-7
a2 = 17 - 7
b = 9.5
b2 = 12
c = 1.5

m0 = box(a, b, c, center=True) 
m1 = box(a, c, b, center=True)
m = m0 + m1

m = m.left(a/2)

m = m + box(a2, c, b2, center=True).left(a2/2)
m = m + box(a2, b2, c, center=True).left(a2/2)
m = m + cylinder(r=7.25, h=2).rotateY(deg(90))
m = m.left(2)

m = m + cylinder(r=5.5, h=3.5).rotateY(deg(90))
m = m.left(3.5)

m = m + cylinder(r=7.25, h=1.5).rotateY(deg(90))
m = m.left(1.5)

m = m.rotateY(deg(90))

m = m - rotate_array(2)(box(3.25,1,5, center=True).up(2.5).left(7.25-3.25/2))

m = m.rotateY(deg(90))

disp(m)
show()