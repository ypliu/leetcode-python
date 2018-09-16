class Solution(object):
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """

        # return list(itertools.permutations(nums))
        if not nums:
            return []

        res = [[ ]]
        for num in nums:
            res_temp = []
            # insert num in at each position of each element during BFS all previous Permutations -res
            for prev_perm in res:
                prev_perm.append(num)
                res_temp.append(prev_perm)
                for j in range(len(prev_perm)-1):
                    prev_perm[j], prev_perm[-1] = prev_perm[-1], prev_perm[j]
                    res_temp.append(prev_perm[:])
                    prev_perm[j], prev_perm[-1] = prev_perm[-1], prev_perm[j]
            res = res_temp
        return res

# debug
s = Solution()
print s.permute([1,2,3])
