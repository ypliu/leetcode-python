class Solution(object):
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """

        if len(candidates) < 1:
            return [[]]
        candidates.sort()
        if target < candidates[0]:
            return [[]]

        res = []
        self.sumDfs(candidates, 0, target, [], res)
        return res

    def sumDfs(self, candidates, k, target, addends, res):
        if target < candidates[k]:
            return
        for i in xrange(k, len(candidates)):
            addend = candidates[i]
            addend_twice = addend << 1
            if i > k and addend == candidates[i-1]:
                continue
            if target > addend_twice:
                self.sumDfs(candidates, i, target-addend, addends+[addend], res)
            elif target == addend_twice:
                res.append(addends + [addend, addend])
            # elif target > addend: continue
            elif target == addend:
                res.append(addends + [addend])
                return
            elif target < addend:
                return

#debug
s = Solution()
print s.combinationSum([2,3,6,7], 7)
print s.combinationSum([2,3,5], 8)
