#!/usr/bin/env python3
#coding: utf-8

from zencad import *

pnts = [(-10,10), (0,7), (10, 10)]
arc= circle_arc(*pnts)

arc4 = rotate_array(4)(arc)
arc4 = sew(arc4.edges())
arc4 = arc4.fill()

m = arc4.extrude(5)

disp(m)
show()
