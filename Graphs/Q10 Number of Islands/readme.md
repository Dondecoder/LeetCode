# Name

200 Number of Islands 

## Problem

* Given an m x n 2D binary grid grid which represents a map of '1's (land) and '0's (water), return the number of islands.

An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically. You may assume all four edges of the grid are all surrounded by water.

## Solution Explanation

* To understand and solve this problem you need to understand how to search a 2D grid or matrix. Typically you need to find the length of the grid and the length of the rows. You need to use dfs to solve this and if you are checking for islands you need to make sure that your for loop stops when you encounter a "1". Once that happens turn the value of the "1" to a "0" to mark as viewed, use a dfs helper function to search to the left,right,bottom and top of the grid to find any other adjacent "1"'s. In order for you to successfully run the loop the row and col has to be greater than 0 and the row and the col has to be less than the length of the rows and the columns and the grid[r][c] == "1". If that all checks out then make a recursive call to the dfs function to run the dfs function on the location of the "new" 1 that was discovered. Keep this going until you pop out dfs functions and then islands will be += 1. Then you iterate through each index of column and rows until the function returns number of islands. 


```python
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        islands = 0
        rows,columns = len(grid), len(grid[0])
        
        
        def dfs(grid,r,c):
            grid[r][c] = "0"
            chk_list = [(r+1,c), (r-1, c), (r,c+1), (r,c-1)]
            for row, col in chk_list:
                if row >= 0 and col >=0 and row < rows and col < columns and grid[row][col] == "1":
                    dfs(grid,row,col)
        
        for r in range(rows):
            for c in range(columns):
                if grid[r][c] == "1":
                    dfs(grid,r,c)
                    islands +=1
        return islands
```