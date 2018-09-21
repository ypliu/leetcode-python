class Solution(object):
    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """

        if not nums or 0 == len(nums):
            return None
        elif 1 == len(nums):
            return True

        last = len(nums) - 1
        start = max_curr = 0
        max_next = 0
        while max_curr < last:
            while start <= max_curr:
                max_next = max(max_next, start + nums[start])
                start += 1
            if max_curr == max_next:
                return False
            max_curr = max_next
        return True

# debug
s = Solution()
print s.canJump([2,3,1,1,4])
print s.canJump([3,2,1,0,4])
