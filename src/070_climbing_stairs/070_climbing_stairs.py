class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """

        if n <= 0:
            print "n must be a positive integer."
            return 0
        elif n <= 2:
            return n

        pre_1 = 2; pre_2 = 1; i = 3
        while i <= n:
            res = pre_1 + pre_2
            pre_1, pre_2 = res, pre_1
            i += 1
        return res

# debug
s = Solution()
print s.climbStairs(2)
print s.climbStairs(3)
