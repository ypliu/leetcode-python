class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        # return (sum(set(nums))*3 - sum(nums)) // 2
        
        if (not nums) or (len(nums)%3 != 1):
            return None
        residue = 0; carry = 0
        for n in nums:
            residue = (residue ^ n) & (~carry)
            carry = (carry ^ n) & (~residue)
        return residue

# debug
s = Solution()
print s.singleNumber([2,2,3,2])
print s.singleNumber([0,1,0,1,0,1,99])
