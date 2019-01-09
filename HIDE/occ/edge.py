from OCC.GC import GC_MakeSegment
from OCC.BRepBuilderAPI import BRepBuilderAPI_MakeEdge, BRepBuilderAPI_Transform, BRepBuilderAPI_MakeWire
from OCC.TopoDS import topods_Edge

from occ.topo import transform_api
import occ.geom as geom
import occ.curve as curve

from OCC.gp import gp_Elips

from OCC.Geom import Handle_Geom_Curve

class edge(transform_api):
	def __init__(self, arg = None):
		if arg:
			self.edg = arg

	def native(self):
		return self.edg 

	def transformed(self, trsf):
		return edge(topods_Edge(BRepBuilderAPI_Transform(self.edg, trsf.get(), False).Shape()))

class closed_edge(edge):
	def __init__(self):
		edge.__init__(self)

	def linear_extrude(self, arg):
		return self.wire().face().linear_extrude(arg)

class segment(edge):
	def __init__(self, point_a, point_b):
		edge.__init__(self)
		self.edg = BRepBuilderAPI_MakeEdge(point_a.native(), point_b.native()).Edge()

class circle(closed_edge):
	def __init__(self, r, ax2 = geom.planeOXY()):
		closed_edge.__init__(self)
		self.edg = BRepBuilderAPI_MakeEdge(geom.circle(r, ax2).native()).Edge()

class elipse(closed_edge):
	def __init__(self, r1, r2, ax2 = geom.planeOXY()):
		closed_edge.__init__(self)
		self.edg = BRepBuilderAPI_MakeEdge(gp_Elips(ax2.native(),r1,r2)).Edge()


def make_edge_from_curve(arg):
	return edge(BRepBuilderAPI_MakeEdge(Handle_Geom_Curve(arg.native())).Edge())

#def bezier(pts):
