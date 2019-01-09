from OCC.gp import gp_Pnt, gp_OX, gp_Vec, gp_Dir, gp_Trsf, gp_DZ, gp_Ax1, gp_Ax2, gp_Ax3, gp_Pnt2d, gp_Dir2d, gp_Ax2d
from OCC.BRepBuilderAPI import BRepBuilderAPI_MakeEdge, BRepBuilderAPI_MakeWire, BRepBuilderAPI_MakeFace, \
    BRepBuilderAPI_Transform
from OCC.BRepOffsetAPI import BRepOffsetAPI_MakePipe
from OCC.BRepPrimAPI import BRepPrimAPI_MakeRevol
from OCC.GC import GC_MakeArcOfCircle, GC_MakeSegment, GC_MakeCircle

from occsimple.base import *
from occsimple.trans import *
import math

class WireObject(OCCSimpleObject):	
	def construct(self):
		edgs = self.edges()
		w = BRepBuilderAPI_MakeWire(edgs[0])
		for i in range(1, len(edgs)):
			w.Add(edgs[i])
		return w.Wire()

	def __add__(self, b):
		return WireObject_Add(self, b)

	def face(self):
		return occsimple.geom2d.Object2d_FromWire(self)

	def transformation(self, trans):
		return WireObject_Transformation(self, trans)

class WireObject_Add(WireObject):
	def __init__(self,a,b):
		self.a = a
		self.b = b

	def edges(self):
		return self.a.edges() + self.b.edges() 

class WireObject_Transformation(WireObject):
	def __init__(self,obj,token):
		self.obj = obj
		self.trans = Transformation(token)

	def transformation(self, token):
		self.trans.add_token(token)
		return self

	def construct(self):
		return self.trans.do_wire(self.obj.construct())

class WireObject_Circle(WireObject):
	def __init__ (self,r):
		self.r = r

	def edges(self):
		return [BRepBuilderAPI_MakeEdge(GC_MakeCircle(gp_Ax1(gp_Pnt(0,0,0), gp_Dir(0,0,1)), self.r).Value()).Edge()]

class WireObject_Segment(WireObject):
	def __init__ (self,x,y):
		self.x = x
		self.y = y

	def edges(self):
		#print("x:{0} y:{1}".format(self.x, self.y))
		return [BRepBuilderAPI_MakeEdge(GC_MakeSegment(self.x.construct(), self.y.construct()).Value()).Edge()]

class WireObject_Arc(WireObject):
	def __init__ (self,a,b,c):
		self.a = a
		self.b = b
		self.c = c

	def edges(self):
		return [BRepBuilderAPI_MakeEdge(GC_MakeArcOfCircle(self.a.construct(), self.b.construct(), self.c.construct()).Value()).Edge()]

class WireObject_Ngon(WireObject):
	def __init__ (self,r,n):
		self.r = r
		self.n = n

	def edges(self):
		pnts = [point([self.r * math.cos(2*math.pi / self.n * a), self.r * math.sin(2*math.pi / self.n * a)]) for a in range(0,self.n)]
		
		edgs = []
		for i in range(1, len(pnts)):
			edgs.extend(segment(pnts[i-1], pnts[i]).edges())
		edgs.extend(segment(pnts[-1], pnts[0]).edges())

		return edgs

class WireObject_Rectangle(WireObject):
	def __init__(self, vec, **kwargs):
		for key in kwargs:
			if key != "rounded" and key != "center":
				raise Exception("AllBad", key) 

		options = {
			"center": False,
			"rounded": None,
		}
		options.update(kwargs)
		self.vec = vector2d(vec)
		self.options = options

	def edges(self):
		edgs = []

		if self.options["center"] == True:
			minx = - self.vec.x / 2
			maxx = + self.vec.x / 2
			miny = - self.vec.y / 2
			maxy = + self.vec.y / 2
		else:
			minx = 0
			maxx = self.vec.x
			miny = 0
			maxy = self.vec.y
		
		#if self.options["center"]:
		#	offset = vector2d([-self.vec.x/2, -self.vec.y/2])
		#else:
		#	offset = vector2d([0, 0])

		if self.options["rounded"]:
			(radius, angles) = self.options["rounded"]
			s = set(angles)
			_p = []
			r = radius
			sr = r * (1 - 1/math.sqrt(2))
			if 0 in s:
				pnt1 = point([maxx, 		maxy - r])
				pnt2 = point([maxx - sr, 	maxy - sr])
				pnt3 = point([maxx - r, 	maxy])
				first_point0 = pnt1
				last_point0 = pnt3
				edgs.append(arc(pnt1,pnt2,pnt3).doit())
			else:
				first_point0 = point([maxx, maxy])
				last_point0 = point([maxx, maxy])

			if 1 in s:
				pnt1 = point([minx + r, 	maxy])
				pnt2 = point([minx + sr, 	maxy - sr])
				pnt3 = point([minx, 	maxy - r])
				first_point1 = pnt1
				last_point1 = pnt3
				edgs.append(segment(last_point0, first_point1).doit())
				edgs.append(arc(pnt1,pnt2,pnt3).doit())
			else:
				first_point1 = point([minx, maxy])
				last_point1 = point([minx, maxy])
				edgs.append(segment(last_point0, first_point1).doit())

			if 2 in s:
				pnt1 = point([minx,	miny + r])
				pnt2 = point([minx + sr, 	miny + sr])
				pnt3 = point([minx + r, 	miny])
				first_point2 = pnt1
				last_point2 = pnt3
				edgs.append(segment(last_point1, first_point2).doit())
				edgs.append(arc(pnt1,pnt2,pnt3).doit())
			else:
				first_point2 = point([minx, miny])
				last_point2 = point([minx, miny])
				edgs.append(segment(last_point1, first_point2).doit())

			if 3 in s:
				pnt1 = point([maxx - r, 	miny])
				pnt2 = point([maxx - sr, 	miny + sr])
				pnt3 = point([maxx,	 	miny + r])
				first_point3 = pnt1
				last_point3 = pnt3
				edgs.append(segment(last_point2, first_point3).doit())
				edgs.append(arc(pnt1,pnt2,pnt3).doit())
			else:
				first_point3 = point([maxx, miny])
				last_point3 = point([maxx, miny])
				edgs.append(segment(last_point2, first_point3).doit())
			edgs.append(segment(last_point3, first_point0).doit())

			return edgs 			

		else:
			pnts = points([[minx,miny], [minx,maxy], [maxx,maxy], [maxx,miny]])
			
			for i in range(1, len(pnts)):
				edgs.extend(segment(pnts[i-1], pnts[i]).edges())
			edgs.extend(segment(pnts[-1], pnts[0]).edges())

			return edgs

#class WireObject_Transformed(WireObject, Transformation):
#	def __init__(self,trans):
		

def circle(r):
	return WireObject_Circle(r)

def rectangle(vec, **kwargs):
	return WireObject_Rectangle(vec, kwargs)

def segment(pnt1, pnt2):
	return WireObject_Segment(pnt1, pnt2)

def ngon(r, n):
	return WireObject_Ngon(r, n)

def arc(pnt1, pnt2, pnt3):
	return WireObject_Arc(pnt1, pnt2, pnt3)