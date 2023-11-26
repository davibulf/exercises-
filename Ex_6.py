from swampy.TurtleWorld import *
import math

world = TurtleWorld()
bob = Turtle()
bob.delay = 0.01
print(bob)


def square(t, length):
    for i in range(4):
        fd(t, length)
        lt(t)


def polygon(t, n, length):
    angle = 360/n
    for i in range(n):
        fd(t, length)
        lt(t, angle)


def circle(t, r):
    circumference = 2 * math.pi * r
    n = 50
    length = circumference/n
    polygon(t, n, length)


def arc(t, r, angle):
    arc_length = 2 * math.pi * r * angle / 360
    n = int(arc_length / 3)
    step_length = arc_length / n
    step_angle = float(angle)/n
    for i in range(n):
        fd(t, step_length)
        lt(t, step_angle)


def polyline(t, n, length, angle):
    for i in range(n):
        fd(t, length)
        lt(t, angle)


def polygon_2(t, n, length):
    angle = 360/n
    polyline(t, n, length, angle)


def arc_2(t, r, angle):
    arc_length = 2 * math.pi * r * angle / 360
    n = int(arc_length/3) + 1
    step_length = arc_length / n
    step_angle = float(angle) / n
    polyline(t, n, step_length, step_angle)


square(bob, 50)
wait_for_user()
