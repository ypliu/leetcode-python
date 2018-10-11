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

        nums.sort()
        return self.bfs(nums)

    def bfs(self, nums):
        res = [[]]; start = 1
        for i, num in enumerate(nums):
            size = len(res)
            if 0 == i or num != nums[i-1]:
                start = 0
            for j in range(start, size):
                res.append(res[j] + [num])
            start = size
        return res

# debug
s = Solution()
print s.subsetsWithDup([1,2,2])
