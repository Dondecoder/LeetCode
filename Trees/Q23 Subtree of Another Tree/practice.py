class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isSubtree(self, s: TreeNode, t: TreeNode) -> bool:
        if not t: return True
        if not s: return False
        
        if self.sameTree(s, t):
            return True
        return (self.isSubtree(s.left, t) or
                self.isSubtree(s.right, t))
    
    def sameTree(self, s, t):
        if not s and not t:
            return True
        if s and t and s.val == t.val:
            return (self.sameTree(s.left, t.left) and
                    self.sameTree(s.right, t.right))
        return False



tree_1 = TreeNode(3)
tree_1.left = TreeNode(4)
tree_1.left.left = TreeNode(1)
tree_1.left.right = TreeNode(2)
tree_1.right = TreeNode(5)
tree_2 = TreeNode(4)
tree_2.left = TreeNode(1)
tree_2.right = TreeNode(2)

Subtree = Solution()
Subtree.isSubtree(s=tree_1, t=tree_2)