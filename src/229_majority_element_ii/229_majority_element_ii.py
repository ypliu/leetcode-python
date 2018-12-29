class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """

        if (not nums) or (len(nums) < 1):
            return []
        n1,c1 = None, 0
        n2,c2 = None, 0
        for n in nums:
            if (n == n1):
                c1 += 1
            elif (n == n2):
                c2 += 1
            elif (0 == c1):
                n1 = n
                c1 = 1
            elif (0 == c2):
                n2 = n
                c2 = 1
            else:
                c1 -= 1
                c2 -= 1
        res = []
        c1 = c2 = 0
        thr = len(nums) // 3
        for n in nums:
            if (n == n1):
                c1 += 1
            elif (n == n2):
                c2 += 1
        if (c1 > thr):
            res.append(n1)
        if (c2 > thr):
            res.append(n2)
        return res

# debug
s = Solution()
print s.majorityElement([3,2,3])
print s.majorityElement([1,1,1,3,3,2,2,2])
