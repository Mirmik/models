from OCC.gp import gp_Pnt, gp_Vec, gp_Dir, gp_Ax1, gp_Ax2, gp_Ax3, gp_Trsf
from occ.base import occ_object

class point(occ_object):
	def __init__(self, *args):
		occ_object.__init__(self)
		if len(args) == 1:
			self.x = args[0].x
			self.y = args[0].y
			self.z = args[0].z
		else:
			self.x = args[0]
			self.y = args[1]
			self.z = args[2]

	def construct(self):
		return gp_Pnt(self.x, self.y, self.z)

def origin():
	return point(0,0,0)

class direction(occ_object):
	def __init__(self, *args):
		occ_object.__init__(self)
		if len(args) == 1:
			self.x = args[0].x
			self.y = args[0].y
			self.z = args[0].z
		else:
			self.x = args[0]
			self.y = args[1]
			self.z = args[2]

	def construct(self):
		return gp_Dir(self.x, self.y, self.z)

class axis:
	def __init__(self, pnt, dr):
		occ_object.__init__(self)
		self.pnt = pnt
		self.dir = dr
		
	def construct(self):
		return gp_Ax1(pnt.pnt, dir.dir)

def axisOX():
	return axis(origin(), direction(1,0,0))

def axisOY():
	return axis(origin(), direction(0,1,0))

def axisOZ():
	return axis(origin(), direction(0,0,1))

class plane(occ_object):
	def __init__(self, pnt, dir_n, dir_x = None):
		occ_object.__init__(self)
		self.pnt = pnt
		self.dir_n = dir_n
		self.dir_x = dir_x

	def construct(self):
		if self.dir_x == None:
			return gp_Ax2(self.pnt.doit(), self.dir_n.doit())
		else:
			return gp_Ax2(self.pnt.doit(), self.dir_n.doit(), self.dir_x.doit())

	def location(self):
		return self.doit().Location()

	def dirs(self):
		pln = self.doit()
		return (
			direction(pln.XDirection()),
			direction(pln.YDirection()),
			direction(pln.Direction()),
		)

def planeOXY():
	return plane(origin(), direction(0,0,1), direction(1,0,0))

def planeOXZ():
	return plane(origin(), direction(0,1,0), direction(-1,0,0))

def planeOYZ():
	return plane(origin(), direction(1,0,0), direction(0,1,0))
#