#!/usr/bin/env python3

"""
cons(a, b) constructs a pair, and car(pair) and cdr(pair) returns the first
and last element of that pair. For example, car(cons(3, 4)) returns 3, and cdr(cons(3, 4)) returns 4.

car(cons(3,4)) returns 3

cdr(cons(3,4)) returns 4

given cons implement car and cdr
"""

"""
This is provided
Cons takes in a and b and returns a new anonymous function
returns a new anonymous function pair
"""
def cons(a, b):
    def pair(f):
        return f(a, b)
    return pair

"""
my solution .to get a and b back we can use closure object
Anonymous functions used here 
https://stackoverflow.com/questions/14413946/what-exactly-is-contained-within-a-obj-closure
"""
def car_my(pair):
    return pair.__closure__[0].cell_contents

def cdr_my(pair):
    return pair.__closure__[1].cell_contents

print("\n My Answer:")
print("car_my(cons(1,2)):", car_my(cons(1,2)))
print("cdr_my(cons(1,2)):", cdr_my(cons(1,2)))


"""
This lambda way to do it is probably much better
also more legible 
"""
def car_answer(pair):
    return pair(lambda a, b: a)

def cdr_answer(pair):
    return pair(lambda a, b: b)

print("\n Their answer:")
print("car_my(cons(4,5)):", car_my(cons(4,5)))
print("cdr_my(cons(4,5)):", cdr_my(cons(4,5)))
