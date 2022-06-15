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