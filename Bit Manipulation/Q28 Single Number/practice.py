class Solution:
    def singleNumber(self, nums: list[int]) -> int:
        res = 0
        for n in nums:
            res = n ^ res
        return res


number_single = Solution()
number_single.singleNumber([2,4,1,2])
