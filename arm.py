#!/usr/bin/env python3
#coding: utf-8

from zencad import *
import time

c = cylinder(h=100, r=5)
s = sphere(r=10)

z = c + s + s.up(100)

scn = Scene()

ctr1 = scn.add(z.unlazy())
ctr2 = scn.add(z.rotateX(deg(45)).unlazy())
ctr3 = scn.add(z.rotateY(deg(90)).unlazy())

def animate(widget):
	
	i = time.time()
	trsf = rotateY(i)
	trsf2 = trsf * translate(0,0,100) * rotateZ(i)
	trsf3 = trsf2 * rotateX(deg(45)) * translate(0,0,100) * rotateZ(i*1.1)
	
	ctr1.set_location(trsf)	
	ctr2.set_location(trsf2)
	ctr3.set_location(trsf3)	
	#widget.viewer.redraw()

show(scn, animate = animate, nointersect=True)
