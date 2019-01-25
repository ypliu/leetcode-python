class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """

        if (not nums) or (len(nums) <= 1):
            return
        index = 0
        for n in nums:
            if (n != 0):
                nums[index] = n
                index += 1
        for i in range(index, len(nums)):
            nums[i] = 0

# debug
s = Solution()
nums = [0,1,0,3,12]
s.moveZeroes(nums)
print nums
