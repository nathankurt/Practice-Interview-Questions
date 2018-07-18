#!/usr/bin/env python3

"""
Find the first recurring character for a given string
"ABCA" -> "A"
"BCABA" -> "B"
"ABC" -> "None"
"DBCABA" -> "B"
"""

"This is probably the Naive solution"
"Since it has to check everything, like (n(n-1))/2 so that's O(n^2)"
def find_first_char(string):
    ls = list(string)
    for i in ls:
        if i in ls[1:]:
            return i
        else:
            ls = ls[1:]
    return None

print("\nTHIS IS FOR THE BAD SOLUTION")
print("find_first_char('hello'):", find_first_char("hello"))
#returns l

print("find_first_char('cow'):", find_first_char("cow"))
#returns None

print("find_first_char('DBCABA'):", find_first_char("DBCABA"))
#returns B

"""
This uses a dict, and checks the dict. That way you only have to check each char once instead of multiple times
I think you can do the same thing just with a list instead though. I guess you can make it easily adaptable
to find the first double repeat character. 
Time complexity for this is O(n) because it only has to go through once.
"""
def find_first_char_good_dict(string):
    ls = list(string)
    dictionary = {}
    for i in ls:
        if i in dictionary.keys():
            return i
        else:
            dictionary[i] = 1
    return None

print("\nThis is for the good solution with dict")

print("find_first_char_good('hello'):", find_first_char_good_dict("hello"))
#returns l

print("find_first_char_good('cow'):", find_first_char_good_dict("cow"))
#returns None

print("find_first_char_good('DBCABA'):", find_first_char_good_dict("DBCABA"))
#returns B


"""
This just uses a second list instead of a dict. I think it might be faster because you don't have to assign any values or search for keys. 
Still think it's negligable though.
"""
def find_first_char_good_list(string):
    ls = list(string.strip(" "))
    ls2 = []
    for i in ls:
        if i in ls2:
            return i
        else:
            ls2.append(i)
    return None

print("\nThis is for the good solution with list")

print("find_first_char_good_list('hello'):", find_first_char_good_list("hello"))
#returns l

print("find_first_char_good_list('cow'):", find_first_char_good_list("cow"))
#returns None

print("find_first_char_good_list('DBCABA'):", find_first_char_good_list("DBCABA"))
#returns B
