class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """


        if x == 0:
            return True

        revx = 0
        x2 = x
        while x2 > 0:
            revx = (revx * 10) + (x2 % 10)
            x2 /= 10

        return revx == x

#
s = Solution()
print s.isPalindrome(121)
