"""Sternenhimmel aus 'Progammieren mit Python supereasy'(ISBN'978-3-8310-3457-4')[S.90]"""
import turtle as t
from random import randint, random
import keyboard
import os


def draw_star(points, size, col, x, y):
    t.penup()
    t.goto(x, y)
    t.pendown()
    angle = 180 - (180 / points)
    t.color(col)
    t.begin_fill()
    for i in range(points):
        t.forward(size)
        t.right(angle)
    t.end_fill()


#Main
t.Screen().bgcolor("dark blue")
t.speed("fastest")

while keyboard.is_pressed("r") == False:
    ranPoi = randint(5, 25)
    #Ungrade SterneS
    ranPoi = int(int(ranPoi / 2) * 2 + 1) 
    ranSize = randint(5, 75)
    ranCol = (random(), random(), random())
    ranX = randint(-350, 300)
    ranY = randint(-250, 250)
    print(ranPoi)

    draw_star(ranPoi, ranSize, ranCol, ranX, ranY)

os.system("pause")