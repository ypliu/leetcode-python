class Solution(object):
    def nthUglyNumber(self, n):
        """
        :type n: int
        :rtype: int
        """

        if (n < 1) or (n > 1690):
            return -1
        elif (n < 7):
            return n
        # the number of UglyNumbers is $C_{m+2}^{2}$, which $m$ is the sum of exponents (powers) in 2,3,5 prime-factorization
        dp = [0 for i in range(n)]; dp[0] = 1
        factors = [2, 3, 5]; next_u = factors[:]
        index_exp = [0 for _ in range(len(factors))]
        for i in range(1, n):
            dp[i] = v = min(next_u)
            for j in range(len(factors)):
                if (v == next_u[j]):
                    index_exp[j] += 1
                    next_u[j] = factors[j] * dp[index_exp[j]]
        return dp[-1]

# debug
s = Solution()
print s.nthUglyNumber(10)
