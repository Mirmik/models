from OCC.gp import gp_Trsf
import occ.util as util
import occ.geom as geom

class transformation:
	def __init__(self, arg = None):
		if arg:
			self.trsf = arg
		else: 
			self.trsf = gp_Trsf()
		
	def __mul__(self,other):
		return transformation(self.get() * other.get())

	def get(self):
		return self.trsf

	def __call__(self, arg):
		return arg.transformed(self)

	def invert(self):
		return transformation(self.get().Inverted())

	def get_translation(self):
		return geom.xyz(self.get().TranslationPart())

class translate(transformation):
	def __init__(self, *args):
		transformation.__init__(self)
		self.trsf.SetTranslation(util.as_vector(*args).native())

class rotate(transformation):
	def __init__(self, ax, angle):
		transformation.__init__(self)
		self.trsf.SetRotation(ax.native(), angle)

class mirror(transformation):
	def __init__(self, arg):
		transformation.__init__(self)
		self.trsf.SetMirror(arg)

class scale(transformation):
	def __init__(self, arg):
		transformation.__init__(self)
		self.trsf.SetScale(geom.origin().pnt, arg)

class toframe(transformation):
	def __init__(self,frm):
		transformation.__init__(self)
		self.trsf.SetTransformation(frm.native())

class locframe(transformation):
	def __init__(self,p3,d3):
		transformation.__init__(self)
		self.trsf.SetTransformation(geom.frame(geom.point(*p3), geom.direction(*d3)).native(), geom.frameOXYZ().native())

class frame_transformation(transformation):
	def __init__(self,frm0,frm1):
		transformation.__init__(self)
		self.trsf.SetTransformation(frm0.native(), frm1.native())

def rotateX(angle):
	return rotate(geom.axisOX(), angle)

def rotateY(angle):
	return rotate(geom.axisOY(), angle)

def rotateZ(angle):
	return rotate(geom.axisOZ(), angle)