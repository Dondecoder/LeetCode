from collections import deque

class Solution:
    def numIslands(self, grid: list[list[str]]) -> int:
        if not grid or not grid[0]:
            return 0
        
        islands = 0
        visit = set()
        rows, cols = len(grid), len(grid[0])
        
        def dfs(r, c):
            if (r not in range(rows) or
                c not in range(cols) or
                grid[r][c] == "0" or
                (r, c) in visit):
                return
            
            visit.add((r, c))
            directions = [[0, 1], [0, -1], [1, 0], [-1, 0]]
            for dr, dc in directions:
                dfs(r + dr, c + dc)
        
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == "1" and (r, c) not in visit:
                    islands += 1
                    dfs(r, c)
        return islands


# Alternative Solution
class Solution:
    def numIslands(self, grid: list[list[str]]) -> int:
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


class Solution3:
    def numIslands(self, grid: list[list[str]]) -> int:
        
        islands = 0
        rows,cols = len(grid), len(grid[0])
        
        def dfs(r,c,grid):
            grid[r][c] = "0"
            visited =[(r+1, c), (r-1, c), (r, c+1), (r, c-1)]
            for row,col in visited:
                if row >= 0 and col >= 0 and row <= (rows - 1) and col <= (cols - 1) and grid[row][col] == "1":
                    dfs(row,col,grid)
              
                    
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == "1":
                    dfs(r,c,grid)
                    islands +=1
        return islands


island_form = Solution3()
island_form.numIslands([["1","1","1","1","0"],["1","1","0","1","0"],["1","1","0","0","0"],["0","0","0","0","0"]])