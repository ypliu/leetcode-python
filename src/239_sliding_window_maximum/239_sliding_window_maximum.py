class Solution(object):
    def maxSlidingWindow(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """

        if (not nums) or (len(nums) < 1) or (k < 1) or (k > len(nums)):
            return []
        return self.maxSlidingWindowBasedDeque(nums, k)

    def maxSlidingWindowBasedDeque(self, nums, k):
        dq = []; res = []
        for i,n in enumerate(nums):
            if (dq and ((i-k) == dq[0])):
                dq.pop(0)
            while (dq and (nums[dq[-1]] <= n)):
                dq.pop()
            dq.append(i)
            if (i >= k-1):
                res.append(nums[dq[0]])
        return res

# debug
s = Solution()
print s.maxSlidingWindow([1,3,-1,-3,5,3,6,7], 3)
