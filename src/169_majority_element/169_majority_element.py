class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        if not nums:
            return None
        elif len(nums) <= 2:
            return nums[0]
        # return sorted(num)[len(num)/2]
        res,count = None,0
        for n in nums:
            if 0 == count:
                res,count = n,1
            elif res != n:
                count -= 1
            else:
                count += 1
        return res

# debug
s = Solution()
print s.majorityElement([3,2,3])
print s.majorityElement([2,2,1,1,1,2,2])
