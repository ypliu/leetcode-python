class Solution(object):
    def uniquePathsWithObstacles(self, obstacleGrid):
        """
        :type obstacleGrid: List[List[int]]
        :rtype: int
        """

        if not obstacleGrid or 0 == len(obstacleGrid) or 0 == len(obstacleGrid[0]) or 0 != obstacleGrid[0][0]:
            return 0

        m, n = len(obstacleGrid), len(obstacleGrid[0])
        res = [0 for _ in xrange(n)]
        for j in xrange(n-1, -1, -1):
            if 0 == obstacleGrid[m-1][j]:
                res[j] = 1
            elif 1 == obstacleGrid[m-1][j]:
                break
            else:
                print 'Ilegal value: %d at (%d, %d).' %(obstacleGrid[m-1][j], (m-1), j)
                return
        for i in xrange(m-2, -1, -1):
            if 1 == obstacleGrid[i][-1]:
                res[-1] = 0
            for j in xrange(n-2, -1, -1):
                val = obstacleGrid[i][j]
                if 1 == val:
                    res[j] = 0 
                elif 0 == val:
                    res[j] += res[j+1]
                else:
                    print 'Ilegal value: %d at (%d, %d).' %(val, i, j)
                    return
        return res[0]

# debug
s = Solution()
print s.uniquePathsWithObstacles([ [0,0,0], [0,1,0], [0,0,0] ])
print s.uniquePathsWithObstacles([ [0,0,0], [0,1,0], [0,2,0] ])
