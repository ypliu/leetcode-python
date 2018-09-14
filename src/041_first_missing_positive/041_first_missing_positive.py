class Solution(object):
    def firstMissingPositive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        i, n = 0, len(nums)
        while i < n:
            val = nums[i]
            while val > 0 and val <= n and val != nums[val-1]:
                nums[i] = nums[val-1]
                nums[val-1] = val
                val = nums[i]
            i += 1

        i = 1
        while i <= n:
            if i != nums[i-1]:
                return i
            i += 1
        return (n+1)

# debug
s = Solution()
print s.firstMissingPositive([1,2,0])
print s.firstMissingPositive([3,4,-1,1])
print s.firstMissingPositive([7,8,9,11,12])
