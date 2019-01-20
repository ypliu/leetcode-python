class Solution(object):
    def hIndex(self, citations):
        """
        :type citations: List[int]
        :rtype: int
        """

        if (not citations) or (len(citations) < 1):
            return 0
        n = len(citations)
        low,high = 0,n-1
        while (low <= high):
            mid = (high - low) // 2 + low
            if (citations[mid] >= (n-mid)):
                high = mid - 1
            else:
                low = mid + 1
        return (n - low)

# debug
s = Solution()
print s.hIndex([0,1,3,5,6])
print s.hIndex([3,3,3])
print s.hIndex([0])
