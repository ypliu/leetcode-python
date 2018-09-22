class Solution(object):
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """

        if not s or 0 == len(s):
            return 0

        for i in xrange(len(s)-1, -1, -1):
            if ' ' != s[i] and '\t' != s[i]:
                end = i
                break
        else:
            return 0

        for i in xrange(end-1, -1, -1):
            if ' ' == s[i] or '\t' == s[i]:
                return (end - i)
        else:
            return (end + 1)

# debug
s = Solution()
print s.lengthOfLastWord("Hello World")
print s.lengthOfLastWord("a	b")
print s.lengthOfLastWord("a    ")
print s.lengthOfLastWord("    b")
print s.lengthOfLastWord("  ")
print s.lengthOfLastWord("")
print s.lengthOfLastWord(None)
