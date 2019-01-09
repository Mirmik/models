from OCC.gp import gp_Pnt, gp_OX, gp_Vec, gp_Mat, gp_XYZ, gp_Dir, gp_Trsf, gp_GTrsf, gp_DZ, gp_Ax1, gp_Ax2, gp_Ax3, gp_Pnt2d, gp_Dir2d, gp_Ax2d
from OCC.BRepBuilderAPI import BRepBuilderAPI_MakeEdge, BRepBuilderAPI_MakeWire, BRepBuilderAPI_MakeFace, \
    BRepBuilderAPI_Transform, BRepBuilderAPI_GTransform, BRepBuilderAPI_Copy
from OCC.BRepOffsetAPI import BRepOffsetAPI_MakePipe
from OCC.BRepPrimAPI import BRepPrimAPI_MakeRevol
from OCC.GC import GC_MakeArcOfCircle, GC_MakeSegment, GC_MakeCircle
from OCC.TopoDS import TopoDS_Shape

import occsimple.base 
import numpy as np

class Transformation:
	def __init__(self, tokens):
		self.tokens = tokens

	def add_token(self, token):
		self.tokens.append(token)

	def do_object3d(self, model):
		#A = BRepBuilderAPI_Copy();
		#A.Perform(model);
		#model = A.Shape()

		mat = np.matrix("1 0 0 0; 0 1 0 0; 0 0 1 0; 0 0 0 1")
		
		full_transform = False
		for t in reversed(self.tokens):
			#if (isinstance(t, MatrixRotationToken)):
			#	full_transform = True
			(dmat, full) = t.get_matrix()
			if full:
				full_transform = True
			mat = mat.dot(dmat)

		if full_transform:
			#print("full transform:")
			#print(mat)
			m = gp_Mat(	gp_XYZ(mat.item((0,0)), mat.item((0,1)), mat.item((0,2))),
						gp_XYZ(mat.item((1,0)), mat.item((1,1)), mat.item((1,2))),
						gp_XYZ(mat.item((2,0)), mat.item((2,1)), mat.item((2,2)))
			)
#	
			v = gp_XYZ(	   mat.item((0,3)),
						   mat.item((1,3)),
						   mat.item((2,3))
			)
#	
			trns = gp_GTrsf(m, v)
			
			brep_trns = BRepBuilderAPI_GTransform(model, trns, False)
			
		else:
			#print("simple transform:")
			#print(mat)
			
			trns = gp_Trsf()
			trns.SetValues(mat.item((0,0)), mat.item((0,1)), mat.item((0,2)),mat.item((0,3)), 
						   mat.item((1,0)), mat.item((1,1)), mat.item((1,2)),mat.item((1,3)),
						   mat.item((2,0)), mat.item((2,1)), mat.item((2,2)),mat.item((2,3)))
		
			brep_trns = BRepBuilderAPI_Transform(model, trns, False)
		
		brep_trns.Build()
		return brep_trns.Shape()

	#def do_wire(self, model):
	#	mat = np.matrix("1 0 0 0; 0 1 0 0; 0 0 1 0; 0 0 0 1")
	#	for t in reversed(self.tokens):
	#		mat = mat.dot(t.get_matrix())
#
	#	trns = gp_Trsf()
	#	trns.SetValues(mat.item((0,0)), mat.item((0,1)), mat.item((0,2)),mat.item((0,3)), 
	#				   mat.item((1,0)), mat.item((1,1)), mat.item((1,2)),mat.item((1,3)),
	#				   mat.item((2,0)), mat.item((2,1)), mat.item((2,2)),mat.item((2,3)))
	#	brep_trns = BRepBuilderAPI_Transform(model, trns, False)
	#	brep_trns.Build()
	#	return brep_trns.Shape()


class TransformationToken:
	pass

