class Solution:
    def maxSubArray(self, nums: list[int]) -> int:
        res = nums[0]
        
        total = 0
        for n in nums:
            total += n
            res = max(res, total)
            if total < 0:
                total = 0
        return res


subarray = Solution()
subarray.maxSubArray([-2,1,-3,4,-1,2,1,-5,4])