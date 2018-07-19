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

### Problem 1(7/19/18)

Given a list of numbers and a number k, return whether any two numbers from the list add up to k.

For example, given `[10, 15, 3, 7]` and `k of 17`, `return true` since 10 + 7 is 17.

**Bonus**: Can you do this in one pass?