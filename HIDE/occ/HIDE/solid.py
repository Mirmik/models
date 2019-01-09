from OCC.BRepPrimAPI import BRepPrimAPI_MakeBox, BRepPrimAPI_MakeCone, BRepPrimAPI_MakeWedge, BRepPrimAPI_MakeSphere, BRepPrimAPI_MakeTorus, BRepPrimAPI_MakeCylinder

from occ.topo import solid
from occ.geom import planeOXY, planeOXZ, origin, point

class box(solid):
	def __init__(self, x, y, z, center_xy=False):
		solid.__init__(self)
		self.x = x
		self.y = y
		self.z = z
		if center_xy:
			self.start = point(-x/2,-y/2,0)
		else:
			self.start = point(0,0,0)

	def construct(self):	
		return BRepPrimAPI_MakeBox(self.start.doit(), self.x, self.y, self.z).Shape()

class wedge(solid):
	def __init__(self, dx, dy, dz, xmin, zmin, xmax, zmax, pln = planeOXY()):
		solid.__init__(self)
		self.dx = dx
		self.dy = dy
		self.dz = dz
		self.xmin = xmin
		self.xmax = xmax
		self.zmin = zmin
		self.zmax = zmax
		
	def construct(self):	
		return BRepPrimAPI_MakeWedge (self.pln.doit(), self.dx, self.dy, self.dz, self.xmin, self.zmin, self.xmax, self.zmax).Shape()

class sphere(solid):
	def __init__(self, r, center = origin()):
		solid.__init__(self)
		self.r = r
		self.center = center
	
	def doit(self):	
		return BRepPrimAPI_MakeSphere(self.center.doit(), self.r).Shape()			

class part_sphere(solid):
	def __init__(self, r, theta1, theta2, phi, ax2 = planeOXY()):
		solid.__init__(self)
		self.ax2 = ax2
		self.r = r
		self.phi = phi
		self.theta1 = theta1
		self.theta2 = theta2

	def construct(self):	
		return BRepPrimAPI_MakeSphere(self.ax2.doit(), self.r, self.theta1, self.theta2, self.phi).Shape()

class cylinder(solid):
	def __init__(self, r, h, angle = None, pln = None):
		solid.__init__(self)
		self.r = r
		self.h = h
		self.angle = angle
		self.pln = pln
	
	def construct(self):	
		if (self.angle == None and self.pln == None):
			return BRepPrimAPI_MakeCylinder(self.r, self.h).Shape()
		elif(self.pln == None):
			return BRepPrimAPI_MakeCylinder(self.r, self.h, self.pln.doit()).Shape()
		else:
			return BRepPrimAPI_MakeCylinder(self.pln.doit(), self.r, self.h, self.angle).Shape()

class torus(solid):
	def __init__(self, r1, r2):
		solid.__init__(self)
		self.r1 = r1
		self.r2 = r2
		
	def construct(self):	
		return BRepPrimAPI_MakeTorus(self.r1, self.r2).Shape()			


class cone(solid):
	def __init__(self, r1, r2, h):
		solid.__init__(self)
		self.r1 = r1
		self.r2 = r2
		self.h = h
		
	def construct(self):	
		return BRepPrimAPI_MakeCone (self.r1, self.r2, self.h).Shape()	
