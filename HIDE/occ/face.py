#from OCC.GC import GC_MakeSegment
from OCC.BRepBuilderAPI import BRepBuilderAPI_MakeFace, BRepBuilderAPI_Transform
from OCC.TopoDS import topods_Face
from occ.topo import transform_api
from occ.solid import prism

import occ.native_algo as nalgo

class face(transform_api):
	def __init__(self, arg = None):
		if arg:
			self.fc = arg

	def native(self):
		return self.fc

	def transformed(self, trsf):
		return face(topods_Face(BRepBuilderAPI_Transform(self.fc, trsf.get(), False).Shape()))

	def __sub__(self, other):
		return face(nalgo.native_shape_cut(self, other))

	def __add__(self, other):
		return face(nalgo.native_shape_fuse(self, other))

	def linear_extrude(self, *args):
		return prism(self, *args)

def make_face(wire):
	return face(BRepBuilderAPI_MakeFace(wire.native()).Face())
