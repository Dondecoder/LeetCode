# Name

110 Balanced Binary Tree

## Problem

* Given a binary tree, determine if it is height-balanced.

For this problem, a height-balanced binary tree is defined as:

a binary tree in which the left and right subtrees of every node differ in height by no more than 1.

## New Topics


## Solution Explanation

* To understand and solve this problem you need to understand tree traversals typically to traverse a tree you will prob use recursion and DFS. In this problem the traversals traverses the tree until it hits a value of none or the base case. In this case once it hits the base case it will return [True, 0].The reason this is done is because you want to track the height of the tree along with a boolean value because that needs to be returned to solve this problem. You can use a dfs function to recursively call left and right side. Then you create a variable that returns a boolean value if a condition is met. Then you return the boolean value in a list and return 1 + max(left[1], right[1]). Finally you return dfs(root)[0] because root[0] has the boolean value. 

```python
# Time: O(n)
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isBalanced(self,root:TreeNode):
        def dfs(root):
            if root is None:
                return [True, 0]
            
            left,right = dfs(root.left), dfs(root.right)

            balanced = left[0] and right[0] and abs(left[1] - right[1]) <= 1

            return [balanced, 1 + max(left[1], right[1])]
        
        return dfs(root)[1]
```