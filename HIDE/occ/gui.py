#!/usr/bin/env python3
#coding: utf-8

from OCC.Display.SimpleGui import *
from OCC.AIS import AIS_Line
from OCC.Geom import Handle_Geom_Line, Geom_Line
from OCC.gp import gp_Pnt, gp_Lin

import occ.geom as geom
import occ.curve as curve

OCCdisplay, start_display, add_menu, add_function_to_menu = init_display()
def display(arg):
	print(arg)
	if isinstance(arg, list):
		for l in arg:
			display(l)
	elif isinstance(arg, geom.line):
		OCCdisplay.DisplayShape(curve.curve(arg).native())
		return
	else:
		OCCdisplay.DisplayShape(arg.native())

def display_raw(arg):
	OCCdisplay.DisplayShape(arg)

def display_frame(frm = geom.frameOXYZ()):
	nat = frm.native()
	x = nat.Direction()
	ax2 = nat.Ax2()
	y = ax2.XDirection()
	z = ax2.YDirection()

	org = gp_Pnt(0,0,0)
	OCCdisplay.DisplayShape(Geom_Line(org, x))
	OCCdisplay.DisplayShape(Geom_Line(org, y))
	OCCdisplay.DisplayShape(Geom_Line(org, z))