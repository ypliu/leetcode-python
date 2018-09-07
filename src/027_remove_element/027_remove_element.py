class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """

        i, last = 0, len(nums)-1
        while i <= last:
            if nums[i] == val:
                nums[i] = nums[last]
                last -= 1
            else:
                i += 1
        return i  # =last+1

# debug
s = Solution()
print s.removeElement([0,1,2,2,3,0,4,2], 2)
