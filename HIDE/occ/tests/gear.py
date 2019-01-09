#!/usr/bin/env python3
#coding: utf-8

import sys
sys.path.append("../..")

import occ.geom as geom
from occ.geom import point, direction, axis
import occ.curve as curve
from occ.trans import *
from occ.gui import display, start_display
import math

def gear(number, module):
	pitch_diametr = number * module
	r_p = pitch_diametr / 2
	r_a = r_p + module
	r_d = r_p - module * 1.25
	r_b = r_p * math.cos(util.degree(20))
	pitch_circle = curve.circle(r_p)
	base_circle = curve.circle(r_b)
	addendum_circle = curve.circle(r_a)
	dedendum_circle = curve.circle(r_d)

	tanlin = geom.line(geom.point(0,r_p,0), geom.direction(1,0,0))
	radlin = geom.line(geom.point(0,r_p,0), geom.direction(0,1,0))
	
	display(pitch_circle)
	display(base_circle)
	display(addendum_circle)
	display(dedendum_circle)

	display(tanlin.rotated(axis(point(0,r_p,0), direction(0,0,1)), util.degree(20)))
	display(radlin)

	angle = 20./180.* math.pi;
	phi = math.tan(angle);
	phi_0 = math.pi / 2. + angle - phi;

	print(util.degree(phi_0))
	h_phi = math.pi / 100.;
	
	for i in range(0,20):
	   phi = i*h_phi;
	   cs = math.cos(phi + phi_0);
	   sn = math.sin(phi + phi_0);
	   x = r_b*(cs+phi*sn);
	   y = r_b*(sn-phi*cs);
	   pnt = point(x,y,0.);
	   display(pnt)
	
	return pitch_circle

model = gear(number = 30, module = 3)

start_display()