from time import sleep
from swampy.TurtleWorld import *
from math import pi
world = TurtleWorld()
t = Turtle()
t.delay = 0.01
while 1:
    def polyline(t,n,length,angle):
        """This Function is used for drawing Line"""
        for i in range(n):
            fd(t,length)
            lt(t,angle)


    def polygon(t,n,length):
        """This Function is used for drawing Polygon"""
        angle=360/n
        polyline(t,n,length,angle)

    def arc(t,radius,angle):
        """This Function is used for drawing arc or circle."""
        circumference = 2*pi*radius*angle/360
        n=int(circumference/3)+1
        step_length=circumference/n
        step_angle=float(angle)/n
        polyline(t,n,step_length,step_angle)



    def petal(t,radius,angle):
        """This Function is used for Drawing Petal
            t=Turtle
            radius=radius of arc
            angle=angle  of ar"""
        for i in range(2):
            arc(t,radius,angle)
            lt(t,180-angle)
    def flower(t,radius,nopetal,angle):
        betangle=float(360/nopetal)
        for i in range(nopetal):
            petal(t,radius,angle)
            lt(t,betangle)


    def move(t,length):
        pu(t)
        fd(t,length)
        pd(t)
    def do_n(arc,t,length,angle,n):
        if n <= 0:
            print("done")
            return
        else:
            arc(t,length,angle)
            move(t, 100)
            do_n(arc,t,length,angle,n-1)

    move(t,-100)
    do_n(arc,t,50,360,4)
    wait_for_user()
    exit(-1)


