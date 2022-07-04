class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def BalancedTree(self, head:TreeNode):

        def dfshelper(head):
            if head is None:
                return [True, 0]
            left = dfshelper(head.left)
            right = dfshelper(head.right)
            balanced = left[0] and right[0] and abs(left[1] - right[1]) <= 1

            return [balanced, 1 + max(left[1], right[1])]

        return dfshelper(head)[0]

            
Bin_tree = TreeNode(3)
Bin_tree.left = TreeNode(9)
Bin_tree.right = TreeNode(20)
Bin_tree.right.left = TreeNode(15)
Bin_tree.right.right = TreeNode(7)

B_tree = Solution()
B_tree.BalancedTree(Bin_tree)