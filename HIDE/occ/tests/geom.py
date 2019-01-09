#!/usr/bin/env python3
#coding: utf-8

import sys
sys.path.append("../..")

import math
from occ.gui import display, start_display
from occ.geom import point, direction, vector, axis, plane, frame, origin
from occ.trans import translate, rotate, mirror, scale, rotateX, rotateY, rotateZ

display(origin())

start_display()