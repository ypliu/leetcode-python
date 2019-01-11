class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """

        if (not nums) or (len(nums) %2 == 1):
            return None
        xor_sum = 0; n1 = 0
        for n in nums:
            xor_sum ^= n
        # fetch the digit in least-significant bit is equal to 1
        # bit_diff = (((xor_sum-1) ^ xor_sum) + 1) >> 1
        # bit_diff = xor_sum & ~(xor_sum - 1)
        bit_diff = xor_sum & -xor_sum
        for n in nums:
            if (n & bit_diff):
                n1 ^= n
        return [n1, xor_sum^n1]

# debug
s = Solution()
print s.singleNumber([1,2,1,3,2,5])
