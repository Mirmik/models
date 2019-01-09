from OCC.Geom import Handle_Geom_Line, Handle_Geom_Geometry, Handle_Geom_Curve, Geom_Line, Geom_Circle, Geom_BezierCurve, Geom_TrimmedCurve
from OCC.GeomAPI import GeomAPI_Interpolate
from OCC.TColgp import TColgp_Array1OfPnt, TColgp_HArray1OfPnt, Handle_TColgp_HArray1OfPnt
import occ.geom as geom

class curve(geom.can_transform):
	def __init__(self, arg = None):
		geom.can_transform.__init__(self)
		if isinstance(arg, geom.line):
			self.crv = Geom_Line(arg.native())
		elif isinstance(arg, geom.circle):
			self.crv = Geom_Circle(arg.native())
		else:
			self.crv = arg

	def native(self):
		return self.crv

	#def transformed(self, trans):
		#print("HERE")
		#return curve(Handle_Geom_Curve.DownCast(self.get().Transformed(trans.get())))

	def trimmed(self, a, b):
		return curve(Geom_TrimmedCurve(Handle_Geom_Line(self.native()), a, b))

class line(curve):
	def __init__(self, *args):
		curve.__init__(self)
		if isinstance(args[0], Handle_Geom_Geometry):
			self.holder = args[0]
			self.crv = Handle_Geom_Curve.DownCast(args[0])
		else:
			self.crv = Geom_Line(args[0].native(), args[1].native());

class circle(curve):
	def __init__(self, r, plane = geom.planeOXY()):
		curve.__init__(self)
		self.crv = Geom_Circle(plane.native(), r);

def lineOX():
	return line(geom.origin(), geom.direction(1,0,0))

def lineOY():
	return line(geom.origin(), geom.direction(0,1,0))

def lineOZ():
	return line(geom.origin(), geom.direction(0,0,1))

class bezier(curve):
	def __init__(self, points):
		curve.__init__(self)
		arr = TColgp_Array1OfPnt(1, len(points))
		for idx, p in enumerate(points):
			arr.SetValue(idx + 1, p.native())
		self.crv = Geom_BezierCurve(arr)

class interpolate(curve):
	def __init__(self, points, closed = False):
		curve.__init__(self)
		arr = TColgp_HArray1OfPnt(1, len(points))
		for idx, p in enumerate(points):
			arr.SetValue(idx + 1, p.native())
		interpolate = GeomAPI_Interpolate(Handle_TColgp_HArray1OfPnt(arr), closed, 0.00000001)
		interpolate.Perform()
		self.crv = interpolate.Curve()

	