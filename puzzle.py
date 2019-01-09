#!/usr/bin/env python3

from zencad import *

N = 6

r0 = 20
r1 = 13
r2 = 6

cr = 2
cs = 1
t = 1
s = 3
h = 5

multrans = multitransform([rotateZ(deg(360/N*i)) for i in range(0,N)])

m0 = circle(r = r0, angle = deg(55)) - circle(r1 + t/2)
m1 = circle(r = r1 - t/2, angle = deg(55)) - circle(r2 + t/2)

cm = circle(r = r2)

c = circle(r = cr)#.forw(r1+cr-cs)
bc = c.scale(1.10)
sc = c.scale(0.95)

trans0 = rotateZ(deg(30)) * right(r1+cr-cs)
trans10 = rotateZ(deg(55 - 4)) * right((r2 + r1) / 2)
trans11 = rotateZ(deg(-4)) * right((r2 + r1) / 2)

m0 = m0 - trans0(bc)
m1 = m1 + trans0(sc) - trans10(bc) + trans11(sc) 

marr0 = multrans(m0) - multrans(trans0(bc))
marr1 = multrans(m1) + multrans(trans0(sc))

display(marr0.extrude(5))
display(marr1.extrude(5))

show()