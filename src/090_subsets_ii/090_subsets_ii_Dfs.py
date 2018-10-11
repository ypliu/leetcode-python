class Solution(object):
    def subsetsWithDup(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """

        if not nums or 0 == len(nums):
            return [[]]
        elif 1 == len(nums):
            return [[], nums]

        nums.sort(); res = []
        self.dfs(nums, 0, [], res)
        return res

    def dfs(self, nums, i, sol, res):
        res.append(sol)
        for j in range(i, len(nums)):
            if j > i and nums[j] == nums[j-1]:
                continue
            self.dfs(nums, j+1, sol+[nums[j]], res)

# debug
s = Solution()
print s.subsetsWithDup([1,2,2])
