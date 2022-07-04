# Name

235 Lowest Common Ancestor of a Binary Search Tree

## Problem

* Given a binary search tree (BST), find the lowest common ancestor (LCA) of two given nodes in the BST.

According to the definition of LCA on Wikipedia: “The lowest common ancestor is defined between two nodes p and q as the lowest node in T that has both p and q as descendants (where we allow a node to be a descendant of itself).”

## New Topics


## Solution Explanation

* We solve this problem iteratively and we compare the value of p and the value of q to the value of the root. As long as their is a root node we iterate. Because it a BST the left side is less than the root and the right side is greater than the root. So we compare if the values of p and q are less than the root or greater. If less we move to root.left if greater we move to root.right. If in both cases the p and q are not either less than or greater than the root we just return the root node. 

```python
# Time: O(n)
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
               return root
```