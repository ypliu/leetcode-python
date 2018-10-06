class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: bool
        """

        low = 0; high = len(nums) - 1
        while low <= high:
            mid = (low + high) >> 1
            if nums[mid] == target:
                return True
            elif nums[low] < nums[mid]:
                if nums[low] <= target and target < nums[mid]:
                    high = mid - 1
                else:
                    low = mid + 1
            elif nums[mid] < nums[high]:
                if nums[mid] < target and target <= nums[high]:
                    low = mid + 1
                else:
                    high = mid - 1
            else:
                while low <= mid and nums[low] == nums[mid]:
                    low += 1
                while high >= mid and nums[high] == nums[mid]:
                    high -= 1
        return False

# debug
s = Solution()
print s.search([2,5,6,0,0,1,2], 0)
print s.search([2,5,6,0,0,1,2], 3)
print s.search([1,3,1,1,1], 3)
print s.search([1], 1)
