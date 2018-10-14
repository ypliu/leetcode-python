class Solution(object):
    def numTrees(self, n):
        """
        :type n: int
        :rtype: int
        """

        # Catalan number, i.e., 1/(n+1) * C(n,2n) = C(n,2n) - C(n-1,2n)
        if n <= 0:
            return 0
        if n <= 2:
            return n
        res = [0 for i in range(n+1)]
        res[0] = res[1] = 1; res[2] = 2
        for i in range(3, n+1):
            for j in range(i):
                res[i] += res[j] * res[i-1-j]
        return res[n]

# debug
s = Solution()
print s.numTrees(5)
