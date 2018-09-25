class Solution(object):
    def minPathSum(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """

        if not grid or 0 == len(grid) or 0 == len(grid[0]):
            return -1

        m, n = len(grid), len(grid[0])
        res = [grid[m-1][j] for j in xrange(n)]
        for j in xrange(n-2, -1, -1):
            if grid[m-1][j] >= 0:
                res[j] += res[j+1]
            else:
                print 'Ilegal value: %d at (%d, %d).' %(grid[m-1][j], (m-1), j)
                return
        for i in xrange(m-2, -1, -1):
            if grid[i][-1] >= 0:
                res[-1] += grid[i][-1]
            else:
                print 'Ilegal value: %d at (%d, %d).' %(val, i, n-1)
                return
            for j in xrange(n-2, -1, -1):
                val = grid[i][j]
                if val >= 0:
                    res[j] = val + min(res[j], res[j+1])
                else:
                    print 'Ilegal value: %d at (%d, %d).' %(val, i, j)
                    return
        return res[0]

# debug
s = Solution()
print s.minPathSum([ [1,3,1], [1,5,1], [4,2,1] ])
print s.minPathSum([ [], [] ])
