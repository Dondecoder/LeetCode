# Name

1 Two Sum

## Problem

* Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

You can return the answer in any order.


## Solution Explanation

* To understand and solve this problem you can use different solutions. The slower solution involves the brute force method which requires two for loops to run through the array of numbers and compare each value pair in the array to see if it equals the target. If it does then it will return the index of it. The next more optimal method is using a hashmap that will take in as it key the value of the element in the array and as it's value it will take in the index of the integer in the array. For this you will only need to iterate through the array once and use the enumerate function to keep track of the index and values in the array. You will also need to keep track of the difference which is the target - integer value. You would check to see if the difference is not in the hashtable; if not append the integer value as the key and the index as the value. If the difference is in the hashmap then we just return the index of the hashmap[difference] and i in a list. 

```python
# Time: O(n^2) | Space: O(1)
class Solution1:
    def TwoSum(self, nums: list([int]), target: int):
        for i in range(len(nums) - 1):
            for j in range(i +1, len(nums)):
                if nums[i] + nums[j] == target:
                    return [i,j]


# Time: O(n) | Space: O(n)
class Solution2:
    def TwoSum(self, nums: list([int]), target: int):
        prev = {}
        for i, n in enumerate(nums):
            difference = target - n
            if difference not in prev:
                prev[n] = i
            else:
                return [prev[difference], i]

```