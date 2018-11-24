class Solution(object):
    def findMin(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        if (not nums) or (0 == len(nums)):
            return None
        low = 0; high = len(nums)-1
        while low < high:
            if nums[low] < nums[high]:
                return nums[low]
            mid = (high - low) // 2 + low
            if nums[low] < nums[mid]:
                low = mid + 1
            else:
                low += 1
                high = mid
        return nums[low]

# debug
s = Solution()
print s.findMin([3,4,5,1,2])
print s.findMin([4,5,6,7,0,1,2])
