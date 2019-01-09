#!/usr/bin/env python3
#coding: utf-8

import zencad
from zencad import pnt, gr
import zencad.face as face
import zencad.solid as solid
import zencad.wire as wire
import zencad.stl as stl
from zencad.widget import display, show

import math

rad = 10
len = 20
rad2 = 5
len2 = 13

mmm = 5

prof = 3

def base_triangle():
	arc = wire.circle(r = rad, arc = (gr(0), gr(120)))
	seg = wire.segment(pnt(rad,0,0), pnt(rad,-len,0))
	tr = wire.make_wire([arc, seg])
	fc = face.square(prof, center = True).fillet(1).rotateX(gr(90)).translate(rad, -len, 0)
	mtr = solid.pipe(tr, fc).forw(len/2).right(len/math.sqrt(3)/2)
	mtr = mtr + mtr.rotateZ(gr(120)) + mtr.rotateZ(gr(240))
	return mtr

def ear():
	arc1 = wire.circle(r = rad2, arc = (gr(0), gr(90))).forw(len2/2)
	arc2 = wire.circle(r = rad2, arc = (gr(-90), gr(0))).back(len2/2)
	seg = wire.segment(pnt(rad2,len2/2,0), pnt(rad2,-len2/2,0))
	seg1 = wire.segment(pnt(0,len2/2+rad2,0), pnt(-mmm,len2/2+rad2,0))
	seg2 = wire.segment(pnt(0,-len2/2-rad2,0), pnt(-mmm,-len2/2-rad2,0))
	sseg = wire.segment(pnt(0,+len2/2+rad2,0), pnt(0,-len2/2-rad2,0))
	tr = wire.make_wire([seg1,arc1,seg,arc2,seg2])
	fc = face.square(prof, center = True).fillet(1).rotateY(gr(90)).translate(0, rad2 + len2/2, 0)
	fc2 = face.square(prof, center = True).fillet(1).rotateX(gr(90)).translate(0, rad2 + len2/2, 0)
	mtr = solid.pipe(tr, fc) + solid.pipe(sseg, fc2)
	m = mtr.right(mmm)
	return m

#arcs = triangle(10, 10)

#for a in arcs:
#	display(a)

#display(arc)
#display(seg)
#display(fc)
base = base_triangle()
ear1 = ear().right(16)
ear2 = ear1.rotateZ(gr(120))
ear3 = ear1.rotateZ(gr(240))

m = base + ear1 + ear2 + ear3
#display(ear())

display(m)
show()