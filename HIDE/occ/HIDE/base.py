#from occ.trans import translate, rotate, mirror, scale

class occ_object:
	def __init__(self):
		self.obj = None

	def constructed(self):
		raise Exception("CONSTRUCTED NEED TO IMPLEMENT")

	def changed(self):
		self.obj = None

	def doit(self):
		if self.obj != None:
			return self.obj
		self.obj = self.construct()
		return self.obj

