#!/usr/bin/env python3.5
#coding: utf-8

import runpy
from zencad import *

organizer = runpy.run_path("./base/organizer.py")
model = organizer["case"](w=27,h=20,l=64,t=1.5,r=27/2-4,z=1,s=0.965)

display(model)
show()