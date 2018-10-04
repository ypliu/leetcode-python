class Solution(object):
    def combine(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: List[List[int]]
        """

        # return list(itertools.combinations(range(1, n+1), k))
        return self.bfs(n, k)

    def bfs(self, n, k):
        if n <= 0 or k <= 0 or n < k:
            return []

        res = [[]]
        for i in xrange(k, 0, -1):
            temp = []
            for comb in res:
                start = 0 if 0 == len(comb) else comb[-1]
                for j in xrange(start+1, n+2-i):
                    temp.append(comb+[j])
            res = temp
        return res

# debug
s = Solution()
print s.combine(4, 2)
print s.combine(4, 4)
print s.combine(0, 2)
print s.combine(4, 0)
print s.combine(4, 5)
