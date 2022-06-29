# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# class Solution:
#     def BalancedTree(self, head:TreeNode):

#         def dfshelper(head):
#             if head is None:
#                 return [True, 0]
#             left = dfshelper(head.left)
#             right = dfshelper(head.right)

            
class Solution:
    def search(self, nums: list[int], target: int) -> int:
        return self.bfshelper(nums,target,start=0,end=(len(nums))- 1)
    
        
    def bfshelper(self, nums, target, start, end):
        start = 0
        end = (len(nums)) - 1
        while start < end:
            mid = (start + end) // 2
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                start = mid + 1
            elif nums[mid] > target:
                end = mid - 1
        return -1


bs = Solution()
bs.search([-1,0,3,5,9,12], 9)