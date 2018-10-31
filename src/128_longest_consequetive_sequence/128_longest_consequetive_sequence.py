class Solution(object):
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        nums = set(nums)
        res = 0
        for n_left in nums:
            if (n_left - 1) not in nums:
                n_right = n_left + 1
                while n_right in nums:
                    n_right += 1
                res = max(res, n_right - n_left)
        return res

# debug
s = Solution()
print s.longestConsecutive([100, 4, 200, 1, 3, 2])
print s.longestConsecutive([])
