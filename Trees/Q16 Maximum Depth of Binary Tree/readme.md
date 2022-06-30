# Name

104 Maximum Depth of Binary Tree

## Problem

* Given the root of a binary tree, return its maximum depth.

A binary tree's maximum depth is the number of nodes along the longest path from the root node down to the farthest leaf node.

## New Topics


## Solution Explanation

* To understand and solve this problem you need to understand tree traversals typically to traverse a tree you will prob use recursion and DFS. In this problem the traversals traverses the tree until it hits a value of none or the base case. From there it backtracks and performs an operation on each node. So the recursion traverses the tree until it hits the bottom node on either the left or the right side. When it hits the bottom node on the left side it backtracks upwards and checks if the value has a right elem if it does it checks that elem for a left and right node. If the values are null it returns 0 and and returns the value of the elem as max(dfs(root.left),dfs(root.right)) + 1. This pretty much solves the problem recursively.  

```python
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        if not root:
            return 0
        
        return 1 + max(self.maxDepth(root.left), self.maxDepth(root.right))
```