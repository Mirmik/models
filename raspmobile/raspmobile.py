#!/usr/bin/env python3

from zencad import *
import zenboards.charger_tp4056

w = 20
l = 30
h = 10

t = 1

def basebox():

	m = box(w,l,h) - box(w-2*t, l-2*t, h-t).translate(t,t,t)

	return m

class assemble(zencad.assemble.unit):
	def __init__(self):
		super().__init__()
		self.m = basebox()
		self.add_shape(self.m)

assemble = assemble()

charger = zenboards.charger_tp4056.charger_tp4056_unit(socket=True)
charger.iobj.set_color(0.5,1,0.5)

charger.relocate(translate(charger.cheight + t*1.5, t, charger.width/2+t) * rotateY(deg(90)) * rotateX(deg(90)))

assemble.link(charger)

disp(assemble, deep = True)
show()