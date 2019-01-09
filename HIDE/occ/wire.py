#from OCC.GC import GC_MakeSegment
from OCC.BRepBuilderAPI import BRepBuilderAPI_MakeWire, BRepBuilderAPI_Transform
from OCC.TopoDS import topods_Wire
from occ.topo import transform_api
import occ.edge as edge
import occ.geom as geom
import occ.curve as curve
import occ.util as util
from occ.face import make_face

import math


from OCC.gp import gp_Lin2d, gp_Pnt2d, gp_Dir2d
from OCC.Geom import Geom_CylindricalSurface, Handle_Geom_Surface
from OCC.GCE2d import GCE2d_MakeSegment
from OCC.Geom2d import Handle_Geom2d_TrimmedCurve, Geom2d_TrimmedCurve
from OCC.BRepBuilderAPI import BRepBuilderAPI_MakeEdge, BRepBuilderAPI_MakeWire

from OCC.BRepOffsetAPI import BRepOffsetAPI_MakePipeShell
from OCC.BRepLib import breplib_BuildCurves3d


class wire(transform_api):
	def __init__(self, arg = None):
		if arg:
			self.wr = arg

	def native(self):
		return self.wr

	def transformed(self, trsf):
		return wire(topods_Wire(BRepBuilderAPI_Transform(self.wr, trsf.get(), False).Shape()))

	def face(self):
		return make_face(self)

	def __add__(self, other):
		builder = BRepBuilderAPI_MakeWire(self.wr)
		builder.Add(other.native())
		return wire(builder.Wire())

def make_wire(arr):
	if isinstance(arr, list):
		w = BRepBuilderAPI_MakeWire(arr[0].native())
		for i in range(1, len(arr)):
			w.Add(arr[i].native())
		return wire(w.Wire())
	else:
		return wire(BRepBuilderAPI_MakeWire(arr.native()).Wire())

def segment(p0, p1):
	return make_wire(edge.segment(p0,p1))

def polysegment(pts, closed = False):
	sgs = []
	for i in range(0, len(pts) - 1):
		sgs.append(edge.segment(pts[i], pts[i+1]))
	if closed:
		sgs.append(edge.segment(pts[-1], pts[0]))
	return make_wire(sgs)

def bezier(pts):
	return make_wire(edge.make_edge_from_curve(curve.bezier(pts)))

def interpolate(pts):
	return make_wire(edge.make_edge_from_curve(curve.interpolate(pts)))

def circle(*args):
	return make_wire(edge.circle(*args))

def elipse(*args):
	return make_wire(edge.elipse(*args))

def rectangle(x,y,center=False):
	if not center:
		pts = util.points([(0,0,0), (x,0,0), (x,y,0), (0,y,0)])
	else:
		cx = x/2
		cy = y/2
		pts = util.points([(-cx,-cy,0), (cx,-cy,0), (cx,cy,0), (-cx,cy,0)])
	return polysegment(pts, closed=True)

def square(a, center=False):
	return rectangle(a,a,center)


def helix(r, h, a):
	aLine2d = gp_Lin2d(gp_Pnt2d(0.0, 0.0), gp_Dir2d(a, h));
	aSegment = GCE2d_MakeSegment(aLine2d, 0, 1);

	surf = Geom_CylindricalSurface(geom.frameOXYZ().native(), r);
	aHelixEdge = BRepBuilderAPI_MakeEdge(
	Handle_Geom2d_TrimmedCurve.DownCast(
		aSegment.Value()),
		Handle_Geom_Surface(surf), 
		0.0, a / math.cos(math.atan2(h,a)) 
	).Edge();

	w = wire(BRepBuilderAPI_MakeWire(aHelixEdge).Wire())
	breplib_BuildCurves3d(w.native())
	return w