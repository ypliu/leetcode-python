class Solution(object):
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """

        if x < 0:
            print "x must be a non-negative integer."
            return
        elif 0 == x or 1 == x:
            return x

        high = x; low = 1
        while low + 1 < high:
            mid = (high + low) >> 1
            temp = mid * mid
            if temp == x:
                return mid
            elif temp < x:
                low = mid
            else:
                high = mid
        return low

# debug
s = Solution()
print s.mySqrt(4)
print s.mySqrt(8)
print s.mySqrt(0)
