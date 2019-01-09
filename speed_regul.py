#!/usr/bin/env python3
#coding: utf-8

from zencad import *
lazy.diag = True

##Base

# Conic body
re1 = 33 / 2
re2 = 38.5 / 2
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

scaletrans = scaleY(1.51) # 1.45

def conic_body():

	ctr = multitrans([right(rdel), left(rdel), forw(rdel), back(rdel)])
	return (
		cone(r1=re1, r2=re2, h=h) 
		+ cone(r1=re1*1.51, r2=re2*1.51, h=h, angle=(0,deg(90)))
		- halfspace().rotateY(-math.atan2(h,re2-re1)).right(re1)
		- cylinder(r=rc, h=hc).up(t) 
		- cylinder(r=ri, h=t)
		- ctr(cylinder(r=rhole, h=t))
		+ rotate_array(tooth_total)(cylinder(r=rcyl, h=h-t).up(t).forw(rc))
	)

base = conic_body()

## Holder

def make_holder():
	polyg_xseg = 4.5
	polyg_yseg = 4.5
	hold_fil = 3
	hold_fil2 = 1

	eey = 2.8
	hold_t = 3

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
	m = m.rotateY(deg(90)).up(polyg_xseg*4).left(hold_t/2).forw(re2 - polyg_yseg*0.4 + 1.5)
	return m
	
holder = make_holder()

display(holder)
show()

sys.exit()

m = (holder - cone(r1=re1, r2=re2, h=h)) + base

hrebr = 23
rebr = cylinder(r=re2*1.51, h=hrebr).up(h) - cylinder(r=re2*1.51-2, h=hrebr).up(h)
rebr = rebr - halfspace().rotateX(-deg(90)) - halfspace().rotateY(deg(90)) - halfspace().rotateY(-deg(90+30)).right(re2).up(h)

m = m + rebr

display(m)
show()
