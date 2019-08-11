#!/usr/bin/env python3

from zencad import *
import pyservoce

from body import bodyunit

class accumulator(zencad.assemble.unit):
	shp = box(20,20,10, center=True)

	def __init__(self):
		super().__init__()
		self.add_shape(self.shp)


class controller(zencad.assemble.unit):
	shp = (
		box(45,45,2, center=True)
		+ sqrtrans()(cylinder(r=3, h=2).translate(45/2,45/2,-1))
	)

	def __init__(self):
		super().__init__()
		self.add_shape(self.shp, color=pyservoce.green)


accum = accumulator()
contr = controller()
contr.relocate(up(10+1))

disp(bodyunit)
disp(accum)
disp(contr)

show()
