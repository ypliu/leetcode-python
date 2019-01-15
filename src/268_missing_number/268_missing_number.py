class Solution(object):
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        if (not nums):
            return 0
        n = len(nums)
        return ((n+1) * n // 2 - sum(nums))

# debug
s = Solution()
print s.missingNumber([3,0,1])
print s.missingNumber([9,6,4,2,3,5,7,0,1])
