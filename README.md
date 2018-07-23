# Practice-Interview-Questions

Just a bunch of practice interview questions that i'll work on.

## Amazon Coding Interview Question - Recursive Staircase Problem

This question asks you to find the number of ways you can go up a staircase given the size of the staircase and knowing you can only take one or two steps at a time like so.

![image](https://user-images.githubusercontent.com/9864281/42898075-1cf45ef4-8a90-11e8-864e-28d6df33c777.png)

The next part of the problem asks you how you would do it if you were given a set of steps that you could take. So for example given the set `X = {1,3,5}` that means you can only take 1 step, 3 steps, or 5 steps at a time. And then you have to figure out the number of ways to solve this problem.  

[source](https://www.youtube.com/watch?v=5o-kdjv7FD0)

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

## Amazon Coding Interview Question - K Closest Points to the Origin

Given a list of tuples like `points_tuple = [(-2,4), (0,-2), (-1,0), (2,5), (-2,-3), (3,2), (1,0)]` find the k closest points to origin. So in this case, if `k=2` then the k closest points would be `(-1,0)` and `(0,-2)`

![image](https://user-images.githubusercontent.com/9864281/42920205-87265522-8ae3-11e8-933e-45b078b9b653.png)

![image](https://user-images.githubusercontent.com/9864281/42920362-3e2c3980-8ae4-11e8-9481-c51328fbd176.png)

[source](https://www.youtube.com/watch?v=eaYX0Ee0Kcg)

## Daily Coding Problems

### (7/19/18) Problem 1

Given a list of numbers and a number k, return whether any two numbers from the list add up to k.

For example, given `[10, 15, 3, 7]` and `k of 17`, `return true` since 10 + 7 is 17.

**Bonus**: Can you do this in one pass?

#### Solution

This problem can be solved in several different ways.

1. Brute force way would involve a nested iteration to check for every pair of numbers. This would take O(N^2).

2. use a set to remember the numbers we've seen so far. Then for a given number, we can check if there is another number that, if added, would sum to k. This would be O(N) since lookups of sets are O(1) each.

3. Yet another solution involves sorting the list. We can then iterate through the list and run a binary search on K - lst[i]. Since we run binary search on N elements, this would take O(N log N) with O(1) space.

### (7/20/18) Problem 2

Given an array of integers, return a new array such that each element at index i of the new array is the product of all the numbers in the original array except the one at i.

For example, if our input was [1, 2, 3, 4, 5], the expected output would be [120, 60, 40, 30, 24]. If our input was [3, 2, 1], the expected output would be [2, 3, 6].

**Follow-up:** What if you can't use division?

#### Solution

This problem would be easy with division: an optimal solution could just find the product of all numbers in the array and then divide by each of the numbers.

Without division, another approach would be to first see that the ith element simply needs the product of numbers before i and the product of numbers after i. Then we could multiply those two numbers to get our desired product.

In order to find the product of numbers before i, we can generate a list of prefix products. Specifically, the ith element in the list would be a product of all numbers including i. Similarly, we would generate the list of suffix products.

This runs in O(N) time and space, since iterating over the input arrays takes O(N) time and creating the prefix and suffix arrays take up O(N) space.

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

#### Solution


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

