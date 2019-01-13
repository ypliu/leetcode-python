class Solution(object):
    def isUgly(self, num):
        """
        :type num: int
        :rtype: bool
        """

        if (num < 1):
            return False
        factors = [2, 3, 5, 6, 10, 15, 30]
        for f in factors[::-1]:
            while ((num % f) == 0):
                num //= f
        return (1 == num)

# debug
s = Solution()
print s.isUgly(6)
print s.isUgly(8)
print s.isUgly(14)
