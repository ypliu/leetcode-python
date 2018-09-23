class Solution(object):
    def getPermutation(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: str
        """

        if 0 == n or k <= 0:
            return ""
        fact = [1, 1]
        for i in xrange(2, n+1):
            fact += [fact[-1] * i]
        if k > fact[-1]:
            return ""

        k -= 1; res = ""
        nums = [str(i) for i in xrange(1, n+1)]
        while n > 0:
            n -= 1
            i_th = k // fact[n]
            k %= fact[n]
            res += nums[i_th]
            del(nums[i_th])
        return res

# debug
s = Solution()
print s.getPermutation(3, 3)
print s.getPermutation(4, 9)
print s.getPermutation(4, 24)
