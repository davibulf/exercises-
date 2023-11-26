from swampy.TurtleWorld import *
import math

world = TurtleWorld()
bob = Turtle()
bob.delay = 0.01
print(bob)


def polyline_dw(t, n, length, angle):
    for i in range(n):
        fd(t, length)
        rt(t, angle)


def arc_dw(t, r, angle):

    arc_length = 2 * math.pi * r * abs(angle) / 360
    n = int(arc_length / 4) + 1
    step_length = arc_length / n
    step_angle = float(angle) / n

    # making a slight left turn before starting reduces
    # the error caused by the linear approximation of the arc
    rt(t, step_angle/2)
    polyline_dw(t, n, step_length, step_angle)
    lt(t, step_angle/2)


def draw_a(t, h):
    k = math.sin(60 * math.pi / 180) * (h/2)
    m = math.sqrt((h/2)**2 - k**2)
    t.lt(60)
    t.fd(h)
    t.rt(120)
    t.fd(h)
    t.rt(180)
    t.fd(h/2)
    t.lt(60)
    t.fd(m*2)
    t.pu()
    t.lt(180)
    t.fd(m*2)
    t.rt(60)
    t.fd(h/2)
    t.lt(60)
    t.fd(50)
    t.pd()


def draw_b(t, h):
    k = math.sin(60 * math.pi / 180) * h
    t.lt(90)
    t.pu()
    t.fd(h/6)
    t.pd()
    t.fd(k)
    t.rt(90)
    t.fd(h/8)
    arc_dw(bob, int(h / 6), 180)
    t.fd(h/8)
    t.rt(180)
    t.fd(h/8)
    arc_dw(bob, (h / 3), 180)
    t.fd(h/8)
    t.rt(90)
    t.fd(h / 2)
    t.rt(180)
    t.fd(h / 2)
    t.rt(90)
    t.pu()
    t.rt(180)
    t.fd((h/8)+(h/4)+50)
    t.pd()


def draw_d(t, h):
    k = math.sin(60 * math.pi / 180) * h
    t.lt(90)
    t.fd(k)
    t.rt(90)
    arc_dw(t, h/2, 180)
    t.rt(90)
    t.fd(h/2)
    t.rt(180)
    t.fd(h/2)
    t.rt(90)
    t.pu()
    t.rt(180)
    t.fd((h/2)+50)
    t.pd()


size = 200
draw_d(bob, size)
draw_a(bob, size)
draw_b(bob, size)
draw_b(bob, size)
draw_a(bob, size)

wait_for_user()
