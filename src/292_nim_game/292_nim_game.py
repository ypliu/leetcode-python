class Solution(object):
    def canWinNim(self, n):
        """
        :type n: int
        :rtype: bool
        """

        if (n <= 0):
            return None
        return (n & 3 != 0)

# debug
s = Solution()
print s.canWinNim(4)
