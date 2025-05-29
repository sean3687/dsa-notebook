class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # sorted , matrix
        # looking for target  = 10 
        # brute force n^2

        # m = rows
        # n = column
        i = 0
        j = len(matrix) -1
        row = -1

        # selecting the correct range
        while i < j:
            middle = (i+j)//2
            
            # under range
            if matrix[middle][0] <= target <= matrix[middle][-1]:
                row = middle
            elif target < matrix[middle][0]:
                i = middle -1
            else:
                j = middle +1

        if middle == -1:
            return False
        l = 0
        r = len(middle) -1
            # binary search
            # 10 11 12 13 target = 12
        while l < r:
            m = (l+r)//2
            if target == matrix[middle][m]:
                return True
            elif target > matrix[middle][m]:
                l = m +1
            else:
                r = m -1
        
        return False

# from typing import List

# class Solution:
#     def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
#         if not matrix or not matrix[0]:
#             return False

#         i = 0
#         j = len(matrix) - 1
#         row = -1

#         # Binary search to find the correct row
#         while i <= j:
#             middle = (i + j) // 2
#             if matrix[middle][0] <= target <= matrix[middle][-1]:
#                 row = middle
#                 break
#             elif target < matrix[middle][0]:
#                 j = middle - 1
#             else:
#                 i = middle + 1

#         if row == -1:
#             return False

#         # Binary search within the row
#         l = 0
#         r = len(matrix[row]) - 1
#         while l <= r:
#             m = (l + r) // 2
#             if matrix[row][m] == target:
#                 return True
#             elif matrix[row][m] < target:
#                 l = m + 1
#             else:
#                 r = m - 1

#         return False

