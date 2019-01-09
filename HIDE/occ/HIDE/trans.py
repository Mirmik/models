from OCC.gp import gp_Trsf, gp_Vec
from occ.geom import origin
from occ.base import occ_object

class translate:
	def __init__(self, *args):
		if len(args) == 1:
			self.x = args[0].x
			self.y = args[0].y
			self.z = args[0].z
		else:
			self.x = args[0]
			self.y = args[1]
			self.z = args[2]

	def doit(self):
		ret = gp_Trsf()
		ret.SetTranslation(gp_Vec(self.x, self.y, self.z))
		return ret

class rotate:
	def __init__(self,ax,angle):
		self.ax = ax
		self.angle = angle

	def doit(self):
		ret = gp_Trsf()
		ret.SetRotation(self.ax.doit(), self.angle)
		return ret

class mirror:
	def __init__(self,arg):
		self.arg = arg
		
	def doit(self):
		ret = gp_Trsf()
		ret.SetMirror(self.arg.doit())
		return ret

class scale:
	def __init__(self,n,center=origin()):
		self.n = n
		self.center = center

	def doit(self):
		ret = gp_Trsf()
		ret.SetScale(self.n, self.center.doit())
		return ret