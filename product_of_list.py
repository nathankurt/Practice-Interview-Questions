#!/usr/bin/env python3
"""
Given an array of integers, return a new array such that each element at index i of the new array is the product of all the numbers in the original array except the one at i.

For example, if our input was [1, 2, 3, 4, 5], the expected output would be [120, 60, 40, 30, 24]. If our input was [3, 2, 1], the expected output would be [2, 3, 6].

Follow-up: What if you can't use division?
"""
from functools import reduce


"""
This one takes the list, gets the sum of it then divides by I
"""
def list_product_division(ls):
    new_ls = []
    if len(ls) == 0:
        return []
    else:
        full_list_prod = reduce(lambda x,y : x * y, ls, 1)
        for i in ls:
            # reduce is used to multiply the list together to turn it into one value.
            # then it divides that by i to get the correct value. 
            new_ls.append(full_list_prod/i)

        return new_ls

print(list_product_division([1,2,3,4,5]))
print(list_product_division([]))

"""This one uses enumedrate to exlude the value from a list and then reduces it all to multiply"""
def list_product_no_division(ls):
    final_list = []
    if len(ls) == 0:
        return []
    else:
        for i in range(len(ls)):
           #Excludes i index from list but i think it's quadratic.
           new_list = [elem for j, elem in enumerate(ls) if j != i] 
           final_list.append(reduce(lambda x,y : x * y, new_list, 1))
        return final_list


print(list_product_no_division([1,2,3,4,5]))
print(list_product_no_division([]))


""" 
The answer from the problem without using division here

Without division, another approach would be to first see that the ith element simply needs the product of numbers before i and the product of numbers after i. Then we could multiply those two numbers to get our desired product.

In order to find the product of numbers before i, we can generate a list of prefix products. Specifically, the ith element in the list would be a product of all numbers including i. Similarly, we would generate the list of suffix products.

This runs in O(N) time and space, since iterating over the input arrays takes O(N) time and creating the prefix and suffix arrays take up O(N) space.

"""

def products(nums):
    # Generate prefix products
    prefix_products = []
    for num in nums:
        if prefix_products:
            prefix_products.append(prefix_products[-1] * num)
        else:
            prefix_products.append(num)

    # Generate suffix products
    suffix_products = []
    for num in reversed(nums):
        if suffix_products:
            suffix_products.append(suffix_products[-1] * num)
        else:
            suffix_products.append(num)
    suffix_products = list(reversed(suffix_products))

    # Generate result
    result = []
    for i in range(len(nums)):
        if i == 0:
            result.append(suffix_products[i + 1])
        elif i == len(nums) - 1:
            result.append(prefix_products[i - 1])
        else:
            result.append(prefix_products[i - 1] * suffix_products[i + 1])
    return result
