from OCC.gp import gp_Pnt
from OCC.BRepBuilderAPI import BRepBuilderAPI_Transform, BRepBuilderAPI_MakeVertex
from OCC.BRepAlgoAPI import BRepAlgoAPI_Fuse, BRepAlgoAPI_Cut

from OCC.TopoDS import topods_Vertex
import occ.trans as trans

class transform_api:
	def translate(self, *args):
		return self.transformed(trans.translate(*args))

	def rotate(self, *args):
		return self.transformed(trans.rotate(*args))

	def rotateX(self, *args):
		return self.transformed(trans.rotateX(*args))

	def rotateY(self, *args):
		return self.transformed(trans.rotateY(*args))

	def rotateZ(self, *args):
		return self.transformed(trans.rotateZ(*args))

	def mirror(self, *args):
		return self.transformed(trans.mirror(*args))

	def scale(self, *args):
		return self.transformed(trans.scale(*args))

	def up(self, arg):
		return self.transformed(trans.translate(0,0,arg))		

	def down(self, arg):
		return self.transformed(trans.translate(0,0,-arg))

	def forward(self, arg):
		return self.transformed(trans.translate(0,arg,0))

	def backward(self, arg):
		return self.transformed(trans.translate(0,-arg,0))

	def right(self, arg):
		return self.transformed(trans.translate(arg,0,0))

	def left(self, arg):
		return self.transformed(trans.translate(-arg,0,0))

	#def toframe(self, frm):
	#	return self.transformed(trans.toframe(frm))

	def frame_transformation(self, frm0, frm1):
		return self.transformed(trans.frame_transformation(frm0,frm1))

	def locframe(self, p3, d3):
		return self.transformed(trans.locframe(p3,d3))

class shape(transform_api):
	def __init__(self, arg = None):
		if arg:
			self.shp = arg

	def native(self):
		return self.shp 

	def __add__(self, other):
		return shape_union(self, other)

	def __sub__(self, other):
		return shape_difference(self, other)

	def transformed(self, trsf):
		return transformed_shape(self, trsf)

class transformed_shape(shape):
	def __init__(self, a, t):
		self.constructed = False
		if isinstance(a, transformed_shape):
			self.base = a.base
			self.trsf = t * a.trsf
		else:
			self.base = a
			self.trsf = t

	def native(self):
		if not self.constructed:
			brep_trns = BRepBuilderAPI_Transform(self.base.native(), self.trsf.get(), False)
			brep_trns.Build()
			self.shp = brep_trns.Shape()
		return self.shp 

def shape_union(a, b):
	return shape(BRepAlgoAPI_Fuse(a.native(), b.native()).Shape())

def shape_difference(a, b):
	return shape(BRepAlgoAPI_Cut(a.native(), b.native()).Shape())

def shape_transformed(a, t):
	brep_trns = BRepBuilderAPI_Transform(a.native(), t.native(), False)
	brep_trns.Build()
	return shape(brep_trns.Shape())






class vertex(transform_api):
	def __init__(self, x, y=None, z=None):
		shape.__init__(self)
		if y==None and z==None:
			self.vtx = x
		else:
			self.vtx = BRepBuilderAPI_MakeVertex(gp_Pnt(x,y,z)).Vertex() 

	def native(self):
		return self.vtx 

	def transformed(self, trsf):
		return vertex(topods_Vertex(BRepBuilderAPI_Transform(self.vtx, trsf.get(), False).Shape()))