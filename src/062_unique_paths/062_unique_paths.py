class Solution(object):
    def uniquePaths(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """

        if m <= 0 or n <= 0:
            return 0
        elif 1 == m or 1 == n:
            return 1

        total = m + n - 2
        counts = min(m, n) - 1
        numerator = denominator = 1
        while counts >= 1:
            numerator *= total
            denominator *= counts
            total -= 1
            counts -= 1
        return (numerator / denominator)

# debug
s = Solution()
print s.uniquePaths(3, 2)
print s.uniquePaths(7, 3)
