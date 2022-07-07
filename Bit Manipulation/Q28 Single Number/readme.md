# Name

136 Single Number

## Problem

* Given a non-empty array of integers nums, every element appears twice except for one. Find that single one.

You must implement a solution with a linear runtime complexity and use only constant extra space.

## Solution

* To understand this problem you need to understand binary numbers and how every number can be converted to binary numbers. This function uses xor (^) operator to solve. It updates the res variable that equals 0 to update based on the binary form of n in the nums list. Finally after it iterates through all the numbers it returns the final value for res which is the single number that appears in the list.

```python
class Solution:
    def singleNumber(self, nums: list[int]) -> int:
        res = 0
        for n in nums:
            res = n ^ res
        return res
```