#!/usr/bin/env python3
#coding: utf-8

import dzencad.solid as solid
from dzencad.widget import *

m = solid.box(10,10,10) + solid.sphere(5).translate(5,5,10)

display(m)
show()