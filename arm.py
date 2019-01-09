#!/usr/bin/env python3
#coding: utf-8

from zencad import *
<<<<<<< HEAD
import zencad.unbound
=======
>>>>>>> d5dfe3cc3ca9b8d674eee5562e0fbad7bf523410

c = cylinder(h=100, r=5)
s = sphere(r=10)

z = c + s + s.up(100)

scn = Scene()

ctr1 = scn.add(z.unlazy())
ctr2 = scn.add(z.rotateX(deg(45)).unlazy())
ctr3 = scn.add(z.rotateY(deg(90)).unlazy())

i = 0
def animate(widget):
	global i
	i += 0.02
	trsf = rotateY(i)
	trsf2 = trsf * translate(0,0,100) * rotateZ(i)
	trsf3 = trsf2 * rotateX(deg(45)) * translate(0,0,100) * rotateZ(i*1.1)
	
	ctr1.set_location(trsf)	
	ctr2.set_location(trsf2)
	ctr3.set_location(trsf3)		
<<<<<<< HEAD
	widget.view.redraw()

zencad.unbound.start_unbound(scn, animate = animate)
=======
	widget.redraw()

show(scn, animate = animate, nointersect=True)
>>>>>>> d5dfe3cc3ca9b8d674eee5562e0fbad7bf523410
