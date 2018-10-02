class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """

        if not matrix or 0 == len(matrix) or 0 == len(matrix[0]):
            return False
        elif matrix[0][0] > target or matrix[-1][-1] < target:
            return False

        num_row, num_col = len(matrix), len(matrix[0])        
        low = 0; high = num_row * num_col - 1
        while low <= high:
            mid = (low + high) >> 1
            val = matrix[mid // num_col][mid % num_col]
            if val > target:
                high = mid - 1
            elif val < target:
                low = mid + 1
            else:
                return True
        return False

# debug
s = Solution()
print s.searchMatrix([ [1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 50] ], 3)
print s.searchMatrix([ [1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 50] ], 13)
