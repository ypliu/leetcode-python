import math
class Solution(object):
    def numSquares(self, n):
        """
        :type n: int
        :rtype: int
        """

        if (n <= 0):
            return 0
        # https://leetcode.com/problems/perfect-squares/discuss/71488/Summary-of-4-different-solutions-(BFS-DP-static-DP-and-mathematics)
        return self.numSquaresLagrangeFourSquareTheorem(n)  # Very Fast
        # return self.numSquaresDp(n)

    def numSquaresLagrangeFourSquareTheorem(self, n):
        n_sqrt = int(math.sqrt(n))
        if (n_sqrt*n_sqrt == n):
            return 1
        while ((n & 3) == 0):
            n >>= 2
        if ((n & 7) == 7):
            return 4
        for i in range(1, int(math.sqrt(n))+1):
            r = n - i * i
            r_sqrt = int(math.sqrt(r))
            if (r_sqrt * r_sqrt == r):
                return 2
        return 3

    def numSquaresDp(self, n):
        dp_table = [i for i in range(n+1)]
        for i in range(2, int(math.sqrt(n))+1):
            i_sqr = i * i
            dp_table[i_sqr] = 1
            for j in range(i_sqr+1, n+1):
                dp_table[j] = min(dp_table[j-i_sqr]+1, dp_table[j])
        return dp_table[-1]

# debug
s = Solution()
print s.numSquares(12)
print s.numSquares(13)
