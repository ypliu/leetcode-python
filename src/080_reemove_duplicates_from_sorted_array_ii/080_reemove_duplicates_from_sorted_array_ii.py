class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        if not nums:
            return 0
        elif len(nums) <= 2:
            return len(nums)

        index = 2
        for i in range(2, len(nums)):
            if nums[index-2] != nums[i]:
                nums[index] = nums[i]
                index += 1
        return index

# debug
s = Solution()
nums = [1,1,1,2,2,3]
print s.removeDuplicates(nums)
print nums
nums = [0,0,1,1,1,1,2,3,3]
print s.removeDuplicates(nums)
print nums
