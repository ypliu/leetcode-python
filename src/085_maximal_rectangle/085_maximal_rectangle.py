class Solution(object):
    def maximalRectangle(self, matrix):
        """
        :type matrix: List[List[str]]
        :rtype: int
        """

        if not matrix or 0 == len(matrix) or 0 == len(matrix[0]):
            return 0

        num_cols = len(matrix[0])
        heights = [0 for j in range(num_cols+1)]
        res = 0
        for mat_row in matrix:
            for j in xrange(num_cols):
                if '1' == mat_row[j]:
                    heights[j] += 1
                elif '0' == mat_row[j]:
                    heights[j] = 0
                else:
                    print "Error! Illegal value"
                    return 0
            stack = [-1]
            for j in xrange(num_cols+1):
                while heights[j] < heights[stack[-1]]:
                    h = heights[stack.pop()]
                    w = j - stack[-1] - 1
                    res = max(res, h*w)
                stack.append(j)
        return res

# debug
s = Solution()
print s.maximalRectangle([ ["1","0","1","0","0"], ["1","0","1","1","1"], ["1","1","1","1","1"], ["1","0","0","1","0"] ])
