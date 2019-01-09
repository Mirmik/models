from occ.geom import axisOX, axisOY, axisOZ  
from occ.base import occ_object
from occ.trans import translate, rotate, scale, mirror

from OCC.BRepBuilderAPI import BRepBuilderAPI_Transform
from OCC.BRepAlgoAPI import BRepAlgoAPI_Fuse, BRepAlgoAPI_Cut
from OCC.TopoDS import TopoDS_Shape

class shape(occ_object):
	def __init__(self):
		occ_object.__init__(self)

	def __add__(self, other):
		return shape_union(self, other)

	def __sub__(self, other):
		return shape_difference(self, other)

	def translate(self, *args):
		return shape_transformated(self, translate(*args))

	def rotate(self, *args):
		return shape_transformated(self, rotate(*args))

	def mirror(self, *args):
		return shape_transformated(self, mirror(*args))

	def scale(self, *args):
		return shape_transformated(self, scale(*args))

	def up(self, dist):
		return self.translate(0,0,dist)

	def down(self, dist):
		return self.translate(0,0,-dist)

	def left(self, dist):
		return self.translate(dist,0,0)

	def right(self, dist):
		return self.translate(-dist,0,0)

	def forward(self, dist):
		return self.translate(0,dist,0)

	def backward(self, dist):
		return self.translate(0,-dist,0)

class shape_transformated(shape):
	def __init__(self, base, inittrans):
		shape.__init__(self)
		self.base = base
		self.trans = [inittrans]

	def translate(self, *args):
		return trans.append(occ.trans.translate(*args))

	def rotate(self, *args):
		return trans.append(occ.trans.rotate(*args))

	def mirror(self, *args):
		return trans.append(occ.trans.mirror(*args))

	def scale(self, *args):
		return trans.append(occ.trans.scale(*args))

	def construct(self):
		tr = self.trans[0].doit()
		for i in range(1,len(self.trans)):
			tr = tr * self.trans[0].doit()
		brep_trns = BRepBuilderAPI_Transform(self.base.doit(), tr, False)
		brep_trns.Build()
		return brep_trns.Shape()

class shape_difference(shape):
	def __init__(self,a,b):
		shape.__init__(self)
		self.a = a
		self.b = b

	def construct(self):
		return BRepAlgoAPI_Cut(self.a.construct(), self.b.construct()).Shape()
		
class shape_union(shape):
	def __init__(self,a,b):
		shape.__init__(self)
		self.a = a
		self.b = b

	def construct(self):
		return BRepAlgoAPI_Fuse(self.a.construct(), self.b.construct()).Shape()

class vertex(shape):
	def __init__(self):
		shape.__init__(self)

class edge(shape):
	def __init__(self):
		shape.__init__(self)

class wire(shape):
	def __init__(self):
		shape.__init__(self)

class face(shape):
	def __init__(self):
		shape.__init__(self)

class solid(shape):
	def __init__(self):
		shape.__init__(self)