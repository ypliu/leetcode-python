class Solution(object):
    def setZeroes(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: void Do not return anything, modify matrix in-place instead.
        """

        if not matrix or 0 == len(matrix):
            return
        elif 0 == len(matrix[0]):
            return

        tag_row = tag_col = -1
        m, n = len(matrix), len(matrix[0])
        for i in xrange(m):
            for j in xrange(n):
                if 0 == matrix[i][j]:
                    if -1 == tag_row:
                        tag_row = i; tag_col = j
                    else:
                        matrix[i][tag_col] = 0; matrix[tag_row][j] = 0

        if -1 == tag_row:
            return
        for i in xrange(m):
            if i == tag_row:
                continue
            for j in xrange(n-1, tag_col, -1):
                if 0 == matrix[tag_row][j] or 0 == matrix[i][tag_col]:
                    matrix[i][j] = 0
            for j in xrange(tag_col):
                if 0 == matrix[tag_row][j] or 0 == matrix[i][tag_col]:
                    matrix[i][j] = 0
            matrix[i][tag_col] = 0
        for j in xrange(n):
            matrix[tag_row][j] = 0

# debug
s = Solution()
matrix = [ [1,1,1], [1,0,1], [1,1,1] ]
s.setZeroes(matrix)
print matrix
matrix = [ [0,1,2,0], [3,4,5,2], [1,3,1,5] ]
s.setZeroes(matrix)
print matrix
