#!/usr/bin/env python3
"""
Given a list of numbers and a number k, return whether any two numbers from the list add up to k.

For example, given [10, 15, 3, 7] and k of 17, return true since 10 + 7 is 17.

Bonus: Can you do this in one pass?

ALSO MADE IT RETURN COUNT FOR EACH ONE IF COUNT = Size of list or less, it was one pass
"""

ls = [10,15,3,7]
ls_big = [4,2,3,1,5,13,5,12,8,0]
ls_dup = [4,2,4,1]
ls_fail = [4,2,1,3,18,500,32,24,12,78]
k = 17

"The first thing that comes to mind is just a double for loop but that is O(n^2)"
def check_sum_bad(nums, k):
    count = 0
    for i in range(len(nums)):
        count += 1
        for j in range(i+1,len(nums)):
            count += 1
            if nums[i] + nums[j] == k:
                return (count, True)
    return (count, False)

print("\n This is the bad way to do things")
print("check_sum_bad(%s,%s):" % (ls,k),check_sum_bad(ls, k))
print("check_sum_bad(%s,%s):" % (ls,35),check_sum_bad(ls, 35))
print("check_sum_bad(%s,%s):" % (ls_big,8),check_sum_bad(ls_big, 8))
print("check_sum_bad(%s,%s):" % (ls_big,36),check_sum_bad(ls_big, 36))
print("check_sum_bad(%s,%s):" % (ls_fail,k),check_sum_bad(ls_fail, k))

#doing this in one try might be kind of tough. Let's try it

"""
{k-ls[0]:ls[0]} ls 
"""
def check_sum_dict(nums, k):
    dict_list = {k-i:i for i in nums}
    for i in nums:
        if (dict_list[i] == k-i):
            return True
    return False
print("\n Check Sum with Dict Comprehension")
print("check_sum_dict(%s,%s):" % (ls,k),check_sum_dict(ls, k))
print("check_sum_dict(%s,%s):" % (ls_big,8),check_sum_dict(ls_big, 8))
"""
So I'm doing it this way because 
"""
def check_sum_one_pass(nums, k):
    dict_list = {}
    count = 0
    for i in nums:
        count += 1
        if k-i in dict_list: 
            return (count,True)
        else:
            dict_list[i] = k-i
    return (count,False)


print("\n THIS MIGHT BE ONE PASS")
print("check_sum_one_pass(%s,%s):" % (ls,17),check_sum_one_pass(ls, 17))
#should return true
print("check_sum_one_pass(%s,%s):" % (ls_dup,8),check_sum_one_pass(ls_dup, 8))
#should return true
print("check_sum_one_pass(%s,%s):" % (ls_fail,8),check_sum_one_pass(ls_fail, 8))
#should return false
print("check_sum_one_pass(%s,%s):" % (ls_big,8),check_sum_one_pass(ls_big, 8))
#should return true
print("check_sum_one_pass(%s,%s):" % (ls_big,10),check_sum_one_pass(ls_big, 10))