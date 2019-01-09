#!/usr/bin/env python3

from zencad import *
import evalcache

lazy.diag=True

m = from_brep("a.brep")
ret = to_brep(m, "b.brep")

m2 = from_brep("b.brep")
m2 = m2 + box(50,50,50)

display(m2)
show()