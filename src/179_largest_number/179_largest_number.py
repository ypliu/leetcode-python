class Solution(object):
    def largestNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: str
        """

        res = ''.join(sorted([str(n) for n in nums], cmp=lambda s1,s2:cmp(s1+s2, 

s2+s1), reverse = True))
        return "0" if (res and '0' == res[0]) else res

# debug
s = Solution()
print s.largestNumber([10,2])
print s.largestNumber([3,30,34,5,9])
