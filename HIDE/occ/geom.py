from OCC.gp import gp_Pnt, gp_Vec, gp_Dir, gp_Ax1, gp_Ax2, gp_Ax3, gp_XYZ, gp_Lin,  gp_Circ
#import occ.curve as crv


#class xyz:
#	def __init__(self, *args):
#		if len(args) == 1 and isinstance(args[0], xyz):
#			self.xyz = args[0].xyz
#		elif len(args) == 1 and isinstance(args[0], gp_XYZ):
#			self.xyz = args[0]
#		else:
#			self.xyz = gp_XYZ(*args)
#
#	def __repr__(self):
#		return str((self.xyz.X(), self.xyz.Y(), self.xyz.Z()))
#
#	def get(self):
#		return self.xyz


class can_transform:
	def transformed(self, trans):
		return self.__class__(self.native().Transformed(trans.get()))

	def translated(self, x, y, z):
		return self.__class__(self.native().Translated(gp_Vec(x,y,z)))		

	def rotated(self, ax, angle):
		return self.__class__(self.native().Rotated(ax.native(), angle))	

	def rotate(self, ax, angle):
		self.native().Rotate(ax.native(), angle)

	def mirrored(self,arg):
		return self.__class__(self.native().Mirrored(arg.native()))	

	def scaled(self, center, scl):
		return self.__class__(self.native().Scaled(center.native(), scl))	

class point(can_transform):
	def __init__(self, *args):
		if isinstance(args[0], point):
			self.pnt = args[0].pnt
		elif isinstance(args[0], gp_Pnt):
			self.pnt = args[0]	
		else:
			self.pnt = gp_Pnt(args[0], args[1], args[2])

	def __repr__(self):
		return str((self.pnt.X(), self.pnt.Y(), self.pnt.Z()))

	def native(self):
		return self.pnt

class vector(can_transform):
	def __init__(self, *args):
		if isinstance(args[0], vector):
			self.vec  = args[0].pnt
		elif isinstance(args[0], point):
			self.vec  = gp_Vec(args[0].native().XYZ())
		elif isinstance(args[0], gp_Vec):
			self.vec = args[0]	
		else:
			self.vec = gp_Vec(args[0], args[1], args[2])

	def __repr__(self):
		return str((self.vec.X(), self.vec.Y(), self.vec.Z()))

	def __neg__(self):
		impl = self.vec
		return vector(-impl)

	def native(self):
		return self.vec

def origin():
	return point(0,0,0)

class line(can_transform):
	def __init__(self, *args):
		if len(args) == 2:
			self.ln = gp_Lin(args[0].native(), args[1].native())
		else:
			self.ln = args[0]

	def location(self):
		return point(self.ln.Location())

	def direction(self):
		return direction(self.ln.Direction())

	def __repr__(self):
		return str((self.location(), self.direction()))
		
	def native(self):
		return self.ln

class direction(can_transform):
	def __init__(self, *args):
		if isinstance(args[0], direction):
			self.dir  = args[0].dir
		elif isinstance(args[0], gp_Dir):
			self.dir = args[0]	
		else:
			self.dir = gp_Dir(args[0], args[1], args[2])

	def __repr__(self):
		return str((self.dir.X(), self.dir.Y(), self.dir.Z()))

	def native(self):
		return self.dir

	def translated(self, *args):
		raise Exception("direction can't be translated")

class axis:
	def __init__(self, pnt, dr):
		self.ax = gp_Ax1(pnt.native(), dr.native())

	def native(self):
		return self.ax

def axisOX():
	return axis(origin(), direction(1,0,0))

def axisOY():
	return axis(origin(), direction(0,1,0))

def axisOZ():
	return axis(origin(), direction(0,0,1))

class plane(can_transform):
	def __init__(self, pnt, dir_n, dir_x = None):
		if dir_x == None:
			self.pln = gp_Ax2(pnt.native(), dir_n.native())
		else:
			self.pln = gp_Ax2(pnt.native(), dir_n.native(), dir_x.native())

	def native(self):
		return self.pln

def planeOXY():
	return plane(origin(), direction(0,0,1), direction(1,0,0))

def planeOXZ():
	return plane(origin(), direction(0,1,0), direction(-1,0,0))

def planeOYZ():
	return plane(origin(), direction(1,0,0), direction(0,1,0))

class frame(can_transform):
	def __init__(self, pnt, dir_n, dir_x = None):
		if dir_x == None:
			self.frm = gp_Ax3(pnt.native(), dir_n.native())
		else:
			self.frm = gp_Ax3(pnt.native(), dir_n.native(), dir_x.native())

	def native(self):
		return self.frm

def frameOXYZ():
	return frame(origin(), direction(0,0,1), direction(1,0,0))

class circle(can_transform):
	def __init__(self, radius, plane = planeOXY()):
		if isinstance(radius, gp_Circ):
			self.circ = radius
		else:
			self.circ = gp_Circ(plane.native(), radius)

	def native(self):
		return self.circ