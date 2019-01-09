#!/usr/bin/env python2
#coding: utf-8
import sys
sys.path.append('../python-model-lib')

from solid import *
from solid.utils import *

from solidlib import *

lenf = 25
lend = 10
lens = 10
width = 2
length = 120

profile = polyline(array_from_deltas([
					[lens,0],
					[lend/sqrt(2),lend/sqrt(2)], 
					[0,lenf], 
					[-lend/sqrt(2),lend/sqrt(2)], 
					[-lens,0]					
				]),width/2)

def bothole(h):
	return translate([h,lend/sqrt(2) + lenf/2,0])(linear_extrude(width)(central_circles_array(4, 1.6, 8, 4)))

model = difference() (
	up(width/2 + lens + lend/sqrt(2))(rotate([0,90,0])(linear_extrude(length, convexity=4)(profile))),
	bothole(20),
	bothole(length - 20),
)

model_text = scad_render(model, file_header='$fn = 40;')
print(model_text)
file = open("forwback-gen.scad","w")
file.write(model_text)
file.close