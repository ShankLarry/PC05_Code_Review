#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Sep 14 14:26:17 2020

@author: bricewilson
"""

from turtle import * 
import random
bgcolor("black")
colormode(255)


panel = Screen()
w = 600 
h = 600 
panel.setup(width=w, height=h)  



panel.setworldcoordinates(0, w, h, 0)

speed(8)
up()
goto(450,150)
down()
color(160,234,222)
REPEATS = range(40)
for element in REPEATS:
    circle(18)
    forward(10)
    right(10)
  
up()
goto(100,150)
down()
color(250,169,22)
begin_fill()
triangle = range(3)
for element in triangle:
    forward(150)
    left(120)
end_fill()

up()
goto(110,400)
down()
color(141,107,148)
begin_fill()
hexagon = range(6)
for element in hexagon:
    forward(100)
    left(60)
end_fill()
up()

goto(450,480)
down()
color(255,16,83)
begin_fill()
square = range(4)
for element in square:
    forward(120)
    left(90)
end_fill()
    