class Solution(object):
    def findPeakElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        low,high = 0,len(nums)-1
        while low < high:
            mid = (high - low) // 2 + low
            if nums[mid] > nums[mid+1]:
                if (low == mid) or (nums[mid] > nums[mid-1]):
                    return mid
                else:
                    high = mid - 1
            else:
                low = mid + 1
        return low

# debug
s = Solution()
print s.findPeakElement([1,2,3,1])
print s.findPeakElement([1,2,1,3,5,6,4])
print s.findPeakElement([1,2])
print s.findPeakElement([2,1])
