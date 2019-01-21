# The isBadVersion API is already defined for you.
# @param version, an integer
# @return a bool
# def isBadVersion(version):

class Solution(object):
    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """

        if (n < 1):
            return 0
        elif (not isBadVersion(n)):
            return (n+1)
        low, high = 1, n
        while (low < high):
            mid = (high - low) // 2 + low
            if isBadVersion(mid):
                high = mid
            else:
                low = mid + 1
        return low

# debug
def isBadVersion(version):
    # arr = [ 0, False, False, False, False, False, False, True, True, True ]
    arr = [ 0, False, False, False, True, True, True, True, True, True ]
    return arr[version]
s = Solution()
print s.firstBadVersion(9)
