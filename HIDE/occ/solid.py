from OCC.BRepPrimAPI import BRepPrimAPI_MakeBox, BRepPrimAPI_MakeCone, BRepPrimAPI_MakeWedge, \
	BRepPrimAPI_MakeSphere, BRepPrimAPI_MakeTorus, BRepPrimAPI_MakeCylinder, BRepPrimAPI_MakePrism

from OCC.BRepPrim import BRepPrim_Cylinder 
from OCC.BRepBuilderAPI import BRepBuilderAPI_MakeEdge

from OCC.BRepOffsetAPI import BRepOffsetAPI_ThruSections
from OCC.gp import gp_Dir


import occ.topo as topo
import occ.geom as geom
#import occ.wire as wire

class solid(topo.shape):
	def __init__(self, shp):
		topo.shape.__init__(self)
		self.shp = shp

def box(x, y, z, center_xy=False):
	if center_xy:
		start = geom.point(-x/2,-y/2,0)
	else:
		start = geom.point(0,0,0)
	return solid(BRepPrimAPI_MakeBox(start.native(), x, y, z).Shape())

def cylinder(r, h=None, center = False):
	if center:
		return cylinder(r,h,False).down(h/2)	
	return solid(BRepPrimAPI_MakeCylinder(r, h).Shape())
#
def sphere(r, center = geom.origin()):
		return solid(BRepPrimAPI_MakeSphere(center.native(), r).Shape())
#
#class sphere_part(topo.solid):
#	def __init__(self, r, theta1, theta2, phi, ax2 = geom.planeOXY()):
#		topo.solid.__init__(self)
#		self.shp = BRepPrimAPI_MakeSphere(ax2.native(), r, theta1, theta2, phi).Shape()
#
#class wedge(topo.solid):
#	def __init__(self, dx, dy, dz, xmin, zmin, xmax, zmax, pln = geom.planeOXY()):
#		topo.solid.__init__(self)
#		self.shp = BRepPrimAPI_MakeWedge (pln.native(), dx, dy, dz, xmin, zmin, xmax, zmax).Shape()
#
#class torus(topo.solid):
#	def __init__(self, r1, r2):
#		topo.solid.__init__(self)
#		self.shp = BRepPrimAPI_MakeTorus(r1, r2).Shape()			
#

def torus(r1, r2, ax2 = geom.planeOXY()):
		return solid(BRepPrimAPI_MakeTorus(ax2.native(), r1, r2).Shape())			

def torus_part(r1, r2, theta1, theta2, phi, ax2 = geom.planeOXY()):
		return solid(BRepPrimAPI_MakeTorus(ax2.native(), r1, r2, theta1, theta2, phi).Shape())			

#
#class cone(topo.solid):
#	def __init__(self, r1, r2, h):
#		topo.solid.__init__(self)
#		self.shp = BRepPrimAPI_MakeCone (r1, r2, h).Shape()	
#
def prism(obj, arg = geom.vector(0,0,1)):
		if isinstance(arg, float) or isinstance(arg, int):
			arg = geom.vector(0,0,arg) 
		return solid(BRepPrimAPI_MakePrism(obj.native(), arg.native()).Shape())
