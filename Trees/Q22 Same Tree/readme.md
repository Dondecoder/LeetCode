# Name

100 Same Tree

## Problem

* Given the roots of two binary trees p and q, write a function to check if they are the same or not.

Two binary trees are considered the same if they are structurally identical, and the nodes have the same value.

## New Topics


## Solution Explanation

* To understand and solve this problem you need to understand tree traversals typically to traverse a tree you will prob use recursion and DFS. In this problem the traversals traverses the tree until it hits either the root of the first tree and the root of the second tree is None. Important to note that each one of the trees have to have a None value in order for the first case to evaluate as True. Next you check if the first tree values equal each other than you run recursion on the right side of tree 1 and tree 2 and then run recurssion on the left side of tree 1 and tree 2. It will return a boolean value of True if it is True. Else it will return False. 

```python
# Time: O(n)
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if p is None and q is None:
            return True
        if p and q and p.val == q.val:
            return self.isSameTree(p.right,q.right) and self.isSameTree(p.left, q.left)
        else:
            return False
```