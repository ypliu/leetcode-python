class Solution(object):
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """

        res = []
        self.dfs(nums, [], res)
        return res

    def dfs(self, unused, sol, res):
        if len(unused) <= 1:
            if len(unused) == 1:
                res.append(sol + [unused[0]])
            else:
                res.append(sol)
            return
        unused_temp = unused[:]
        for it in unused_temp:
            unused.remove(it)
            self.dfs(unused, sol+[it], res)
            unused.append(it)

# debug
s = Solution()
print s.permute([1,2,3])
