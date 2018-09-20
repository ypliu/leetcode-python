class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        if not nums or 0 == len(nums):
            return None
        elif 1 == len(nums):
            return nums[0]

        max_temp = sum_temp = nums[0]
        for i in xrange(1, len(nums)):
            sum_temp = (sum_temp + nums[i]) if (sum_temp > 0) else nums[i]
            max_temp = max(max_temp, sum_temp)

        return max_temp

# debug
s = Solution()
print s.maxSubArray(None)
print s.maxSubArray([-2])
print s.maxSubArray([-2,1,-3,4,-1,2,1,-5,4])
