#!/usr/bin/env python3
#coding: utf-8

from zencad import *

# корпус крепления
base1 = box(30, 40, 30, center = True)
base1 = base1.up(15)
# вырез под шланг
virez = box(15 , 15 , 30, center = True)
virez = virez.forw(15)
virez = virez.up(15)
# отверстие под душ
cone1 = cone(10, 11.5, 30)
cone1 = cone1.forw(5)
# крепление к стене
krep = box(50, 5, 30)
krep = krep.translate(-25, 0, 0)

# отверстия под саморезы 
krep1 = cylinder(2, 5, center = False)
krep1 = krep1.rotateX(deg(-90))
krep1 = krep1.translate(17.5, 0, 15)

# потай для саморезов
cone2 = cone(2, 4, 3)
cone2 = cone2.rotateX(deg(-90))
cone2 = cone2.translate(17.5, 2, 15)

# конус для закручивания
cone3 = cone(2, 4, 25)
cone3 = cone3.rotateX(deg(90))
cone3 = cone3.translate(17.5, 30, 15)

virez2 = krep1 + cone2 + cone3
virez3 = virez2 + virez2.moveX(-35)

# summary
base1 = base1 - cone1 - virez#base + base1 - krep1 - krep2
base1 = base1.forw(25)
base1 = base1 + krep - virez3
base1 = base1.fillet(3, refs=[(13.45195,45.00000,12.08970),
                              point3(-15.00000,44.58277,19.68265),
                              point3(7.50000,44.58372,12.70448),
                              point3(7.50000,37.80426,7.23947),
                              point3(7.50000,41.53330,29.77320),
                              point3(-7.50000,37.79587,12.18445),
                              point3(-7.50000,44.65081,12.03689),
                              point3(-7.50000,41.59087,29.99750),
                              point3(24.59345,2.90774,30.00000),
                              point3(-23.34343,2.55344,30.00000),
                              point3(-25.00000,2.30786,0.31608),
                              point3(25.00000,2.91760,0.23813)
])

disp(base1)

show()
