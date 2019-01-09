from OCC.Geom import Geom_Circle
from occ.geom import planeOXY 
from OCC.BRepBuilderAPI import BRepBuilderAPI_MakeEdge, BRepBuilderAPI_MakeWire

class curve:	
	def __init__(self):
		pass

	def edge(self):
  		return BRepBuilderAPI_MakeEdge(self.doit().GetHandle()).Edge();
	
def as_edge(arg):
	if isinstance(arg, curve):
		return arg.edge()
	else:
		return arg

class circle(curve):
	def __init__(self, r, ax2 = planeOXY()):
		curve.__init__(self)
		self.r = r
		self.ax2 = ax2

	def doit(self):
		return Geom_Circle(self.ax2.doit(), self.r)

class elips(curve):
	def __init__(a, b):
		self.a = a
		self.b = b

	def doit():
		pass


class wire:
	def __init__(self, *args):
		self.edges = [as_edge(e) for e in args]

	def doit(self):
		maker = BRepBuilderAPI_MakeWire(*self.edges)
		return maker.Wire()


