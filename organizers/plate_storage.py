#!/usr/bin/env python3
#coding: utf-8

import runpy
from zencad import *

organizer = runpy.run_path("./base/organizer.py")

m = organizer["storage"](m=1,n=3,w=120,h=40,l=120,t=1.5,d=10,d2=20)

display(m)
show()