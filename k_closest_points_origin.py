#!/usr/bin/env python3

#TODO Add max heap sort integration
from math import sqrt
"""
Given a list of tuples find the k closest points to the origin(0,0)
IE
Points = [(-2,4), (0,-2), (-1,0), (2,5), (-2,-3), (3,2)]
Find the 2 closest points to the origin
two closest points here are (-1,0) and (0,-2) so list those
"""

points_tuple = [(-2,4), (0,-2), (-1,0), (2,5), (-2,-3), (3,2), (1,0)]


###Used to get the distance from origin. which is hypotenuse so x^2 + y^2
def distance(tup):
    return (sqrt(tup[0]**2 + tup[1] **2))
    #could also just do **.5 instead of sqrt

"""
I'm not sure if this works if there are two points that are the same distance away, may be better to use zip
"""
def closest_points(tuple_list, k):
    
    #This gets the distances for all of the items and stores it in a dict with the key being the distance and the value being the 
    distance_dict = {distance(k):k for k in tuple_list}
    ls = sorted(distance_dict)
    return [distance_dict[j] for j in ls[:k]]

print("\n this is the wrong way to do it because the dictionary key can only have one value and negative/positive numbers are the same")
print(closest_points(points_tuple, 3))


def closest_points_zip(tuple_list, k):
    distance_list = sorted(zip([distance(tup) for tup in tuple_list],tuple_list))

    """Could also do this if you wanted to switch the order
    distance_list = sorted(zip(tuple_list, [distance(tup) for tup in tuple_list]), key=lambda x: x[1])
    return [x[0] for x in distance_list[:k]]
    """
    return [x[1] for x in distance_list[:k]]


print("\n This seems like the most pythonic way of doing it!")
print("Closest 3 Points: ", closest_points_zip(points_tuple, 3))
print("Closest 4 Points: ", closest_points_zip(points_tuple, 4))

"""
Doing this with classes seems probably like the cleanest way to do this. 
"""
class Point:
    def __init__(self, tup):
        self.coords = tup
        self.distance = sqrt(tup[0]**2 + tup[1]**2)

def closest_points_class(tuple_list, k):
    point_list = sorted([Point(tup) for tup in tuple_list],key=lambda x: x.distance)
    return [x.coords for x in point_list[:k]]

print("\n This is the way to do it with a class that works well")
print("Closest 3 Points: ", closest_points_class(points_tuple, 3))
print("Closest 4 Points: ", closest_points_class(points_tuple, 4))
