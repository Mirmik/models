#!/usr/bin/env python3
#coding: utf-8

from zencad import *

#t = 0.5
#r = 1.5
#
#h = r*math.cos(gr(30))
#a = r
#
#x_size =100
#y_size =20
#
#n = int(x_size / r)
#m = int(y_size / r)
#
#hexagon = linear_extrude(ngon(r=r+t/2,n=6) - ngon(r=r-t/2,n=6), t)
#
#xnet = multitransform(
#	[forw(2*h*i) for i in range(0,n)]
#)(hexagon)
#
#onet = xnet + xnet.translate(r+a/2, h, 0)
##r+r/math.sqrt(3) - t / math.cos(gr(30))
#net = multitransform(
#	[translate(i*(2*r+a),0,0) for i in range(0,m)]
#)(onet)
#
#display(net)
#show() 


r = 3
a=r
h = r * math.cos(gr(30)) 
t = 1
s = 0.5

ri = r - t/2
ro = r + t/2

size_x = 180
size_y = 180

m = int(size_x / h/2) 
n = int(size_y / h/2)

plate_hexagon = ngon(r=ro, n=6)
plate_line = multitransform([forw(2*h*i) for i in range(0,m)])(plate_hexagon)
plate = multitransform([translate(i*(r+a/2),h*(i%2),0) for i in range(0,n)])(plate_line)

holes_hexagon = ngon(r=ri, n=6)
holes_line = multitransform([forw(2*h*i) for i in range(0,m)])(holes_hexagon)
holes = multitransform([translate(i*(r+a/2),h*(i%2),0) for i in range(0,n)])(holes_line)

display(linear_extrude(plate - holes,s))
show()