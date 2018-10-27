class Solution(object):
    def minimumTotal(self, triangle):
        """
        :type triangle: List[List[int]]
        :rtype: int
        """

        if not triangle or 0 == len(triangle):
            return None
        n = len(triangle)
        res = [0 for _ in range(n)]; res[0] = triangle[0][0]
        for i in range(1, n):
            res[i] = res[i-1] + triangle[i][i]
            for j in range(i-1, 0, -1):
                res[j] = min(res[j], res[j-1]) + triangle[i][j]
            res[0] += triangle[i][0]
        min_val = res[0]
        for i in range(1, n):
            if min_val > res[i]:
                min_val = res[i]
        return min_val

    def minimumTotalBetterFromAns(self, triangle):
        if not triangle or 0 == len(triangle):
            return None
        res = triangle[-1]
        for row in reversed(triangle[:-1]):
            for i in range(len(row)):
                res[i] = min(res[i], res[i+1]) + row[i]
        return res[0]

# debug
s = Solution()
print s.minimumTotal([ [2], [3,4], [6,5,7], [4,1,8,3] ])
print s.minimumTotalBetterFromAns([ [2], [3,4], [6,5,7], [4,1,8,3] ])
