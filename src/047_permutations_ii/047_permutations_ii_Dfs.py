class Solution(object):
    def permuteUnique(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """

        res = []
        nums.sort()
        self.dfs(nums, [], res)
        return res

    def dfs(self, unused, sol, res):
        if len(unused) <= 1:
            if len(unused) == 1:
                res.append(sol + [unused[0]])
            else:
                res.append(sol)
            return
        unused_temp = sorted(unused)
        for i in xrange(len(unused_temp)):
            it = unused_temp[i]
            if i > 0 and unused_temp[i-1] == it:
                continue
            unused.remove(it)
            self.dfs(unused, sol+[it], res)
            unused.append(it)

# debug
s = Solution()
print s.permuteUnique([2,2,1,1])
