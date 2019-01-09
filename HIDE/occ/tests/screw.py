#!/usr/bin/env python3
#coding: utf-8

import sys
sys.path.append("../..")

import math
import occ.solid as solid
import occ.util as util
import occ.topo as topo
import occ.wire as wire
import occ.algo as algo
import occ.stl as stl
from occ.gui import *


import OCC.BRepTools as BRepTools
import OCC.BRep as BRep
import OCC.TopoDS as TopoDS

pts = util.points([
	(6,0,0),
	(6,10,0),
	(10,10,0),
	(15,5,0),
	(10,0,0),
])


#display(makeHelixWire(r=2, h=1, a=math.pi*4))
#display(solid.cylinder(r=2,h=1))




#c = wire.circle(3).face().rotateX(math.pi/2).right(10)
#pipe = algo.pipe(w, p);

#display(p)
#display(geom.origin())

#display_raw(aLine2d)
#display_raw(aSegment)

#display(w)
#display(pipe)

def simple_screw(l, idiam, odiam, step, left = False):
	helix = wire.helix(h = l, r = idiam / 2, a = 2*math.pi * l / step)
	profile = wire.circle((odiam + idiam) / 4).translate((odiam - idiam) / 4,0,0)
	return algo.pipe_shell(helix, profile)

s1 = simple_screw(l = 10,idiam = 6.6, odiam = 8, step = 1.25)
s2 = solid.cylinder(4, 10).left(4)

#BRepTools.breptools().Write((s1+s2).native(), "test.brep")

#m22 = TopoDS.TopoDS_Shape()
#builder = BRep.BRep_Builder()
#BRepTools.breptools().Read(m22,"test.brep",builder)

#m2 = topo.shape(m22)

display(s1 + s2)
#display(m2)

display_frame()
start_display()



#void makeHelix(void)
#{
#    Handle_Geom_CylindricalSurface aCylinder = new Geom_CylindricalSurface(gp::XOY(), 6.0);
#    gp_Lin2d aLine2d(gp_Pnt2d(0.0, 0.0), gp_Dir2d(1.0, 1.0));
#    Handle_Geom2d_TrimmedCurve aSegment = GCE2d_MakeSegment(aLine2d, 0.0, M_PI * 2.0);
#    TopoDS_Edge aHelixEdge = BRepBuilderAPI_MakeEdge(aSegment, aCylinder, 0.0, 6.0 * M_PI).Edge();
#    BRepTools::Dump(aHelixEdge, std::cout);
#    BRepTools::Write(aHelixEdge, "d:/helix.brep");
#}#