#!/usr/bin/env python3

from zencad import *

#box1 = box(40, 60, 50)

box1 = box(63, 22, 3, center = True)
box1 = box1.translate(0, 0, 1.5)

cyli1 = cylinder(19/2, 22, center = True)
cyli1 = cyli1.rotateX(deg(-90))
cyli1 = cyli1.translate(0, 0, 19/2)

cyli2 = cylinder(25/2, 22, center = True)
cyli2 = cyli2.rotateX(deg(-90))
cyli2 = cyli2.translate(0, 0, 19/2)

box2 = box(25, 22, 19, center = True)
box3 = box(15, 22, 15, center = True)

cone1 = cone(2, 4, 3, center = True)
cone1 = cone1.translate(-42.5/2, 0, 1.5)

cone2 = cone(2, 4, 3, center = True)
cone2 = cone2.translate(42.5/2, 0, 1.5)

pnts1 = points([
    (0, 0, 0),
    (21, 0, 0),
    (21, 0, 16),
    ])

seg1 = polysegment(pnts1, closed = True)
seg1 = seg1.fill()
seg1 = seg1.extrude(vec=(0, 3, 0))

seg2 = seg1.translate(-31.5, 8, 0)
seg1 = seg1.translate(-31.5, -11, 0)

seg3 = seg1.mirrorZ()
seg4 = seg2.mirrorZ()

cyli2 = cyli2 + box2 - box3 - cyli1 - halfspace()

box1 = box1 - box3 - cone1 - cone2 + seg1 + seg2 + seg3 + seg4 + cyli2
box1 = box1.fillet(2.9, [(30, 4, 3), (-30, -3, 3)])

box1 = unify(box1)
display(box1)
#display(cyli2)
#display(seg1)
#display(seg2)
#display(seg3)
#display(seg4)
#display(cone1)
show()

