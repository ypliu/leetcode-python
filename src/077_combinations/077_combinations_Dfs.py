class Solution(object):
    def combine(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: List[List[int]]
        """

        # return list(itertools.combinations(range(1, n+1), k))
        if n <= 0 or k <= 0 or n < k:
            return []

        res = []
        self.dfs(n, k, [], res)
        return res

    def dfs(self, n, k, sol, res):
        start = 0 if 0 == len(sol) else sol[-1]
        if 0 == k:
            res.append(sol)
        elif 1 == k:
            for i in xrange(start+1, n+2-k):
                res.append(sol+[i])
        elif k > 1:
            for i in xrange(start+1, n+2-k):
                self.dfs(n, k-1, sol+[i], res)
        else:
            print "Error!"

# debug
s = Solution()
print s.combine(4, 2)
