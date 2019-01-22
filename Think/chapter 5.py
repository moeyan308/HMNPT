#!/usr/bin/python3
import time
from swampy.TurtleWorld import *
import math
world = TurtleWorld()
t = Turtle()
while 1:
    #a = int(input("Value of A= "))                             #i/p for check_fermat and is_triangle
    #b = int(input("Value of B= "))                             #i/p for check_fermat and is_triangle
    #c = int(input("Value of C= "))                             #i/p for check_fermat and is_triangle
    #n = int(input("Value of n= "))                             #i/p for check_fermat and is_triangle
    #Fermet_integer=n                                           #i/p for check_fermat and is_triangle
    def check_fermat(a,b,c,n):
        if n > 2:
            if (a**n+b**n == c**n):
                print("Holy smokes,Fermat was Wrong.")
            else:
                pass
        else:
            print("No interger between {} to {} violate Fermat's Theorem.".format(2,Fermet_integer))
            print("n must be greater than 2")
            exit(-1)
        check_fermat(a,b,c,n-1)


    def is_triangle(a,b,c):
        if a+b<c:
            print("No.")
        elif a+c<b:
            print("No.")
        elif b+c<a:
            print("No.")
        else:
            print("Yes")

    def draw(t,length,n):
        if n==0:
            return
        angle=50
        fd(t,length*n)
        lt(t,angle)
        draw(t,length,n-1)
        rt(t,2*angle)
        print(n)
        print("=====================")
        draw(t,length,n-1)
        lt(t,angle)
        bk(t,length*n)

    def koch(t,n):
        if n<3:
            fd(t,n);
            return
        m=n/3
        # print(n)
        koch(t,m)
        lt(t,60)
        koch(t,m)
        rt(t,120)
        koch(t,m)
        lt(t,60)
        koch(t,m)
    def snowflake(t,n):
        for i in range(3):
            koch(t,n)
            rt(t,120)

    koch(t,30)
    wait_for_user()
    exit(-1)

