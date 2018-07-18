#!/usr/bin/env python3



"""
N Represents number of steps, W represents number of ways to get
up steps assuming you can only take one or two steps at a time
N = 0 W = 1 <- { [0] }
N = 1 W = 1 <- { [1,0] }
N = 2 W = 2 <- { [2,1,0], [2,0] }
N = 3 W = 3 <- { [3,2,1,0], [3,2,0], [3,1,0] }
N = 4 W = 5 <- { [4,3,2,1,0], [4,3,2,0], [4,3,1,0], [4,2,1,0], [4,2,0] }

num_ways(3) = num_ways(2) + num_ways(1)
num_ways(n) = num_ways(n-1) + num_ways(n-2)
"""

###JUST TESTING CRAP OUT, THIS IS PROBABLY WRONGcd
# def num_ways(stairs, steps_set, count):
#     stairs_remaining = stairs
#     for i in steps_set:
#         if (stairs_remaining - i) >= 0:
#             stairs_remaining -= i
#             num_ways(stairs_remaining, steps_set, count)
#     count += 1
#     return count



"""
Well I guess this isn't haskell so this won't work
"""
# def num_ways(stairs):
#     #"First start with base cases"
#     num_ways(0) = 1
#     num_ways(1) = 1
#     num_ways(stairs) = num_ways(stairs - 1) + num_ways(stairs - 2)

def num_ways(stairs):
    "First start with base cases"
    if stairs == 1 or stairs == 0:
        return 1
    else:
        return (num_ways(stairs - 1) + num_ways(stairs - 2))

print("num_ways(4): ", num_ways(4))
#Returns 5

print("num_ways(10): ",  num_ways(5))
#Returns 8

print("num_ways(10): ", num_ways(10))
#Reutnrs 89


"""
This other way is pretty wasteful so we'll do a bottom up approach
"""
def num_ways_bottom_up(stairs):
    "Have to start with base cases again"
    if stairs == 1 or stairs == 0:
        return 1
    #look at that fancy match case to make an empty list filled with 10 nums 
    nums = [None for _ in range(stairs+1)]
    nums[0] = 1
    nums[1] = 1
    for i in range(2,stairs+1):
        nums[i] = nums[i-1] + nums[i-2]
    return nums[stairs]
        
        

print("num_ways_bottom_up(4): ", num_ways_bottom_up(4))
#Returns 5

print("num_ways_bottom_up(10): ",  num_ways_bottom_up(5))
#Returns 8

print("num_ways_bottom_up(10): ", num_ways_bottom_up(10))
#Reutnrs 89


"""
Given Number of steps at a time(X) = {1,3,5} and Total number of stairs(N)

X = {1,3,5}, N = 2
num_ways(N) = (num_ways(n - 1) + num_ways(n - 3) + num_ways(n-5))


"""

def num_ways_set(stairs, steps):
    if stairs == 1 or stairs == 0:
        return 1
    #Oh man look at that list comprehension
    return sum([num_ways(stairs - x) for x in steps])

print("num_ways_set(10, [1,3,5]):", num_ways_set(10, [1,3,5]) )
#returns 84

print("num_ways_set(15, [1,3,5]):", num_ways_set(15, [1,3,5]) )
#returns 932

print("num_ways_set(10, [1,2])", num_ways_set(10, [1,2]))