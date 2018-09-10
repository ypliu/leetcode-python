class Solution(object):
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """

        left = self.searchLeft(nums, 0, len(nums)-1, target)
        if -1 == left:
            return [-1, -1]
        right = self.searchRight(nums, left, len(nums)-1, target)
        return [left, right]

    def searchLeft(self, nums, start, end, target):
        while start <= end:
            if target < nums[start] or target > nums[end]:
                return -1
            if target == nums[start]:
                return start
            start += 1
            mid = (start + end) // 2
            if target < nums[mid]:
                end = mid - 1
            elif target == nums[mid]:
                end = mid
            else:
                start = mid + 1
        return -1

    def searchRight(self, nums, start, end, target):
        while start <= end:
            if target < nums[start] or target > nums[end]:
                return -1
            if target == nums[end]:
                return end
            end -= 1 # Necessary!!! Maybe it is a infinite loop because division is math.floor()
            mid = (start + end) // 2
            if target < nums[mid]:
                end = mid - 1
            elif target == nums[mid]:
                start = mid
            else:
                start = mid + 1
        return -1

# debug
s = Solution()
print s.searchRange([5,7,7,8,8,10], 8)
print s.searchRange([5,7,7,8,8,10], 6)
