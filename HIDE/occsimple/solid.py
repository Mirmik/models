from OCC.BRepPrimAPI import BRepPrimAPI_MakeSweep, BRepPrimAPI_MakePrism, BRepPrimAPI_MakeCylinder, BRepPrimAPI_MakeSphere, BRepPrimAPI_MakeBox
from OCC.BRepBuilderAPI import BRepBuilderAPI_MakeEdge, BRepBuilderAPI_MakeWire, BRepBuilderAPI_MakeFace, \
	BRepBuilderAPI_Transform
from OCC.BRepAlgoAPI import BRepAlgoAPI_Fuse, BRepAlgoAPI_Common, BRepAlgoAPI_Section, BRepAlgoAPI_Cut
from OCC.gp import gp_Pnt, gp_OX, gp_Vec, gp_Dir, gp_Trsf, gp_DZ, gp_Ax2, gp_Ax3, gp_Pnt2d, gp_Dir2d, gp_Ax2d

from OCC.BRepPrimAPI import BRepPrimAPI_MakeRevol

#from occsimple.solid_operations import *
from occsimple.base import *
from occsimple.trans import *

class Object3d(OCCSimpleObject):
	def __sub__(a,b):
		return Object3d_Sub(a,b)

	def __add__(a,b):
		return Object3d_Add(a,b)

	def transformation(self, token):
		return Object3d_Transformation(self, [token])

class Object3d_Box(Object3d):
	size = None

	def __init__(self, size, kwargs):
		self.size = vector3d(size)

	def construct(self):
		return BRepPrimAPI_MakeBox(self.size.x, self.size.y, self.size.z).Shape()

class Object3d_Sphere(Object3d):
	def __init__(self,r):
		self.r = r
	
	def construct(self):
		return BRepPrimAPI_MakeSphere(self.r).Shape()

class Object3d_Cylinder(Object3d):
	def __init__(self,r,h):
		self.r = r
		self.h = h
	
	def construct(self):
		return BRepPrimAPI_MakeCylinder(self.r, self.h).Shape()

class Object3d_OpenCascadeShape(Object3d):
	def __init__(self,shp):
		self.shp = shp
	
	def construct(self):
		return self.shp

class Object3d_Sub(Object3d):
	def __init__(self,a,b):
		self.a = a
		self.b = b

	def construct(self):
		return BRepAlgoAPI_Cut(self.a.construct(), self.b.construct()).Shape()
		
class Object3d_Add(Object3d):
	def __init__(self,a,b):
		self.a = a
		self.b = b

	def construct(self):
		return BRepAlgoAPI_Fuse(self.a.construct(), self.b.construct()).Shape()

class Object3d_Sweep(Object3d):
	def __init__(self,a,b):
		self.a = a
		self.b = b

	def construct(self):
		return BRepPrimAPI_MakeSweep(self.a.doit(), self.b.doit()).Shape()
		
class Object3d_Transformation(Object3d):
	def __init__(self,obj,tokens):
		self.obj = obj
		self.trans = Transformation(tokens)

	def transformation(self, token):
		tokens = list(self.trans.tokens)
		tokens.append(token)
		return Object3d_Transformation(self.obj, tokens)

	def construct(self):
		return self.trans.do_object3d(self.obj.construct())


#	def construct(self):
#		trns = gp_Trsf()
#		trns.SetTranslation(gp_Vec(self.vec.x, self.vec.y, self.vec.z))
#		brep_trns = BRepBuilderAPI_Transform(self.obj.construct(), trns, False)
#		brep_trns.Build()
#		return brep_trns.Shape()

class Object3d_Mirror(Object3d):
	def __init__(self,xyz,obj):
		self.xyz = xyz
		self.obj = obj

	def construct(self):
		trns = gp_Trsf()
		trns.SetMirror(gp_Ax2(gp_Pnt(0,0,0), gp_Dir(self.xyz[0], self.xyz[1], self.xyz[2])))
		brep_trns = BRepBuilderAPI_Transform(self.obj.construct(), trns, False)
		brep_trns.Build()
		return brep_trns.Shape()

#class MirrorShape(Object3d):


#	def construct():
#		aTrsf = gp_Trsf()
#		aTrsf.SetMirror(xAxis)



class Object3d_Revol(Object3d):
	def __init__ (self,face,axis,angle):
		self.face = face
		self.axis = axis
		self.angle = angle
		
	def construct(self):
		return BRepPrimAPI_MakeRevol(self.face.construct(), self.axis.construct(), self.angle).Shape()

class Object3d_Prism(Object3d):
	def __init__ (self,profile,vec):
		self.profile = profile
		self.vec = vector3d(vec)
		
	def construct(self):
		return BRepPrimAPI_MakePrism(self.profile.doit(), self.vec.to_occ_vec()).Shape()

	def native_object(self):
		return BRepPrimAPI_MakePrism(self.profile.doit(), self.vec.to_occ_vec())


def box(size, **kwargs):
	return Object3d_Box(size, kwargs)

def sphere(r):
	return Object3d_Sphere(r)

def cylinder(r,h):
	return Object3d_Cylinder(r,h)

def shape(shp):
	return Object3d_OpenCascadeShape(shp)

def revol(_face, _axis, angle):
	return Object3d_Revol(_face, _axis, angle)

def prism(profile, vec):
	return Object3d_Prism(profile, vec)

def sweep(start, stop):
	return Object3d_Sweep(start, stop)