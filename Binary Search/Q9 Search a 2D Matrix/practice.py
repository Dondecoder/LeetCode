# class Solution:
#     def searchMatrix(self, matrix: list[list[int]], target: int) -> bool:
#         ROWS, COLS = len(matrix), len(matrix[0])
        
#         top, bot = 0, ROWS - 1
#         while top <= bot:
#             row = (top + bot) // 2
#             if target > matrix[row][-1]:
#                 top = row + 1
#             elif target < matrix[row][0]:
#                 bot = row - 1
#             else:
#                 break
        
#         if not (top <= bot):
#             return False
#         row = (top + bot) // 2
#         l, r = 0, COLS - 1
#         while l <= r:
#             m = (l + r) // 2
#             if target > matrix[row][m]:
#                 l = m + 1
#             elif target < matrix[row][m]:
#                 r = m - 1
#             else:
#                 return True
#         return False

class Solution:
    def searchMatrix(self, matrix: list[list[int]], target: int) -> bool:
        col, rows = len(matrix), len(matrix[0])
        
        top, bottom = 0, col -1
        while top <= bottom:
            middle_row = (top + bottom) // 2
            if matrix[middle_row][0] > target:
                bottom = middle_row -1
            elif matrix[middle_row][-1] < target:
                top = middle_row + 1
            else:
                break
        
        if top >= bottom:
            return False
        
        middle_row = (top + bottom) // 2
        start, end = 0, rows -1
        while start <= end:
            middle_idx = (start + end) // 2
            if matrix[middle_row][middle_idx] < target:
                start = middle_idx + 1
            elif matrix[middle_row][middle_idx] > target:
                end = middle_idx - 1
            else:
                return True
        return False

find = Solution()
find.searchMatrix([[1,3,5,7],[10,11,16,20],[23,30,34,60]], 3)