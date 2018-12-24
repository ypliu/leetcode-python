class Solution(object):
    def maximalSquare(self, matrix):
        """
        :type matrix: List[List[str]]
        :rtype: int
        """

        if (not matrix) or (len(matrix) < 1) or (len(matrix[0]) < 1):
            return 0
        dp_table = [0 for _ in range(len(matrix[0])+1)]
        max_square_len = 0; prev = 0
        for i in range(1, len(matrix)+1):
            for j in range(1, len(matrix[0])+1):
                temp = dp_table[j]
                if ('1' == matrix[i - 1][j - 1]):
                    dp_table[j] = min(dp_table[j-1], prev, dp_table[j]) + 1
                    max_square_len = max(max_square_len, dp_table[j])
                else:
                    dp_table[j] = 0
                prev = temp
        return (max_square_len * max_square_len)

# debug
s = Solution()
print s.maximalSquare([ ['1','0','1','0','0'], ['1','0','1','1','1'], ['1','1','1','1','1'], ['1','0','0','1','0'] ])
print s.maximalSquare([ ['0','1','1','1','0'], ['1','1','1','1','1'], ['1','1','1','1','1'], ['0','1','1','1','1'], ['0','0','1','1','1'] ])
