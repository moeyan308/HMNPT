from swampy.TurtleWorld import *
import math
world=TurtleWorld()
t=Turtle()
t.delay=0.01
while 1:
    def polyline(t,n,length,angle):
        for i in range(n):
            fd(t,length)
            lt(t,angle)
    def polygon(t,n,length):
        for i in range(n):
            angle=360/n
            fd(t,length)
            lt(t,angle)

    def arc(t, r, angle):
        arc_length = 2 * math.pi * r * angle / 360
        n = int(arc_length / 3) + 1
        step_length = arc_length / n
        step_angle = float(angle) / n

        polyline(t,n,step_length,step_angle)
    def circle(t,r):
        arc(t,r,360)

    circle(t,30)
    wait_for_user()
    exit(-1)
