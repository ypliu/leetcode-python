class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        if (not nums) or (len(nums) <= 0):
            return 0
        elif (len(nums) < 4):
            return max(nums)
        def helper(arr):
            pre2, pre1 = arr[0], max(arr[0],arr[1])
            for n in arr[2:]:
                pre2, pre1 = pre1, max(pre2+n,pre1)
            return pre1
        return max(helper(nums[:-1]), helper(nums[1:]))

# debug
s = Solution()
print s.rob([2,3,2])
print s.rob([1,2,3,1])