class TranslateToken( TransformationToken ):
	def __init__(self, vec):
		self.vec = occsimple.base.vector3d(vec)

	def get_matrix(self):
		return (np.matrix( [
				[1, 0, 0, self.vec.x],
				[0, 1, 0, self.vec.y],
				[0, 0, 1, self.vec.z],
				[0, 0, 0, 	       1],
			]), False)

class RotateAroundVectorToken( TransformationToken ):
	def __init__(self, vec, angle):
		self.vec = vec
		self.angle = angle

	def get_matrix(self):
		vec = np.array([self.vec.x, self.vec.y, self.vec.z])
		norm = np.linalg.norm(vec)
		unit = vec / norm
		l = unit.item(0)
		m = unit.item(1)
		n = unit.item(2)

		c = np.cos(self.angle)
		s = np.sin(self.angle)
		d = (1 - c)

		mat = np.matrix( [
				[l*l*d+c,   m*l*d-n*s, n*l*d+m*s, 0],
				[l*m*d+n*s, m*m*d+c,   n*m*d-l*s, 0],
				[l*n*d-m*s, m*n*d+l*s, n*n*d+c,   0],
				[0, 		0, 		   0, 	 	  1],
			] )
		#print(mat)
		return (mat, False)

class MatrixRotationToken( TransformationToken ):
	def __init__(self, rot):
		self.rot = rot

	def get_matrix(self):
		mat = np.matrix( [
				[self.rot[0][0], self.rot[0][1], self.rot[0][2], 0],
				[self.rot[1][0], self.rot[1][1], self.rot[1][2], 0],
				[self.rot[2][0], self.rot[2][1], self.rot[2][2], 0],
				[0, 						  0, 		  	  0, 1],
			] )
		return (mat, False)

class MirrorToken( TransformationToken ):
	def __init__(self, arg):
		self.arg = occsimple.base.vector3d(arg)

	def get_matrix(self):
		vec = np.array([self.arg.x, self.arg.y, self.arg.z])
		norm = np.linalg.norm(vec)
		unit = vec / norm
		a = unit.item(0)
		b = unit.item(1)
		c = unit.item(2)

		return (np.matrix( [
				[ 1-2*a**2, 	-2*a*b, 	-2*a*c, 0],
				[	-2*a*b,   1-2*b**2, 	-2*b*c, 0],
				[	-2*a*c, 	-2*b*c,   1-2*c**2, 0],
				[		 0, 		 0, 		 0, 1],
			] ), False)
				

def translate(vec):
	def retfunc(model):
		return model.transformation( TranslateToken(vec) )
	return retfunc

def multiply_translate(vecs):
	def f(model):
		return occsimple.mlib.array_union([translate(p)(model) for p in vecs])
	return f

def rotateVec(ax, angle):
	def retfunc(model):
		return model.transformation( RotateAroundVectorToken(ax, angle) )
	return retfunc

def matrix_rotation(rot):
	def retfunc(model):
		return model.transformation( MatrixRotationToken(rot) )
	return retfunc

def mirror(arg):
	def retfunc(model):
		return model.transformation( MirrorToken(arg) )
	return retfunc

#def mirror(xyz):
#	def retfunc(model):
#		return MirrorShape(xyz, model)
#	return retfunc




#utils:

def up(arg):
	return translate([0,0,arg])
def down(arg):
	return translate([0,0,-arg])
def left(arg):
	return translate([-arg,0,0])
def right(arg):
	return translate([arg,0,0])
def forward(arg):
	return translate([0,arg,0])
def back(arg):
	return translate([0,-arg,0])


def rotateX(arg):
	return rotateVec(occsimple.base.vector3d([1,0,0]), arg)
def rotateY(arg):
	return rotateVec(occsimple.base.vector3d([0,1,0]), arg)
def rotateZ(arg):
	return rotateVec(occsimple.base.vector3d([0,0,1]), arg)

def linear_extrude(h):
	def retfunc(face):
		return occsimple.solid.prism(face, [0,0,h])
	return retfunc