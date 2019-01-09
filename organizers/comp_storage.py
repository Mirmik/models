#!/usr/bin/env python3
#coding: utf-8

import runpy
from zencad import *

import sys

if len(sys.argv) != 3:
	print("Usage: './comp_storage (m) (n)', when (m) and (n) is matrix dimention")
	exit(0)

organizer = runpy.run_path("./base/organizer.py")
model = organizer["storage"](int(sys.argv[1]),int(sys.argv[2]),27,20,64,1.5,5,5)

display(model)
show()