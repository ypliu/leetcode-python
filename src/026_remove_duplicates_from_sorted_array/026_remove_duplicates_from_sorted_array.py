class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        i, res = 1, len(nums)
        while i < res:
            if nums[i-1] == nums[i]:
                del nums[i]
                res -= 1
            else:
                i += 1

        return res

# debug
s = Solution()
nums = [0,0,1,1,1,2,2,3,3,4]
print s.removeDuplicates(nums)
