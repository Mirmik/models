from OCC.gp import gp_Pnt, gp_OX, gp_Vec, gp_Dir, gp_Trsf, gp_DZ, gp_Ax1, gp_Ax2, gp_Ax3, gp_Pnt2d, gp_Dir2d, gp_Ax2d
from OCC.BRepBuilderAPI import BRepBuilderAPI_MakeEdge, BRepBuilderAPI_MakeWire, BRepBuilderAPI_MakeFace, \
    BRepBuilderAPI_Transform
from OCC.BRepOffsetAPI import BRepOffsetAPI_MakePipe
from OCC.BRepPrimAPI import BRepPrimAPI_MakeRevol
from OCC.GC import GC_MakeArcOfCircle, GC_MakeSegment, GC_MakeCircle
from OCC.BRepAlgoAPI import BRepAlgoAPI_Fuse, BRepAlgoAPI_Common, BRepAlgoAPI_Section, BRepAlgoAPI_Cut


from occsimple.base import *
import occsimple.wires as wires
from occsimple.trans import *

#def make_wire(edges):
#	w = BRepBuilderAPI_MakeWire(edges[0])
#	for i in range(1, len(edges)):
#		w.Add(edgs[i])
#	return w.Wire()

def make_face(wire):
	return BRepBuilderAPI_MakeFace(wire).Face()

class Object2d(OCCSimpleObject):
	def __add__(self, b):
		return Object2d_Add(self,b)

	def __sub__(self, b):
		return Object2d_Sub(self,b)

	def construct(self):
		return make_face(make_wire(self.edges()))

	def transformation(self, token):
		return Object2d_Transformation(self, [token])

	def linear_extrude(self, *args):
		return linear_extrude(*args)(self)

	def revol(self, axis, angle):
		return occsimple.solid.revol(self, axis, angle)

class Object2d_Sub(Object2d):
	def __init__(self,a,b):
		self.a = a
		self.b = b

	def construct(self):
		return BRepAlgoAPI_Cut(self.a.construct(), self.b.construct()).Shape()
		
class Object2d_Add(Object2d):
	def __init__(self,a,b):
		self.a = a
		self.b = b

	def construct(self):
		return BRepAlgoAPI_Fuse(self.a.construct(), self.b.construct()).Shape()

class Object2d_FromWire(Object2d):
	def __init__(self, wire):
		self.wire = wire

	def construct(self):
		return make_face(self.wire.construct())

class Object2d_Circle(Object2d):
	def __init__(self, r):
		self.r = r

	def construct(self):
		return make_face(wires.circle(self.r).construct())

	
class Object2d_Transformation(Object2d):
	def __init__(self,obj,tokens):
		self.obj = obj
		self.trans = Transformation(tokens)

	def transformation(self, token):
		tokens = list(self.trans.tokens)
		tokens.append(token)
		return Object2d_Transformation(self.obj, tokens)

	def construct(self):
		return self.trans.do_object3d(self.obj.construct())


class Object2d_Rectangle(Object2d):
	def __init__(self, vec, **kwargs):
		self.vec = vec
		self.options = kwargs

	def construct(self):	
		return make_face(wires.WireObject_Rectangle(self.vec, **self.options).construct())

class Object2d_Ngon(Object2d):
	def __init__(self, r, n):
		self.r = r
		self.n = n

	def construct(self):	
		return make_face(wires.WireObject_Ngon(self.r, self.n).construct())


def circle_arc(a,b,c):
	return CircleArc(a,b,c)

def circle(r):
	return Object2d_Circle(r)

def rectangle(vec, **kwargs):
	return Object2d_Rectangle(vec, **kwargs)

def ngon(r, n):
	return Object2d_Ngon(r, n)

def face(arg):
	return Face(arg)

def axis(d,p = None):
	return Axis(d,p)

def dir(x,y,z):
	return Direction(x,y,z)

def clossed_wire_by_points(pnts): 
	assert len(pnts) >= 2
	w = wire()
	for i in range(1, len(pnts)):
		w.append(segment(pnts[i-1], pnts[i]))
	w.append(segment(pnts[-1], pnts[0]))
	return w
