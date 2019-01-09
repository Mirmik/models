#!/usr/bin/env python3.5
#coding: utf-8

from zencad import *

def section(w, h, l, t, d, d2):
	return (
		  box(2*t+w, t+l, 2*t+h)
		- box(w, l, h).translate(t,0,t)
		- box(w-2*d,l,h+2*t).translate(t+d,0,0)
		- box(w,l+t,h-d2).translate(t,0,d2+t)
	)

#n, m - параметры матрицы.
#w,h,l - параметры нишы.
#t - толщина стенок.
#d - выступ поддержки.
#d2 - высота заднего бампера.
def storage(m, n, w, h, l, t, d, d2, corners = None):
	x = w*m+t*(m+1)
	y = h*n+t*(n+1)
	z = l + t

	sect = section(w,h,l,t,d,d2)
	line = union([sect.translate(j*(w+t),0,0) for j in range(0, m)])

	arr = []
	for i in range(0, n):
		arr.append(line.up(i*(h+t)))

	arr.append(box(w*m+t*(m+1), l+t, t))
	arr.append(box(w*m+t*(m+1), l+t, t).up(n*(h+t)))

	ret = union(arr).rotateX(gr(-90)).up(z).left(x)

	if corners: 
		c = cylinder(r=corners["r"], h=corners["h"]) - box(corners["r"], corners["r"], corners["h"])
		c = c
		ret = (
			ret 
			+ c.rotateZ(gr(90))
			+ c.translate(-x,0,0)
			+ c.rotateZ(gr(180)).translate(0,y,0)
			+ c.rotateZ(gr(-90)).translate(-x,y,0)
		)

	return ret




def case(w,h,l,t,r,z,s):
	w = w*s #Запас по ширине
	h = h*0.95 #Запас по высоте
	
	return (
		#Базовая коробка
		box(w,l,h) - box(w-2*t, l-2*t,h-t).translate(t,t,t)

		#Вычитаем цилиндр под ручку
		- cylinder(r=r,h=t+1).rotateX(gr(90)).translate(w/2,t+0.5,h) 

		#Формируем держатель ярлыка
		+ box(w-2*t, z*2, h-r).translate(t,-z*2,0) 
		- box(w-2*t-2*z, z, h-r-z).translate(t+z,-z,z) # Внутренняя полость
		- box(w-2*t-6*z, z, h-r-2*z).translate(t+z*3,-2*z,2*z) #Внешняя полость
	)