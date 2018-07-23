#!/usr/bin/env python3

"""
Find the lowest missing positive number that doesn't exist in an array

For example [3,4,-1,1] would Return 2 
[1,2,0] would return 3

can contain duplicates and negative numbers
"""


"""
The first way I could think to do this would be with just a counter starting at 1
if it finds one, go up. else return that number.
This is pretty slow and bad though I assume. I could make it a set 
"""
def find_missing_num_while(ls):
    count = 1
    while count in ls:
        count += 1
    return count

print("find_missing_num_while([1,2,0]):",find_missing_num_while([1,2,0]))

"""
Using a set here would make things way faster 
so turn it into a set and try that
"""
def find_missing_num_set(ls):
    count = 1
    #Use a set because that's way faster for finding val in list
    ls = set(ls)
    while count in ls:
        count+=1
    return count

print("find_missing_num_set([1,1,3,4,6]):",find_missing_num_set([1,1,3,4,6]))