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

"""
The solution is way more complicated but doesn't use any extra space

Our lives would be easier without the linear time constraint: we would just sort the array
while filtering out negative numbers, and iterate over the sorted array and return the first
number that doesn't match the index. However, sorting takes O(n log n), so we can't use that here.

Clearly we have to use some sort of trick here
to get it running in linear time. Since the first missing
positive number must be between 1 and len(array) (why?), we
can ignore any negative numbers and numbers bigger than len(array).
The basic idea is to use the indices of the array itself to reorder the
elements to where they should be. We traverse the array and swap
elements between 0 and the length of the array to their value's index.
We stay at each index until we find that index's value and keep on swapping.

By the end of this process, all the first positive numbers
should be grouped in order at the beginning of the array.
We don't care about the others. This only takes O(N)
time, since we swap each element at most once.

Then we can iterate through the array and return the index of the first number that doesn't match, just like before.
"""
def first_missing_positive(nums):
    if not nums:
        return 1
    for i, num in enumerate(nums):
        while i + 1 != nums[i] and 0 < nums[i] <= len(nums):
            v = nums[i]
            nums[i], nums[v - 1] = nums[v - 1], nums[i]
            nums[v - 1] = v
            if nums[i] == nums[v - 1]:
                break
    for i, num in enumerate(nums, 1):
        if num != i:
            return i
    return len(nums) + 1
