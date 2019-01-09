import occsimple.geom2d
import math

def array_union(arr):
	model = arr[0]
	for i in range(1,len(arr)):
		model += arr[i]
	return model

def rotate_array(m, n):
	return occsimple.mlib.array_union([m.rotateZ(2*math.pi / n * i) for i in range(0,n)])
	#ret = m
	#for i in range (1, n):
	#	ret = ret + m.rotateZ(math.radians(360./n * i))
	#return ret

def rounded_angle(y, z, x, w, angles):
	a = occsimple.geom2d.rectangle([x,y], rounded = (2, [i for i in angles if i < 2])).linear_extrude(w)
	b = occsimple.geom2d.rectangle([x,z], rounded= (2, [i-2 for i in angles if i >= 2])).linear_extrude(w)
	return a + b.rotateX(math.pi/2).forward(w)

def central_circles_array(central, side, radius, num):
	return  occsimple.geom2d.circle(central) + rotate_array((occsimple.geom2d.circle(side).right(radius)), num)
