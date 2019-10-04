#!/usr/bin/env python3
"""
This problem was asked by Airbnb.

Given a linked list and a positive integer k, rotate the list to the right by k places.

For example, given the linked list 7 -> 7 -> 3 -> 5 and k = 2, it should become 3 -> 5 -> 7 -> 7.

Given the linked list 1 -> 2 -> 3 -> 4 -> 5 and k = 3, it should become 3 -> 4 -> 5 -> 1 -> 2.
"""
#The list comprehension way of doing things seems to work pretty well
def rotate(ls,k):
    return [ls[(i-k) % len(ls)] for i, x in enumerate(ls)]



print(rotate([1,3,7,7],2))
print(rotate([1,5,6,3],1))
