import occ.geom as geom
import math

def degree(angle):
	return math.pi / 180 * angle

def as_vector(*args):
	if isinstance(args[0], geom.vector):
		return args[0]
	else:
		return geom.vector(*args)

def union(*args):
	ret = args[0]
	for i in range(1,len(args)):
		ret = ret + args[i]
	return ret

def difference(*args):
	ret = args[0]
	for i in range(1,len(args)):
		ret = ret - args[i]
	return ret

def points(pnts):
	return [geom.point(p[0], p[1], p[2]) for p in pnts]

def multiple_transform(obj, arr):
	return union(*[obj.transformed(t) for t in arr])