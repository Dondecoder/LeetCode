# Name

70 Climbing Stairs

## Problem

* You are climbing a staircase. It takes n steps to reach the top.

Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?

## Solution

* To understand this problem you need to know when to use dynamic programing. In this case we use dynamic programming to solve this problem. First do some charting to find out how many combination it takes to get to the top for n values that you do not know. record the values. See if you find any similarities between previous values and your current values. In this case this problem was the fibonnaci sequence. The two previous numbers added up equal the value of the current number. So dynamically this can be solved by creating some type of base case for what we know for example. Anything <= 3  will return the same number of combinations. So you iterate from 4 because the value changes and you iterate through the range of n +1. Use a variable to record the value of the 2 previous numbers which in this case was 2 and 3 then updated n1 = n2 and n2 to equal values of previous numbers added. After the loop simply return n2. 

```python
class Solution:
    def lclimbingStairs(self, n: int):
        if n <= 3:
            return n

        n1,n2 = 2,3

        for i in range(4, n+1):
            prev_val = n1 + n2
            n1 = n2
            n2 = prev_val
        return n2        
```