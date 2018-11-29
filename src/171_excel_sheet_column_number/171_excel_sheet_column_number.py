class Solution(object):
    def titleToNumber(self, s):
        """
        :type s: str
        :rtype: int
        """

        if (not s) or (0 == len(s)):
            return 0
        res = 0; shift = ord('A')-1
        for ch in s:
            res = res * 26 + ord(ch) - shift
        return res

# debug
s = Solution()
print s.titleToNumber("A")
print s.titleToNumber("AB")
print s.titleToNumber("ZY")
