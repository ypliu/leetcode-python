class Solution(object):
    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """

        if not nums or len(nums) < 2:
            return

        index0, index1, index2 = 0, 0, len(nums)-1
        while index1 <= index2:
            num = nums[index1]
            if 0 == num:
                nums[index0], nums[index1] = 0, nums[index0]
                index0 += 1
                index1 += 1
            elif 1 == num:
                index1 += 1
            elif 2 == num:
                nums[index1], nums[index2] = nums[index2], 2
                index2 -= 1

# debug
s = Solution()
nums = [2,0,2,1,1,0]
s.sortColors(nums)
print nums
