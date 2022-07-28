# Name

53 Maximum Subarray

## Problem

* Given an integer array nums, find the contiguous subarray (containing at least one number) which has the largest sum and return its sum.

A subarray is a contiguous part of an array.

## New Topics

Max Subarray


## Solution Explanation

* To understand and solve this problem you pretty much use a sliding window and a count function that calculates the max of the addition of each integer in the array and updates the count if the addition of the count and the new integer in the array is higher than the current count. It uses the max function and to update the value. 

```python
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        max_val = nums[0]
        total = 0
        for n in nums:
            total += n
            max_val = max(max_val, total)
            if total < 0:
                total = 0
        return max_val            
```