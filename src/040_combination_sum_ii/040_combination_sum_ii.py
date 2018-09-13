class Solution(object):
    def combinationSum2(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """

        if len(candidates) < 1:
            return []
        candidates.sort()
        if target < candidates[0]:
            return []

        res = []
        self.sumDfs2(candidates, 0, target, [], res)
        return res

    def sumDfs2(self, candidates, k, target, addends, res):
        for i in xrange(k, len(candidates)):
            addend = candidates[i]
            if i > k and addend == candidates[i-1]:
                continue
            if target > addend and i+1 < len(candidates):
                self.sumDfs2(candidates, i+1, target-addend, addends+[addend], res)
            elif target == addend:
                res.append(addends + [addend])
                return
            else:
                return

#debug
s = Solution()
print s.combinationSum2([2,3,6,7], 7)
print s.combinationSum2([10,1,2,7,6,1,5], 8)
print s.combinationSum2([2,5,2,1,2], 5)
