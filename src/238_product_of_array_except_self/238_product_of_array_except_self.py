class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """

        if (None == nums) or (len(nums) < 1):
            return []
        res = [1 for _ in range(len(nums))]
        product_f = product_b = 1
        tlen,i,j = len(nums),1,len(nums)-2
        while (i < tlen):
            product_f *= nums[i-1]
            res[i] *= product_f
            product_b *= nums[j+1]
            res[j] *= product_b
            i += 1
            j -= 1
        return res

# debug
s = Solution()
nums = [i for i in range(1,5)]
print s.productExceptSelf(nums)
