class Solution(object):
    def rangeBitwiseAnd(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """

        # return (self.rangeBitwiseAnd(m>>1, n>>1) << 1) if (n > m) else m
        if (m <= 0) or (m > n) or (n > 2147483647):
            return 0
        while m < n:
            n &= n-1
        return n

# debug
s = Solution()
print s.rangeBitwiseAnd(5, 7)
print s.rangeBitwiseAnd(0, 1)
print s.rangeBitwiseAnd(128, 129)
