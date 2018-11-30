class Solution(object):
    def trailingZeroes(self, n):
        """
        :type n: int
        :rtype: int
        """

        if (not n) or (n < 5):
            return 0
        res = 0
        while n > 0:
            n //= 5
            res += n
        return res

# debug
s = Solution()
print s.trailingZeroes(3)
print s.trailingZeroes(5)
print s.trailingZeroes(10)
