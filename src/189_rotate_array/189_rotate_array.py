class Solution(object):
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: void Do not return anything, modify nums in-place instead.
        """

        def reverse(nums, start, end):
            while start < end:
                nums[start],nums[end] = nums[end],nums[start]
                start += 1; end -= 1

        if (not nums) or (k <= 0) or (0 == (k % len(nums))):
            return
        k %= len(nums)
        reverse(nums, 0, len(nums)-k-1)
        reverse(nums, len(nums)-k, len(nums)-1)
        reverse(nums, 0, len(nums)-1)

# debug
s = Solution()
nums = [1,2,3,4,5,6,7]
s.rotate(nums, 3)
print nums
nums = [-1,-100,3,99]
s.rotate(nums, 2)
print nums
