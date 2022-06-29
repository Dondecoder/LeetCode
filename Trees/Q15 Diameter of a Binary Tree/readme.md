# Name

226 Invert Binary Tree

## Problem

* Given the root of a binary tree, invert the tree and return its root

## New Topics

* nonlocal 


## Solution Explanation

* To understand and solve this problem you need to understand tree traversals typically to traverse a tree you will prob use recursion and DFS. In this problem the traversals traverses the tree until it hits a value of none or the base case. From there it backtracks and performs an operation on each node. So the recursion traverses the tree until it hits the bottom node on either the left or the right side. When it hits the bottom node on the left side it backtracks upwards and checks if the value has a right elem if it does it checks that elem for a left and right node. If the values are null it returns 0 and and returns the value of the elem as max(left,right) + 1. We also update diameter. Diamater is the sum of the left and the right so if the sum of the left and right are greater than the current value in diameter than we update the diameter. All in all we return diameter after everything. 

```python
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

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
```