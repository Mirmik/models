#!/usr/bin/env python3
#coding: utf-8

import runpy
from zencad import *
import argparse

organizer = runpy.run_path("./base/organizer.py")

parser = argparse.ArgumentParser(description='Process some integers.')
parser.add_argument('--x', type=float, default=120)
parser.add_argument('--y', type=float, default=120)
parser.add_argument('--z', type=float, default=40)
parser.add_argument('--m', type=int, default=1)
parser.add_argument('--n', type=int, default=1)
parser.add_argument('--t', type=float, default=1.5)
parser.add_argument('--s', type=float, default=1)
parser.add_argument('--model', type=str)

args = parser.parse_args()

print(args)

x = args.x
y = args.y
z = args.z

t = args.t
s = args.s

m = args.m
n = args.n

model = args.model

if model == "case":	
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

	m = do_model(x - s, y - s, z - s, t, m, n)
	
	display(m)
	show()


if model == "storage":
	m = organizer["storage"](m=m,n=n,w=x,h=z,l=y,t=t,d=10,d2=z/2)
	display(m)
	show()


