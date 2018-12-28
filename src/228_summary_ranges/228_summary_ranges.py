class Solution(object):
    def summaryRanges(self, nums):
        """
        :type nums: List[int]
        :rtype: List[str]
        """

        if (not nums) or (len(nums) < 1):
            return []
        start = nums[0]; count = 1
        res = []
        for n in (nums[1:] + [nums[0]]):
            if ((start + count) == n):
                count += 1
            else:
                if (1 == count):
                    res.append(str(start))
                else:
                    res.append(str(start) + "->" + str(start+count-1))
                start = n; count = 1
        return res

# debug
s = Solution()
print s.summaryRanges([0,1,2,4,5,7])
print s.summaryRanges([0,2,3,4,6,8,9])
print s.summaryRanges([])
