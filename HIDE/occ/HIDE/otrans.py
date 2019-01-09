from occ.topo import shape

class transform_object:
	def __init__(self, base, trsf):
		self.base = base
		self.trsf = trsf

	def transform(self, atrsf):
		self.trsf = self.trsf * atrsf

	def doit(self):
		if (isinstance(self.base, shape)):
			return shape.do_transform(self.trsf)