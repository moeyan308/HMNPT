from swampy.TurtleWorld import *
import math
while 1:
    #sides=int(input("Please input sides of polygon. "))
    #length=int(input("Please input length of polygon. "))
    world=TurtleWorld()
    t=Turtle()
    t.delay=0.001
    def polygon(t,n,length):
        for i in range(n):
            fd(t,length)
            lt(t,360/n)
    def circle(t,radius):
        circumference=2 * math.pi *radius
        n=int(circumference/3)+1
        length=circumference/n
        polygon(t,n,length)
    circle(t,50)
    wait_for_user()
    exit(-1)

