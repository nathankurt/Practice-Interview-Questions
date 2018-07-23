# Practice-Interview-Questions

Just a bunch of practice interview questions that i'll work on.

## Go To

* [Amazon Coding Interview Question - Recursive Staircase Problem](#amazon-coding-interview-question---recursive-staircase-problem)
* [Google Coding Interview Question - First Recurring Character](#google-coding-interview-question---first-recurring-character)
* [Daily Coding Problems](#daily-coding-problems)
  * [Problem 1: Any Two Numbers == K](#(7/19/18)-problem-1)
  * [Problem 2: Return New List with Product of List Except Ith Index](#(7/20/18)-problem-2)
  * [Problem 3: Serialize/Desiralize BST Node](#(7/23/18)-problem-3)
  * [Problem 4: Find Missing Integer](#(7/23/18)-problem-4)

## Amazon Coding Interview Question - Recursive Staircase Problem

This question asks you to find the number of ways you can go up a staircase given the size of the staircase and knowing you can only take one or two steps at a time like so.

![image](https://user-images.githubusercontent.com/9864281/42898075-1cf45ef4-8a90-11e8-864e-28d6df33c777.png)

The next part of the problem asks you how you would do it if you were given a set of steps that you could take. So for example given the set `X = {1,3,5}` that means you can only take 1 step, 3 steps, or 5 steps at a time. And then you have to figure out the number of ways to solve this problem.  

[source](https://www.youtube.com/watch?v=5o-kdjv7FD0)

[Return To Top](#go-to)

## Google Coding Interview Question - First Recurring Character

This question asks you to find the first repeating character given a string of characters like so:

```text
"ABCA" -> "A"
"HELLO" -> "L"
"COW" -> "NONE"
"DBCABA" -> "B"
```

![image](https://user-images.githubusercontent.com/9864281/42902848-ebccf972-8a9d-11e8-80b7-9b9a293a73a3.png)

[source](https://www.youtube.com/watch?v=GJdiM-muYqc)

[Return To Top](#go-to)

## Amazon Coding Interview Question - K Closest Points to the Origin

Given a list of tuples like `points_tuple = [(-2,4), (0,-2), (-1,0), (2,5), (-2,-3), (3,2), (1,0)]` find the k closest points to origin. So in this case, if `k=2` then the k closest points would be `(-1,0)` and `(0,-2)`

![image](https://user-images.githubusercontent.com/9864281/42920205-87265522-8ae3-11e8-933e-45b078b9b653.png)

![image](https://user-images.githubusercontent.com/9864281/42920362-3e2c3980-8ae4-11e8-9481-c51328fbd176.png)

[source](https://www.youtube.com/watch?v=eaYX0Ee0Kcg)

[Return To Top](#go-to)

## Daily Coding Problems

### (7/19/18) Problem 1

Given a list of numbers and a number k, return whether any two numbers from the list add up to k.

For example, given `[10, 15, 3, 7]` and `k of 17`, `return true` since 10 + 7 is 17.

**Bonus**: Can you do this in one pass?

[Return To Top](#go-to)

#### Problem 1 Solution

This problem can be solved in several different ways.

1. Brute force way would involve a nested iteration to check for every pair of numbers. This would take O(N^2).

2. use a set to remember the numbers we've seen so far. Then for a given number, we can check if there is another number that, if added, would sum to k. This would be O(N) since lookups of sets are O(1) each.

3. Yet another solution involves sorting the list. We can then iterate through the list and run a binary search on K - lst[i]. Since we run binary search on N elements, this would take O(N log N) with O(1) space.

[Return To Top](#go-to)

### (7/20/18) Problem 2

Given an array of integers, return a new array such that each element at index i of the new array is the product of all the numbers in the original array except the one at i.

For example, if our input was [1, 2, 3, 4, 5], the expected output would be [120, 60, 40, 30, 24]. If our input was [3, 2, 1], the expected output would be [2, 3, 6].

**Follow-up:** What if you can't use division?

[Return To Top](#go-to)

#### Problem 2 Solution

This problem would be easy with division: an optimal solution could just find the product of all numbers in the array and then divide by each of the numbers.

Without division, another approach would be to first see that the ith element simply needs the product of numbers before i and the product of numbers after i. Then we could multiply those two numbers to get our desired product.

In order to find the product of numbers before i, we can generate a list of prefix products. Specifically, the ith element in the list would be a product of all numbers including i. Similarly, we would generate the list of suffix products.

This runs in O(N) time and space, since iterating over the input arrays takes O(N) time and creating the prefix and suffix arrays take up O(N) space.

[Return To Top](#go-to)

### (7/23/18) Problem 3

Given the root to a binary tree, implement serialize(root), which serializes the tree into a string, and deserialize(s), which deserializes the string back into the tree.

For example, given the following Node class

```python
class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
```

The following test should pass:

```python
node = Node('root', Node('left', Node('left.left')), Node('right'))
assert deserialize(serialize(node)).left.left.val == 'left.left'
```

[Return To Top](#go-to)

#### Problem 3 Solution

There are many ways to serialize and deserialize a binary tree,
so don't worry if your solution differs from this one.
We will be only going through one possible solution.

We can approach this problem by first figuring out what we would
like the serialized tree to look like. Ideally, it would contain the
minimum information required to encode all the necessary information
about the binary tree. One possible encoding might be to borrow S-expressions from Lisp.
The tree `Node(1, Node(2), Node(3))` would then look like `'(1 (2 () ()) (3 () ()))'`,
where the empty brackets denote nulls.

To minimize data over the hypothetical wire, we could go a step further and prune out
some unnecessary brackets. We could also replace the 2-character `()` with `#`. We can then infer leaf nodes by their form
`val # #` and thus get the structure of the tree that way. Then our tree would look like `1 2 # # 3 # #`.

[Return To Top](#go-to)

### (7/23/18) Problem 4

Given an array of integers, find the first missing positive integer in linear time and constant space. In other words, find the lowest positive integer that does not exist in the array. The array can contain duplicates and negative numbers as well.

For example, the input `[3, 4, -1, 1]` should give `2`

The input `[1, 2, 0]` should give `3`.

You can modify the input array in-place.

[Return To Top](#go-to)

### Problem 4 Solution

The solution is way more complicated but doesn't use any extra space

Our lives would be easier without the linear time constraint: we would just sort the array
while filtering out negative numbers, and iterate over the sorted array and return the first
number that doesn't match the index. However, sorting takes `O(n log n)`, so we can't use that here.

Clearly we have to use some sort of trick here
to get it running in linear time. Since the first missing
positive number must be between `1 and len(array)` (why?), we
can ignore any negative numbers and `numbers bigger than len(array)`.
The basic idea is to use the indices of the array itself to reorder the
elements to where they should be. We traverse the array and swap
elements between 0 and the length of the array to their value's index.
We stay at each index until we find that index's value and keep on swapping.

By the end of this process, all the first positive numbers
should be grouped in order at the beginning of the array.
We don't care about the others. This only takes `O(N) time`
since we swap each element at most once.

Then we can iterate through the array and return the index of the first number that doesn't match, just like before.

Another way we can do this is by adding all the numbers to a set, and then use a counter initialized to 1
Then continuously increment the counter and check whether the value is in the set.

[Return To Top](#go-to)