#!/usr/bin/env python3
#coding: utf-8

import sys
sys.path.append("../..")

import math
import occ.solid as solid
import occ.topo as topo
import occ.util as util
import occ.wire as wire
import occ.algo as algo
import occ.stl as stl
from occ.gui import *

import OCC.BRepTools as BRepTools
import OCC.BRep as BRep
import OCC.TopoDS as TopoDS

#thikness = 3.5
#height = 90
#radius = 40
#handle_radius = 4
#
#pts = util.points([
#	(0,-5,-5),
#	(0,0,0),
#	(0,5,5),
#	(0,10,10),
#	(0,15,15),
#	(0,20,20),
#	(0,27,40),
#	(0,25,50),
#	(0,10,60),
#	(0,5,60),
#	(0,-5,60),
#])
#
#spine = wire.interpolate(pts)
#profile = wire.circle(handle_radius).face().rotateX(util.degree(-45))
#
#base = solid.cylinder(radius, height)
#hole = solid.cylinder(radius - thikness, height - thikness)
#handle = algo.pipe(spine, profile)
#
#m = base + handle.forward(40).up(17) - hole.up(thikness)
#
#BRepTools.breptools().Write(m.native(), "test.brep")
#
m22 = TopoDS.TopoDS_Shape()
builder = BRep.BRep_Builder()
BRepTools.breptools().Read(m22,"test.brep",builder)

m2 = topo.shape(m22)

#stl.make_stl(m, "cup2.stl", 0.01)

display(m2)
start_display()