class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        for i in range(len(nums)):
            for j in range(i +1, len(nums)):
                if nums[i] + nums[j] == target:
                    return i,j


class Solution2:
    def twoSum(self, nums:list, target:int):
        prev = {}
        for i,n in enumerate(nums):
            difference = target - n
            if difference not in prev:
                prev[n] = i 
            else:
                return [prev[difference], i]
