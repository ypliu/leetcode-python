class Solution(object):
    def rotate(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: void Do not return anything, modify matrix in-place instead.
        """

        dim_matrix = len(matrix)
        up_row, down_row = 0, dim_matrix-1
        while up_row < down_row:
            i, corr = up_row, dim_matrix - 1 - up_row
            while i < down_row:
                # print up_row,i, '<=', corr, up_row, '<=', down_row, corr, '<=', i, down_row
                val = matrix[up_row][i]
                matrix[up_row][i] = matrix[corr][up_row]
                matrix[corr][up_row] = matrix[down_row][corr]
                matrix[down_row][corr] = matrix[i][down_row]
                matrix[i][down_row] = val
                i += 1
                corr -= 1
            up_row += 1
            down_row -= 1

# debug
s = Solution()

matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
#print matrix
s.rotate(matrix)
print matrix

matrix = [[ 5, 1, 9,11], [ 2, 4, 8,10], [13, 3, 6, 7], [15,14,12,16]]
#print matrix
s.rotate(matrix)
print matrix
