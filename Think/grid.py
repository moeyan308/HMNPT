#!usr/bin/python
#This program is dedicated to print grid on screen
while 1:
    a=0
    row=int(input("Please enter row number= "))
    column=int(input("Please enter Column number= "))
    def do_twice(f):
        f()
        f()
    def do_four(f,a):
        f(a)
        f(a)
        f(a)
        f(a)
    def print_beam(a):
        print("+----"*a+'+')
    def print_post(a):
        print("|    " * a + '|')
        print("|    " * a + '|')
        print("|    " * a + '|')
        print("|    " * a + '|')
    def print_column(a):
        print_beam(column)
        print_post(column)
        print_beam(column)




    print_column(a)

