class Solution(object):
    def grayCode(self, n):
        """
        :type n: int
        :rtype: List[int]
        """

        if n < 0:
            return []

        res = [0]
        for i in range(n):
            pre = 1 << i
            for num in reversed(res):
                res.append(pre + num)
        return res

# debug
s = Solution()
print s.grayCode(2)
