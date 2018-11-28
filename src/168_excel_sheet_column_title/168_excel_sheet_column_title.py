class Solution(object):
    def convertToTitle(self, n):
        """
        :type n: int
        :rtype: str
        """

        if n <= 0:
            return None
        res = ""; diff = ord('A')
        while n > 0:
            n -= 1
            res = chr((n % 26) + diff) + res
            n //= 26
        return res

# debug
s = Solution()
print s.convertToTitle(1)
print s.convertToTitle(28)
print s.convertToTitle(701)
