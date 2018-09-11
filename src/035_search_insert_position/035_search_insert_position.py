class Solution(object):
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """

        left, right = 0, len(nums)-1
        if right < 0 or target <= nums[left]:
            return left
        elif target > nums[right]:
            return (right + 1)

        while left < right:
            mid = (left + right) // 2
            if target == nums[mid]:
                return mid
            elif target > nums[mid]:
                left = mid + 1
            else:
                right = mid

        return right

# debug
s = Solution()
print s.searchInsert([1,3,5,6], 0)
print s.searchInsert([1,3,5,6], 2)
print s.searchInsert([1,3,5,6], 5)
print s.searchInsert([1,3,5,6], 7)
