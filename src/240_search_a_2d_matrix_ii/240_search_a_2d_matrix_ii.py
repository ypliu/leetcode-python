class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """

        if (not matrix):
            return False
        n_r,n_c = len(matrix),len(matrix[0])
        r_bl,c_bl = n_r-1,0
        # time: O(m+n)
        while (r_bl >= 0) and (c_bl < n_c):
            if (target < matrix[0][c_bl]) or (target > matrix[r_bl][-1]):
                return False
            v_bl = matrix[r_bl][c_bl]
            if (target < v_bl):
                r_bl -= 1
            elif (target > v_bl):
                c_bl += 1
            else:
                return True
        return False

# debug
s = Solution()
matrix = [ [1,4,7,11,15], [2,5,8,12,19], [3,6,9,16,22], [10,13,14,17,24],[18,21,23,26,30] ]
print s.searchMatrix(matrix, 5)
print s.searchMatrix(matrix, 20)
