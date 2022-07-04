# Name

572 Subtree of Another Tree

## Problem

* Given the roots of two binary trees root and subRoot, return true if there is a subtree of root with the same structure and node values of subRoot and false otherwise.

A subtree of a binary tree tree is a tree that consists of a node in tree and all of this node's descendants. The tree tree could also be considered as a subtree of itself.

## New Topics


## Solution Explanation

* For this problem you use recursion to solve you use a helper function to check if the trees are the same. If they are it will return True. You use a next recursive function to move to the left and right side of the tree if the tree is not the same. Two recurssive calls one two traverse the tree and one to compare if the trees are the same. 

```python
# Time: O(n)
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