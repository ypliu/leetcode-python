class Solution(object):
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """

        if numRows <= 0:
            return []
        res = [[1]]
        for rth in range(1, numRows):
            rth_row = [1 for _ in range(rth+1)]
            i = 1; j = rth - 1
            while i <= j:
                rth_row[i] = rth_row[j] = res[-1][i] + res[-1][i-1]
                i += 1; j -= 1
            res.append(rth_row)
        return res

# debug
s = Solution()
print s.generate(5)
