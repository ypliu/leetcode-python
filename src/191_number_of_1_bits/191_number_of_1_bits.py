class Solution(object):
    def hammingWeight(self, n):
        """
        :type n: int
        :rtype: int
        """

        res = 0
        while (n != 0):
            res += 1
            n &= n - 1
        return res

# debug
s = Solution()
print s.hammingWeight(11)
print s.hammingWeight(128)
