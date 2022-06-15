# Name

74 Search a 2D Matrix

## Problem

* Write an efficient algorithm that searches for a value target in an m x n integer matrix matrix. This matrix has the following properties:

Integers in each row are sorted from left to right.
The first integer of each row is greater than the last integer of the previous row.


## Solution Explanation

* To understand and solve this problem you need to first understand how to use binary search in this case to solve this problem you have to find the length of the matrix and the length of the matrix and the length of one of the rows in the matrix. After finding that you perform a binary search. You divide the matrix in half and find the middle. You find the middle row by assigning a variable to equal 0 and a variable to equal the length of the matrix -1. Then when you find the middle row you compare the target to the first and last element of that row. If the target is greater then the last element you move to the row in the bottom of the matrix. If the target is less than the first element you move to the row on the top of the matrix. As long as the target is less than first element in middle row you move to the first row then break. If the top row index is not less than or equal to the bottom row index return False. Finally you run a binary search on the row corresponding with the target and use a while loop to locate the target.


```python
class Solution:
    def searchMatrix(self, matrix: list[list[int]], target: int) -> bool:
        ROWS, COLS = len(matrix), len(matrix[0])
        
        top, bot = 0, ROWS - 1
        while top <= bot:
            row = (top + bot) // 2
            if target > matrix[row][-1]:
                top = row + 1
            elif target < matrix[row][0]:
                bot = row - 1
            else:
                break
        
        if not (top <= bot):
            return False
        row = (top + bot) // 2
        l, r = 0, COLS - 1
        while l <= r:
            m = (l + r) // 2
            if target > matrix[row][m]:
                l = m + 1
            elif target < matrix[row][m]:
                r = m - 1
            else:
                return True
        return False

``` 