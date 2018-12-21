class Solution(object):
    def combinationSum3(self, k, n):
        """
        :type k: int
        :type n: int
        :rtype: List[List[int]]
        """

        if (k*(k+1)/2 > n) or (k*(19-k)/2 < n):
            return []
        elif (1 == k):
            return [n]
        res = []
        self.combinationSum3Dfs(k, n, [], res)
        return res

    def combinationSum3Dfs(self, k, r, sol, res):
        if (1 == k):
            if (r > sol[-1]) and (r <= 9):
                res.append(sol+[r])
            return
        lb = (sol[-1]+1) if (len(sol) > 0) else 1
        ub = min(r//k+1, 11-k)
        for i in range(lb, ub):
            if (i * k) >= r:
                break
            self.combinationSum3Dfs(k-1, r-i, sol+[i], res)

# debug
s = Solution()
print s.combinationSum3(3, 7)
print s.combinationSum3(3, 9)
