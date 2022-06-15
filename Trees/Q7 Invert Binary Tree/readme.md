# Name

226 Invert Binary Tree

## Problem

* Given the root of a binary tree, invert the tree and return its root


## Solution Explanation

* To understand and solve this problem you need to understand tree traversals typically to traverse a tree you will prob use recursion and DFS. In this problem the traversals traverses the tree until it hits a value of none or the base case. From there it backtracks and performs an operation on each node. So the recursion traverses the tree until it hits the bottom node on either the left or the right side. From there it backtracks up and switch every node from left to right. 

```python
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def invertTree(self, root: TreeNode) -> TreeNode:
        # this is the base case
        if not root:
            return None
        # if root is none then exit the traversal and backtrack
        
        # swap the children
        tmp = root.left
        # this saves the value of root.left in a variable
        root.left = root.right
        # then you switch root.left = root.right
        root.right = tmp
        # then you make root.right = temp_node

        # alternatively you could use
        # root.right, root.left = root.left, root.right
        
        self.invertTree(root.left)
        # recursively call the function for the left side of the function
        self.invertTree(root.right)
        # recursively call the function for the right side of the function
        return root
        # return root
```