#!/usr/bin/env python3
#coding: utf-8

import runpy
from zencad import *

organizer = runpy.run_path("./base/organizer.py")

x = 118
y = 118
z = 38

t = 1.5

m = 1
n = 1

hand = cylinder(r = z / 2, h = t*2)-box(z,z,t*2).left(z/2)

diff_x = box(x, t, z-t)
diff_y = box(t, y, z-t)

model = box(x, y, z) - box(x-2*t, y-2*t, z-t).translate(t,t,t)

if m > 1: model = model + union([diff_x.forw((y-t) / m * i) for i in range(1, m)])
if n > 1: model = model + union([diff_y.right((x-t) / n * i) for i in range(1, n)])

model = model + hand.rotateY(gr(90)).right(x/2-t).up(z/2)

display(model)
show()