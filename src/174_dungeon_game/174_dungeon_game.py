class Solution(object):
    def calculateMinimumHP(self, dungeon):
        """
        :type dungeon: List[List[int]]
        :rtype: int
        """

        if (not dungeon) or (0 == len(dungeon)) or (0 == len(dungeon[0])):
            return 1
        n_row,n_col = len(dungeon),len(dungeon[0])
        health_dp = [0 for i in range(n_col)]
        health_dp[-1] = max(1-dungeon[-1][-1], 1)
        for j in range(n_col-2, -1, -1):
            health_dp[j] = max(health_dp[j+1]-dungeon[-1][j], 1)
        for i in range(n_row-2, -1, -1):
            health_dp[-1] = max(health_dp[-1]-dungeon[i][-1], 1)
            for j in range(n_col-2, -1, -1):
                health_dp[j] = max(min(health_dp[j],health_dp[j+1])-dungeon[i][j], 1)
        return health_dp[0]

# debug
s = Solution()
print s.calculateMinimumHP([[-2,-3,3], [-5,-10,1], [10,30,-5]])
print s.calculateMinimumHP([[0,-3],[-10,0]])
