#!/usr/bin/env python3
#coding: utf-8



import zencad

r0 = 40
r1 = 35
r2 = 30
r3 = 25
r4 = 20
r5 = 15
r6 = 10

h = 40
t = 0.5

m0 = zencad.sphere(r = r0) - zencad.sphere(r = r1 + t)
m1 = zencad.sphere(r = r1) - zencad.sphere(r = r2 + t)
m2 = zencad.sphere(r = r2) - zencad.sphere(r = r3 + t)
m3 = zencad.sphere(r = r3)

m = m0 + m1 + m2 + m3
m = (
	m 
	- zencad.halfspace().mirrorXY().up(h/2) 
	- zencad.halfspace().down(h/2)
)

zencad.display(m)
zencad.show()
