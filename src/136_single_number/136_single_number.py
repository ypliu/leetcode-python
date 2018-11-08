class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        # return (sum(set(nums))*2 - sum(nums))
        if (not nums) or (len(nums) % 2 == 0):
            return None
        res = 0
        for n in nums:
            res ^= n
        return res

# debug
s = Solution()
print s.singleNumber([2,2,1])
print s.singleNumber([4,1,2,1,2])
