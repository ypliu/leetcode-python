class Solution(object):
    def minSubArrayLen(self, s, nums):
        """
        :type s: int
        :type nums: List[int]
        :rtype: int
        """

        if (not nums) or (len(nums) == 0):
            return 0
        elif (s <= nums[0]):
            return 1
        sum_t = 0; start = -1
        res = len(nums) + 1
        for i in range(len(nums)):
            sum_t += nums[i]
            if (sum_t >= s):
                while (sum_t >= s):
                    start += 1
                    sum_t -= nums[start]
                res = min(i-start+1, res)
        return 0 if res > len(nums) else res

# debug
s = Solution()
print s.minSubArrayLen(7, [2,3,1,2,4,3])
