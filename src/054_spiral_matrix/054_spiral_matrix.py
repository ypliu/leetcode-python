class Solution(object):
    def spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """

        if not matrix or 0 == len(matrix):
            return []
        elif 1 == len(matrix):
            return matrix[0]

        res = []
        row_last = len(matrix) - 1
        col_last = len(matrix[0]) - 1
        layer_th = 0
        while layer_th <= row_last and layer_th <= col_last:
            for i in xrange(layer_th, col_last+1): # top border, to right
                # until the right-most. Otherwise, it is possible that it will omit only 1 num in this last layer
                res.append(matrix[layer_th][i])
            if layer_th == row_last: # prevent duplicate access nums in 1st for-loop, targeting the 3rd for-loop (bottom border)
                break
            for i in xrange(layer_th+1, row_last+1): # right border, downward
                res.append(matrix[i][col_last])
            if layer_th == col_last: # prevent duplicate access nums in 2nd for-loop, targeting the 4th for-loop (left border)
                break
            for i in xrange(col_last-1, layer_th, -1): # bottom border, to left
                res.append(matrix[row_last][i])
            for i in xrange(row_last, layer_th, -1): # left border, upward
                res.append(matrix[i][layer_th])
            layer_th += 1
            row_last -= 1
            col_last -= 1

        return res

# debug
s = Solution()
print s.spiralOrder([ [1, 2, 3], [4, 5, 6], [7, 8, 9] ])
print s.spiralOrder([ [1, 2, 3, 4, 5], [6, 7, 8, 9, 10], [11, 12, 13, 14, 15] ])
print s.spiralOrder([ [3], [2] ])
