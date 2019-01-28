class Solution(object):
    def findDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        if (not nums) or (len(nums) < 2):
            return 0
        return self.findDuplicateBasedCycleDetection(nums)
        # return self.findDuplicateBasedBinarySearch(nums)

    def findDuplicateBasedBinarySearch(self, nums):  # O(n*log^n)
        low,high = 0,len(nums)-1
        while (low < high):
            mid = (high - low) // 2 + low
            count_le = 0
            for n in nums:
                if (n <= mid):
                    count_le += 1
            if (count_le <= mid):
                low = mid + 1
            else:
                high = mid
        return low

    def findDuplicateBasedCycleDetection(self, nums):  # O(n)
        slow,fast = nums[0],nums[0]
        while (0 < fast < len(nums)) and (0 < nums[fast] < len(nums)):
            slow = nums[slow]
            fast = nums[nums[fast]]
            if (slow == fast):
                temp = nums[0]
                while (slow != temp):
                    slow = nums[slow]
                    temp = nums[temp]
                return slow
        return -1 # no duplicate

# debug
s = Solution()
print s.findDuplicate([1,3,4,2,2])
print s.findDuplicate([3,1,3,4,2])
