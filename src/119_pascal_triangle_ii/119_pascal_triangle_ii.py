class Solution(object):
    def getRow(self, rowIndex):
        """
        :type rowIndex: int
        :rtype: List[int]
        """

        if rowIndex < 0:
            return []
        res = [1]
        for rth in range(1, rowIndex+1):
            i = rth >> 1; j = rth - i
            while i > 0:
                res[i] = res[j] = res[i] + res[i-1]
                i -= 1; j += 1
            res.append(1)
        return res

# debug
s = Solution()
print s.getRow(5)
