#! usr/bin/python3

#This program is dedicated for traing while reading Think Python book.

def do_twice(f,arg):
    f(arg)
    f(arg)

def print_twice(arg):
    print(arg)
    print(arg)

do_twice(print_twice,'spam')
print("+",)
print("-")