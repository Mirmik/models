#!/usr/bin/env python3

from zencad import *

ct = 1
cr = 20
hr = 10

ft = 2

w = 40

cyl = cylinder(r=cr + ct, h=hr) - cylinder(r=cr, h=hr) 
cyl = cyl + (
	rotate_array(3)(box(ct,cr,hr/2, center=True).forw(cr/2).up(hr/4).rotateZ(deg(75)))
	+ cylinder(r=3, h=hr/2) 
	- cylinder(r=2, h=hr/2)
)

cyl = cyl.translate(w,w,0)
cyl = sqrtrans()(cyl)

cylrem = cylinder(r=cr + ct, h=hr)
cylrem = cylrem.translate(w,w,0)
cylrem = sqrtrans()(cylrem)

holder = (cylinder(r=3, h=hr) 
	+ box(ct,cr,hr,center=True)
		.forw(cr/2).up(hr/2)
			.rotateZ(deg(-45))
	- cylinder(r=2, h=hr) 
)
holder = holder.translate(45/2,45/2,0)
holder = sqrtrans()(holder) - cylrem

cylrem = cylrem +  sqrtrans()(cylinder(r=3, h=hr).translate(45/2,45/2,0))

crest = box(ct, w*2, hr*0.8, center=True).rotateZ(deg(45)).up(hr/2 - hr*0.2/2)
crest = crest + crest.rotateZ(deg(90))

crest = crest - cylrem

frame = (box(2*w+ft/2,2*w+ft/2,hr,center=True) - box(2*w-ft/2,2*w-ft/2,hr,center=True)).up(hr/2) - cylrem


tcyl = cylinder()
#table = box(45,45,ct,center=True)


m = cyl + frame + holder + crest #+ table 
m = unify(m)

bodyunit = zencad.assemble.unit(shape=m)

if __name__ == "__main__":
	disp(m)
	show()