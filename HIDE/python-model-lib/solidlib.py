#!/usr/bin/env python2
#coding: utf-8

from solid import *
from solid.utils import *

#2d line
def line(p1,p2,radius):
	return hull()(
		translate(p1)(circle(r=radius)),
		translate(p2)(circle(r=radius)))

#2d polyline. usage: polyline(points, width)
def polyline(parr,radius,index=0):  
	model = line(parr[index], parr[index + 1], radius)
	if (len(parr) == index + 2):
		return model
	else:
		return model + polyline(parr, radius, index + 1)

def rotate_array(m, n):
	ret = m
	for f in frange(1, n):
		ret = ret + rotate([0,0,360./n * f])(m)
	return ret

def array_union(arr):
	model = arr[0]
	for i in range(1,len(arr)):
		model += arr[i]
	return model

def rounded_square(size, radius, angles, **kwargs) :
	quadr_dict = {
		0: [1,1],
		1: [0,1],
		2: [0,0],
		3: [1,0], 	
	}
	ret = translate([radius, radius, 0])(
		offset(radius)(
			square([size[0] - 2*radius, size[1] - 2*radius])))
	for i in list(set(range(0,4)) - set(angles)):
		q = quadr_dict[i]
		ret += translate([size[0]/2.*q[0], size[1]/2.*q[1], 0])(square([size[0]/2., size[1]/2.]))
	center = kwargs.pop('center', False)
	if center :
		ret = translate([-x/2 for x in size ])(ret)
	return ret

def array_from_deltas(arr):
	ret = [[0,0]]
	for i in range(0, len(arr)):
		ret.append([ret[i][0] + arr[i][0], ret[i][1] + arr[i][1]])
	return ret

def central_circles_array(central, side, radius, num):
	return circle(r=central) + rotate_array(translate([radius,0,0])(circle(r=side)), num)

def rounded_angle(y, z, x, w, angles):
	a = linear_extrude(w)(rounded_square([x,y], 2, [i for i in angles if i < 2])) 
	b = linear_extrude(w)(rounded_square([x,z], 2, [i-2 for i in angles if i >= 2])) 
	return a + forward(w)(rotate([90,0,0])(b))

def multiply_translate(points):
	def f(model):
		return array_union([translate(p)(model) for p in points])
	return f

def chain(*argv):
	def f(model):
		res = model
		for op in argv:
			res = op(res)
		return res
	return f

if __name__ == "__main__" :
	#debuged element
	#model = rounded_square([10,20], 2, [0,1])
	model_text = scad_render(model, file_header='$fn = 40;')
	print(model_text)
	file = open("debug.scad","w")
	file.write(model_text)
	file.close
	pass