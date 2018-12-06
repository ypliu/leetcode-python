class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        if (not nums) or (len(nums) <= 0):
            return 0
        elif len(nums) <= 1:
            return nums[0]
        pre2, pre1 = nums[0], max(nums[0],nums[1])
        for n in nums[2:]:
            pre2, pre1 = pre1, max(n + pre2, pre1)
        return pre1

# debug
s = Solution()
print s.rob([1,2,3,1])
print s.rob([2,7,9,3,1])
print s.rob([10,1,1,10])
