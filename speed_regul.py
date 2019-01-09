#!/usr/bin/env python3
#coding: utf-8

from zencad import *
lazy.diag = True

##Base
#scaletrans = scaleY(1.51) # 1.45

re1 = 33 / 2
re2 = 38.5 / 2
h = 7
	
def make_body(r1, r2, h):
	# Conic body
	h = 7
	
	# Internal cylinder
	rc = 31 / 2 + 0.5
	hc = 5
	
	ri = 23 / 2 # Central hole radius
	t = h - hc # Central part height
	
	rdel = 27 / 2 # Screw`s to center radius
	rhole = 1 # Screw`s hole radius
	
	rcyl = 0.8 # Tooth radius
	tooth_total = 54 # Count of toothes

	ctr = multitrans([right(rdel), left(rdel), forw(rdel), back(rdel)])
	return (
		cone(r1=r1, r2=r2, h=h) 
		- cylinder(r=rc, h=hc).up(t) 
		- cylinder(r=ri, h=t)
		- ctr(cylinder(r=rhole, h=t))
		+ rotate_array(tooth_total)(cylinder(r=rcyl, h=h-t).up(t).forw(rc))
	)

def make_base_support(r1, r2, h):
	return (
		cone(r1=r1*1.51, r2=r2*1.51, h=h, angle=(0,deg(90)))
		- halfspace().rotateY(-math.atan2(h,r2-r1)).right(r1)
		- cone(r1, r2, h)
	)
	
def make_holder():
	polyg_xseg = 4.5
	polyg_yseg = 4.5
	hold_t = 3
	
	hold_fil = 3
	hold_fil2 = 1
	eey = 2.8

	polyg = polygon([
		(polyg_xseg*0,		polyg_yseg*0.5), 
		(polyg_xseg, 		polyg_yseg*0.5),
		(polyg_xseg*2, 		polyg_yseg),
		(polyg_xseg*4, 		polyg_yseg),
		(polyg_xseg*4, 		polyg_yseg*3.5),
		(polyg_xseg*2, 		polyg_yseg*3.5),
		(polyg_xseg*0, 		polyg_yseg*3),
		(polyg_xseg*(-1),	polyg_yseg*2),
		(polyg_xseg*(-1),	polyg_yseg*1),
	]).left(polyg_xseg*3)
	
	polyg = polyg.fillet(hold_fil)
	
	m = polyg.extrude(hold_t).fillet(hold_fil2)
	m = m + mirrorYZ()(m)
	
	hh = polygon([(0,-4), (-2,2), (-12,6), (5,8), (5,-4)]).extrude(hold_t).right(polyg_xseg*4-5).fillet(hold_fil2)

	c = circle(r=hold_t / 3 * 2).rotateY(deg(90)).forw(polyg_yseg*3.5)
	path = interpolate([
		(3*polyg_xseg, 		polyg_yseg*eey),
		(0*polyg_xseg, 		polyg_yseg*3.5),
		(-3*polyg_xseg, 	polyg_yseg*eey)
	])

	sph = sphere(hold_t / 3 * 2)
	det = pipe(c, path) + sph.translate(3*polyg_xseg, polyg_yseg*eey, 0) + sph.translate(-3*polyg_xseg, polyg_yseg*eey, 0)
	det = det.up(hold_t/2)

	m = m + det
	return m.rotateY(deg(90)).up(polyg_xseg*4).left(hold_t/2).forw(polyg_yseg*0.4 + 1.5)

def make_rebr(r, t, h, xblade, angle):
	rebr = cylinder(r=r, h=h) - cylinder(r=r-t, h=h)
	rebr = difference([
		rebr, 
		halfspace().rotateX(-deg(90)),
		halfspace().rotateY(deg(90)),
		halfspace().rotateY(-deg(90)-angle).right(xblade)
	])
	return rebr
	
base = 			make_body(r1=re1, r2=re2, h=h)
base_support = 	make_base_support(r1=re1, r2=re2, h=h)
holder = 		make_holder().forw(re2)
rebr = 			make_rebr(re2*1.51, 2, 23, xblade=re2, angle=deg(30)).up(h)

m = union([
	holder,
	base,
	base_support,
	rebr
])

display(m)
show()
