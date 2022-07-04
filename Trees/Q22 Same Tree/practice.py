class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def isSameTree(self, p: TreeNode, q: TreeNode) -> bool:
        if not p and not q:
            return True
        if p and q and p.val == q.val:
            return self.isSameTree(p.right,q.right) and self.isSameTree(p.left, q.left)
        else:
            return False


# Different Solution

class Solution:
    def isSameTree(self, p:TreeNode, q: TreeNode):
        if not p and not q:
            return True

        if not p or not q or p.val != q.val:
            return False

        return (self.isSameTree(p.left, q.left) and self.isSameTree(p.right,q.right))
        