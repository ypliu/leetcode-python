class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        dict = {}
        for index, value in enumerate(nums):
            difference = target - value
            if difference in dict:
                return (dict[difference], index)
            dict[value] = index

# debug
s = Solution()
print s.twoSum([2, 7, 11, 15], 9)
