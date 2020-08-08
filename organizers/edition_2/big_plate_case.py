#!/usr/bin/env python3
#coding: utf-8

import runpy
from zencad import *
from big_plate_param import *

organizer = runpy.run_path("../base/organizer.py")

def do_model(x,y,z,t,m,n):
	#Формируем ручку из половины цилиндра
	hand = cylinder(r = z / 2, h = t*2)-box(z,z,t*2).left(z/2)

	#Разделительные перегородки
	diff_x = box(x, t, z-t)
	diff_y = box(t, y, z-t)
	
	#Базовая коробка
	model = box(x, y, z) - box(x-2*t, y-2*t, z-t).translate(t,t,t)
	
	#Расставляем разделительные перегородки
	if m > 1: model = model + union([diff_x.forw((y-t) / m * i) for i in range(1, m)])
	if n > 1: model = model + union([diff_y.right((x-t) / n * i) for i in range(1, n)])
	
	#Собираем изделие
	model = model + hand.rotateY(gr(90)).right(x/2-t).up(z/2)

	return model


s = 1.2
to_stl(do_model(x - s, y - s, z - s, t, 2, 3), "./big_case_2x3_1.2.stl", 0.01)
to_stl(do_model(x - s, y - s, z - s, t, 2, 2), "./big_case_2x2_1.2.stl", 0.01)
to_stl(do_model(x - s, y - s, z - s, t, 1, 2), "./big_case_1x2_1.2.stl", 0.01)

s = 2.0
to_stl(do_model(x - s, y - s, z - s, t, 2, 3), "./big_case_2x3_2.0.stl", 0.01)
to_stl(do_model(x - s, y - s, z - s, t, 2, 2), "./big_case_2x2_2.0.stl", 0.01)
to_stl(do_model(x - s, y - s, z - s, t, 1, 2), "./big_case_1x2_2.0.stl", 0.01)

