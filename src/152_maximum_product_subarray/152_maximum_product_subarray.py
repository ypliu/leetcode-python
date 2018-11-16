class Solution(object):
    def maxProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        if not nums or 0 == len(nums):
            return None
        max_pro = pre_min = pre_max = nums[0]
        for n in nums[1:]:
            pre_min *= n; pre_max *= n
            pre_min, pre_max = min(pre_min, pre_max, n), max(pre_min, pre_max, n)
            max_pro = max(max_pro, pre_max)
        return max_pro

# debug
s = Solution()
print s.maxProduct([2,3,-2,4])
print s.maxProduct([-2,0,-1])
print s.maxProduct([-2,2,2,2,-2])
print s.maxProduct([-2,2,2,2])
print s.maxProduct([2,2,2,-2])
