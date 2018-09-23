class Solution(object):
    def generateMatrix(self, n):
        """
        :type n: int
        :rtype: List[List[int]]
        """

        if not n or 0 == n:
            return []
        elif 1 == n:
            return [[1]]

        res = [[0 for i in xrange(n)] for j in xrange(n)]
        layer_th, row_last = 0, n-1
        num = 1
        while layer_th <= row_last:
            for i in xrange(layer_th, row_last+1):
                res[layer_th][i] = num
                num += 1
            for i in xrange(layer_th+1, row_last+1):
                res[i][row_last] = num
                num += 1
            for i in xrange(row_last-1, layer_th, -1):
                res[row_last][i] = num
                num += 1
            for i in xrange(row_last, layer_th, -1):
                res[i][layer_th] = num
                num += 1
            layer_th += 1
            row_last -= 1
        return res

# debug
s = Solution()
print s.generateMatrix(2)
print s.generateMatrix(3)
print s.generateMatrix(6)
