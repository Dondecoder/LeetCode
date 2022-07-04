class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        while root:
            if p.val > root.val and q.val > root.val:
                root = root.right
            elif p.val < root.val and q.val < root.val:
                root = root.left
            else:
               return print(root)


BST = TreeNode(6)
BST.left = TreeNode(2)
BST.right = TreeNode(8)
BST.left.left = TreeNode(0)
BST.left.right = TreeNode(4)
BST.right.right = TreeNode(9)
BST.right.left = TreeNode(7)
BST.left.right.left = TreeNode(3)
BST.left.right.right = TreeNode(5)

common_tree = Solution()
common_tree.lowestCommonAncestor(BST, TreeNode(0), TreeNode(4))