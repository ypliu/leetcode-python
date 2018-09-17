class Solution(object):
    def permuteUnique(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """

        if not nums:
            return []

        res = [[]]
        for num in nums:
            res_temp = []
            for prev_perm in res:
                # try to insert `num` at each position of `prev_perm`, front and back, but must avoid unnecessary repetition
                for i in xrange(len(prev_perm)+1):
                    res_temp.append(prev_perm[:i]+[num]+prev_perm[i:])
                    if i < len(prev_perm) and prev_perm[i] == num:
                        break
            res = res_temp
        return res

# debug
s = Solution()
print s.permuteUnique([1,1,2])
print s.permuteUnique([2,2,1,1])
print s.permuteUnique(None)
