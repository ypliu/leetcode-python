class Solution(object):
    def myPow(self, x, n):
        """
        :type x: float
        :type n: int
        :rtype: float
        """

        if n < 0:
            x, n = 1/x, -n

        res = 1.0
        while n > 0:
            if 1 == n % 2:
                res *= x
            x *= x
            n >>= 1

        return res

# debug
s = Solution()
print s.myPow(2.00000, 10)
print s.myPow(2.10000, 3)
print s.myPow(2.00000, -2)
