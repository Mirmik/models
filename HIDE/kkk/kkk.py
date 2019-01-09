#!/usr/bin/env python3
#coding: utf-8

import zencad
from zencad import pnt, gr
import zencad.face as face
import zencad.solid as solid
import zencad.wire as wire
import zencad.stl as stl
from zencad.widget import display, show

import math

m = solid.box(30, 30, 1) - solid.box(10, 15, 1).translate(10,8,0) + solid.box(10 - 0.8*2, 15 - 0.8, 1).translate(10 + 0.8,8,0)

display(m)
show()