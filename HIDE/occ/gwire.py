class wire(can_transform):
	def __init__(self):
		pass

class wire_fuse(wire):
	def __init__(self, a, b):
		protowire.__init__(self)
		self.a = a
		self.b = b

	def edges(self):
		return self.a.edges() + self.b.edges()
