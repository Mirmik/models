#!/usr/bin/env python3
#coding: utf-8

import math
import zencad
from zencad import *


wbase = 30
thicknes = 2

def shpingalet_base(height, quadr_holes):
	w = 8
	h = 5
	
	thole_x = 22
	thole_y = 39
	rhole = 1.8
	#height = 70
	
	base = rectangle(wbase, thicknes, center = True)
	pl1 = rectangle(thicknes, h, center=True).right(w/2+thicknes/2).forw(thicknes/2 + h/2)
	pl2 = rectangle(thicknes, h, center=True).left(w/2+thicknes/2).forw(thicknes/2 + h/2)
	
	sph = (circle(w/2+thicknes, angle=deg(180)) - circle(w/2, angle=deg(180))).forw(thicknes/2 + h)
	sss = base + pl1 + pl2 + sph
	
	model = sss.extrude(height).rotateX(deg(90)).forw(height/2)
	
	if quadr_holes:
		mlt = multitrans([
			translate(+thole_x/2, +thole_y/2),
			translate(+thole_x/2, -thole_y/2),
			translate(-thole_x/2, +thole_y/2),
			translate(-thole_x/2, -thole_y/2),
		])
	else:
		mlt = multitrans([
			translate(+thole_x/2, 0),
			translate(-thole_x/2, 0),
		])

	holes = mlt(cylinder(r = rhole, h = thicknes, center=True))
	model = model - holes

	return model

if __name__ == "__main__":
	disp(shpingalet_base(10, quadr_holes=False))
	show()