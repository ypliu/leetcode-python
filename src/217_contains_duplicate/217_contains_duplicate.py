class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        return (len(nums) > len(set(nums)))

# debug
s = Solution()
print s.containsDuplicate([1,2,3,1])
print s.containsDuplicate([1,2,3,4])
print s.containsDuplicate([1,1,1,3,3,4,3,2,4,2])
