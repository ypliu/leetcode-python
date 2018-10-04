class Solution(object):
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """

        res = [[]]; len_res = 1
        if not nums or 0 == len(nums):
            return res

        for n in nums:
            for i in xrange(len_res):
                res.append(res[i]+[n])
            len_res <<= 1
        return res

# debug
s = Solution()
print s.subsets([1,2,3])
