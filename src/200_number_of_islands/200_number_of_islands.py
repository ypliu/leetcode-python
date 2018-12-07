class Solution(object):
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """

        def fillGridBfs(i, j): # TLE???
            q = [(i,j)]
            while q:
                q_t = []
                for r,c in q:
                    grid[r][c] = '@'
                    if (r > 0) and ('1' == grid[r-1][c]):
                        q_t.append((r-1,c))
                    if (r+1 < n_r) and ('1' == grid[r+1][c]):
                        q_t.append((r+1,c))
                    if (c > 0) and ('1' == grid[r][c-1]):
                        q_t.append((r,c-1))
                    if (c+1 < n_c) and ('1' == grid[r][c+1]):
                        q_t.append((r,c+1))
                q = q_t

        def fillGridDfsRecursion(i, j):
            grid[i][j] = '@'
            if (i > 0) and ('1' == grid[i-1][j]):
                fillGridDfsRecursion(i-1, j)
            if (i+1 < n_r) and ('1' == grid[i+1][j]):
                fillGridDfsRecursion(i+1, j)
            if (j > 0) and ('1' == grid[i][j-1]):
                fillGridDfsRecursion(i, j-1)
            if (j+1 < n_c) and ('1' == grid[i][j+1]):
                fillGridDfsRecursion(i, j+1)

        def fillGridDfsIteration(i, j):
            q = [(i,j)]
            while q:
                r,c = q.pop()
                grid[r][c] = '@'
                if (r > 0) and ('1' == grid[r-1][c]):
                    q.append((r-1,c))
                if (r+1 < n_r) and ('1' == grid[r+1][c]):
                    q.append((r+1,c))
                if (c > 0) and ('1' == grid[r][c-1]):
                    q.append((r,c-1))
                if (c+1 < n_c) and ('1' == grid[r][c+1]):
                    q.append((r,c+1))

        if (not grid) or (len(grid) < 1) or (len(grid[0]) < 1):
            return 0
        n_r = len(grid); n_c = len(grid[0])
        count = 0
        for i in range(n_r):
            for j in range(n_c):
                if ('1' == grid[i][j]):
                    count += 1
                    # fillGridBfs(i, j)
                    # fillGridDfsRecursion(i, j)
                    fillGridDfsIteration(i, j)
        return count

# debug
s = Solution()
grid = [ ['1','1','1','1','0'], ['1','1','0','1','0'], ['1','1','0','0','0'], ['0','0','0','0','0'] ]
print s.numIslands(grid)
grid = [ ['1','1','0','0','0'], ['1','1','0','0','0'], ['0','0','1','0','0'], ['0','0','0','1','1'] ]
print s.numIslands(grid)
