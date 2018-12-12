class Solution(object):
    def countPrimes(self, n):
        """
        :type n: int
        :rtype: int
        """

        if n < 3:
            return 0
        elif n < 5:
            return (n - 2)
        #s = [1 for i in range(n)]
        s = [1] * (n)
        for i in range(3, int(n ** 0.5)+1, 2):
            if (0 == s[i]):
                continue
            for j in range(i*i, n, i*2):
                s[j] = 0
        return (sum(s[5::2]) + 2)

# debug
s = Solution()
print s.countPrimes(10000)
