class Solution(object):
    def nextPermutation(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """

        last = len(nums) - 1
        i = last - 1
        while i >= 0:
            if nums[i] < nums[i+1]:
                break
            i -= 1

        if i < 0:
            self.reverse_seg(nums, 0, last)
        else:
            temp, j = nums[i], last
            while j > i:
                if temp < nums[j]:
                    break
                j -= 1
            nums[i] = nums[j]
            nums[j] = temp
            self.reverse_seg(nums, i+1, last)

    def reverse_seg(self, nums, start, end):
        while start < end:
            nums[start], nums[end] = nums[start], nums[end]
            start += 1
            end -= 1

# debug
s = Solution()
nums = [1,2,3]
s.nextPermutation(nums)
print nums
