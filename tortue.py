from math import sqrt
import turtle
import numpy as np

t = turtle.Turtle()
t.speed(0)


def move_to(x: int, y: int, write: bool = False):
    if write is False:
        t.pendown()
    else:
        t.up()
    t.setheading(0)
    t.setpos(x, y)
    t.pendown()


def sommet(c, x):
    t.setheading(0)
    t.up()
    t.setpos(x, 0)
    t.down()
    t.circle(15)
    t.up()
    t.setpos(x, 5)
    t.write(c, False, align="center", font=("Ariel", 10, "normal"))


def arc(x, a):
    if x - a > 0:
        t.setheading(180)
        t.up()
        t.setpos(a, 0)
    else:
        t.setheading(0)
        t.up()
        t.setpos(a, 30)
    t.left(90)
    t.down()
    t.circle(abs(x - a) / 2, 180)
    t.right(135)
    t.forward(5)
    t.backward(5)
    t.right(90)
    t.forward(5)


def arcp(x, a, p):
    if x - a > 0:
        t.setheading(180)
        t.up()
        t.setpos(a, 0)
    else:
        t.setheading(0)
        t.up()
        t.setpos(a, 30)
    t.left(90)
    t.down()
    t.circle(abs(x - a) / 2, 90)
    t.write(p, align="center")
    t.circle(abs(x - a) / 2, 90)
    t.right(135)
    t.forward(5)
    t.backward(5)
    t.right(90)
    t.forward(5)


def graph(m: np.ndarray, base_dist: int = 100, weight: bool = True):
    n = len(m)
    r = range(n)
    pos = np.arange((1 - n) / 2, (n + 1) / 2) * base_dist
    for i in r:
        sommet(i, pos[i])
    for i in r:
        for j in set(r) - {i}:
            if m[i, j] != 0:
                if weight:
                    arcp(pos[i], pos[j], m[i, j])
                else:
                    arc(pos[i], pos[j])
