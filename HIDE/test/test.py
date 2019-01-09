#!/usr/bin/env python3
#coding:utf-8
import math

import sys
sys.path.append("../")

from OCC.Display.SimpleGui import *
import occsimple.solid as solid
import occsimple.geom2d as geom2d
import occsimple.wires as wires

from OCC.TopExp import TopExp_Explorer
from OCC.TopAbs import TopAbs_EDGE, TopAbs_FACE
from OCC.TopTools import TopTools_ListOfShape
from OCC.TopoDS import topods, TopoDS_Edge, TopoDS_Compound


from occsimple.stl import *
import occsimple.base
import occsimple.mlib

#model = solid.sweep(geom2d.ngon(20,6), geom2d.ngon(20,6).translate([0,0,20])) 

shp = solid.prism(geom2d.ngon(20,6), [0,1,1]).native_object()
#shp.LastShape(geom2d.ngon(20,6).translate([0,0,20]).doit())


display, start_display, add_menu, add_function_to_menu = init_display()
display.DisplayShape(shp.Shape())
start_display()