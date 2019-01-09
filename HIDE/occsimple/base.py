from OCC.gp import gp_Pnt, gp_OX, gp_Vec, gp_Dir, gp_Trsf, gp_DZ, gp_Ax1, gp_Ax2, gp_Ax3, gp_Pnt2d, gp_Dir2d, gp_Ax2d
	
import inspect
import occsimple.trans as trans
from OCC.TopExp import TopExp_Explorer
from OCC.TopAbs import TopAbs_EDGE, TopAbs_FACE
from OCC.TopTools import TopTools_ListOfShape
from OCC.TopoDS import topods, TopoDS_Edge, TopoDS_Compound
class vector3d:
	x = 0
	y = 0
	z = 0

	def __init__(self, arg):
		if (isinstance(arg, list)):
			self.x = arg[0]
			self.y = arg[1]
			if len(arg) > 2:
				self.z = arg[2]
		if (isinstance(arg, vector3d)):
			self.x = arg.x
			self.y = arg.y
			self.z = arg.z	
		if (isinstance(arg, int) or isinstance(arg, float)):
			self.x = arg
			self.y = arg
			self.z = arg
		if self.z == None:
			self.z = 0

	def __add__(self, other):
		return vector3d([self.x+other.x, self.y+other.y, self.z+other.z])  

	def __sub__(self, other):
		return vector3d([self.x-other.x, self.y-other.y, self.z-other.z])  	

	def __repr__(self):
		return "point({},{},{})".format(self.x, self.y, self.z)

	def __neg__(self):
		return vector3d([-self.x, -self.y, -self.z])  

	def to_occ_vec(self):
		return gp_Vec(self.x, self.y, self.z)

def vector2d(vec):
	return vector3d(vec)

class Axis:
	pnt = None
	vec = None

	def __init__(self, pnt, vec):
		self.pnt = pnt
		self.vec = vec

	def __neg__(self):
		return Axis(self.pnt, - self.vec)

	def construct(self):
		return gp_Ax1(self.pnt.doit(), gp_Dir(self.vec.x, self.vec.y, self.vec.z))



def xaxis():
	return Axis(point([0,0,0]), vector3d([1,0,0]))
def yaxis():
	return Axis(point([0,0,0]), vector3d([0,1,0]))
def zaxis():
	return Axis(point([0,0,0]), vector3d([0,0,1]))

class OCCSimpleObject:
	constructed = False
	model = None

	def translate(self,vec):
		return trans.translate(vec)(self)
	def multiply_translate(self,vecs):
		return trans.multiply_translate(vecs)(self)
	def mirror(self,arg):
		return trans.mirror(arg)(self)
	def up(self,arg):
		return trans.up(arg)(self)
	def down(self,arg):
		return trans.down(arg)(self)
	def left(self,arg):
		return trans.left(arg)(self)
	def right(self,arg):
		return trans.right(arg)(self)
	def forward(self,arg):
		return trans.forward(arg)(self)
	def back(self,arg):
		return trans.back(arg)(self)

	def rotateX(self,arg):
		return trans.rotateX(arg)(self)
	def rotateY(self,arg):
		return trans.rotateY(arg)(self)
	def rotateZ(self,arg):
		return trans.rotateZ(arg)(self)

	def matrix_rotation(self,rot):
		return trans.matrix_rotation(rot)(self)

	def faces(self):
		ret = []
		explorer = TopExp_Explorer(self.doit(), TopAbs_FACE)
		while explorer.More():
			aFace = topods.Face(explorer.Current())
			ret.append(aFace)
			explorer.Next()
		return ret

	def edges(self):
		ret = []
		explorer = TopExp_Explorer(self.doit(), TopAbs_FACE)
		while explorer.More():
			aFace = topods.Face(explorer.Current())
			ret.append(aFace)
			explorer.Next()
		return ret

	def doit(self):
		if self.constructed == False:
			self.model = self.construct()
		return self.model


class point(vector3d, OCCSimpleObject):
	def construct(self):
		#print('{2}, {1}, {0}'.format(self.x, self.y, self.z))
		return gp_Pnt(self.x, self.y, self.z)

def points(arr):
	return [point(x) for x in arr]