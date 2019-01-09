from OCC.BRepAlgoAPI import BRepAlgoAPI_Fuse, BRepAlgoAPI_Cut

def native_shape_cut(a,b):
	return BRepAlgoAPI_Cut(a.native(), b.native()).Shape()\

def native_shape_fuse(a,b):
	return BRepAlgoAPI_Fuse(a.native(), b.native()).Shape()