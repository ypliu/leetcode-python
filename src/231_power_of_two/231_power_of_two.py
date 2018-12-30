class Solution(object):
    def isPowerOfTwo(self, n):
        """
        :type n: int
        :rtype: bool
        """

        return (n > 0) and (((n-1) & n) == 0)

# debug
s = Solution()
print s.isPowerOfTwo(1)
print s.isPowerOfTwo(16)
print s.isPowerOfTwo(218)
