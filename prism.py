#!/usr/bin/env python3
#coding:utf-8

from zencad import *

m = cylinder(r = 60, h = 80)
m = m - halfspace().rotateX(-deg(120)).back(60) - halfspace().rotateX(deg(120)).forw(60) 
top = m

m = cylinder(r=60, h = 200)
bot = m

m = bot + top.up(200)
body = m.up(200)

m = sphere(r=250)
m = body + m

m = m - rotate_array(6)(cylinder(r=100,h=800,center=True).left(250))
m = m.up(200+200) + cylinder(r = 80, h=400,center=True)

m = m.up(600) + cone(h = 400, r2 = 120, r1 = 200)

display(m)
show()