# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

#DFS
class Solution:
    def diameterOfBinaryTree(self, root: TreeNode) -> int:
        res = 0
        
        def dfs(root):
            nonlocal res
            if not root:
                return 0
            left = dfs(root.left)
            right = dfs(root.right)
            res = max(res, left + right)
            
            return 1 + max(left, right)
        
        dfs(root)
        return res

class Solution2:
    def diameterOfBinaryTree(self, root: TreeNode) -> int:
        
        def dfs(root): 
            nonlocal diameter
            if root is None: 
                return 0
            left = dfs(root.left)
            right = dfs(root.right)
            
            diameter = max(left + right, diameter)
            
            return max(left, right) + 1
            
                    
        diameter = 0
        dfs(root)
        return diameter


Bin_tree = TreeNode(3)
Bin_tree.left = TreeNode(4)
Bin_tree.right = TreeNode(5)
Bin_tree.right.right = TreeNode(6)
Bin_tree.right.left = TreeNode(7)
Bin_tree.left.right = TreeNode(8)
Bin_tree.left.left = TreeNode(9)
Bin_tree.left.left.left = TreeNode(10)
Bin_tree.left.left.left.left = TreeNode(12)
Bin_tree.right.right.left = TreeNode(15)
Bin_tree.right.right.left.right = TreeNode(20)
Node_height = Solution()
Node_height.diameterOfBinaryTree(Bin_tree)