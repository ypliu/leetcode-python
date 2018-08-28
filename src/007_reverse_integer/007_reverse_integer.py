class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """

        res = int(str(abs(x))[::-1])
        if res > (1 << 31):
            return 0
        else:
            return res * cmp(x, 0)

# debug
s = Solution()
print s.reverse(1234)
