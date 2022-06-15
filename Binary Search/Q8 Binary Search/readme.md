# Name

704 Binary Search

## Problem

* Given an array of integers nums which is sorted in ascending order, and an integer target, write a function to search target in nums. If target exists, then return its index. Otherwise, return -1.

You must write an algorithm with O(log n) runtime complexity.

 Example 1:

Input: nums = [-1,0,3,5,9,12], target = 9
Output: 4
Explanation: 9 exists in nums and its index is 4
Example 2:

Input: nums = [-1,0,3,5,9,12], target = 2
Output: -1
Explanation: 2 does not exist in nums so return -1


## Solution Explanation

* In order to solve this problem you need to understand binary search. In a sorted array you need to search for a number. You first have to divide the array in half and if the target is greater than the middle number move to the right. Alternatively if the number is less than the middle number move to the left. You continue dividing the array in half until you reach the target number and then that is how you solve the problem. 


```python
class Solution:
    def search(self, nums: list[int], target: int) -> int:
        return searchhelper(nums,target, start = 0, end = len(nums) - 1)
    
def searchhelper(nums, target, start, end):
    while start <= end:
        mid = (start + end) // 2
        if nums[mid] == target:
            return mid
        elif nums[mid] < target:
            start = mid + 1
        elif nums[mid] > target:
            end = mid -1
    return -1

```