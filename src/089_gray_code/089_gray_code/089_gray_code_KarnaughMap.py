class Solution(object):
    def grayCode(self, n):
        """
        :type n: int
        :rtype: List[int]
        """

        if n < 0:
            return []

        res = []; total = 1 << n
        for i in range(total):
            res.append((i >> 1) ^ i)
        return res

# debug
s = Solution()
print s.grayCode(2)
