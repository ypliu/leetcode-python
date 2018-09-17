class Solution(object):
    def permuteUnique(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """

        if not nums:
            return []

        res = [[ ]]
        for num in nums:
            res_temp = []
            for prev_perm in res:
                prev_perm.append(num)
                res_temp.append(prev_perm[:])
                for j in range(len(prev_perm)):
                    if prev_perm[j] == num:
                        break
                    prev_perm[j], prev_perm[-1] = prev_perm[-1], prev_perm[j]
                    res_temp.append(prev_perm[:])
                    prev_perm[j], prev_perm[-1] = prev_perm[-1], prev_perm[j]
            res = res_temp
        return res

# debug
s = Solution()
print s.permuteUnique([2,1,1,2])
