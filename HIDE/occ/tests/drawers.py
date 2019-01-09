#!/usr/bin/env python3
#coding: utf-8

import sys
sys.path.append("../..")

import math
import occ.solid as solid
import occ.util as util
import occ.wire as wire
import occ.algo as algo
import occ.trans as trans
import occ.stl as stl
from occ.gui import *

def section(w, h, l, t, d, d2):
	base = solid.box(2*t+w, t+l, 2*t+h)
	hole = solid.box(w, l, h).up(t).right(t)
	hole2 = solid.box(w-2*d,l,h+2*t).right(t + d)
	hole3 = solid.box(w,l+t,h-d2).right(t).up(d2+t)
	return base - hole - hole2 - hole3

#n, m - параметры матрицы.
#w,h,l - параметры нишы.
#t - толщина стенок.
#d - выступ поддержки.
#d2 - высота заднего бампера.
def storage(n, m, w, h, l, t, d, d2):
	sect = section(w,h,l,t,d, d2)
	transes = []
	for i in range(0,n):
		for j in range(0,m):
			transes.append(trans.translate(j*(w+t), 0, i*(h+t)))
	plate = solid.box(w*m + t*(n+1),l+t,t)
	return util.multiple_transform(sect, transes) + plate + plate.up(h*n+t*n)

def case(w,h,l,t,r,z,s):
	w = w*s
	h = h*0.95
	base = solid.box(w,l,h)
	hole = solid.box(w-2*t, l-2*t,h-t).translate(t,t,t)
	hole2 = solid.cylinder(r,t).rotateX(math.pi/2).translate(w/2,t,h)
	cbase = solid.box(w-2*t, z*2, h-r).backward(z*2).right(t)
	chole = solid.box(w-2*t-2*z, z, h-r-z).backward(z).right(t+z).up(z)
	chole2 = solid.box(w-2*t-4*z, z, h-r-2*z).backward(2*z).right(t+2*z).up(2*z)
	return base-hole-hole2 + cbase-chole-chole2

#m = storage(2,2,27,20,100,2,5,5).rotateX(-math.pi/2)
#m = storage(2,2,27,20,64,2,5,5).rotateX(-math.pi/2)

m1 = storage(6,6,27,20,64,1.5,5,5).rotateX(-math.pi/2)
m2 = case(w=27,h=20,l=64,t=1.5,r=27/2-4,z=1,s=0.97)

stl.make_stl(m1, "storage.stl")
stl.make_stl(m2, "case.stl")

display(m2)
start_display()