from swampy.TurtleWorld import *
import math

world = TurtleWorld()
bob = Turtle()
bob.delay = 0.01
print(bob)


def polygon(t, n, length):
    angle = 360/n
    for i in range(n):
        fd(t, length)
        lt(t, angle)


def circle(t, r):
    circumference = 2 * math.pi * r
    n = 50
    length = circumference / n
    polygon(t, n, length)


def arc(t, r, angle):
    #   t=turtle r=radius a=angle, in degrees
    arc_length = 2 * math.pi * r * angle / 360
    n = int(arc_length / 3)
    step_length = arc_length / n
    step_angle = float(angle)/n
    for i in range(n):
        fd(t, step_length)
        lt(t, step_angle)


def petal(t, r, angle):
    for i in range(2):
        arc(t, r, angle)
        t.lt(180-angle)


def flower(t, n, r, angle):
    for i in range(n):
        petal(t, r, angle)
        t.lt(360/n)


def move(t, length):
    t.pu()
    t.fd(length)
    t.pd()


def draw_line(t, length):
    t.fd(length)


def draw_three_flowers(t, r, a):
    move(t, 300)
    for i in range(3):
        flower(t, 20, r, a)
        move(t, -150)


draw_three_flowers(bob, 50, 30)

wait_for_user()
