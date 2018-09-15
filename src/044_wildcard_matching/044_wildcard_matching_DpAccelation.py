class Solution(object):
    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """

        i = j = 0
        pos_s, pos_p = -1, -1

        while i < len(s):
            if j < len(p) and (s[i] == p[j] or p[j] == "?"):
                i += 1
                j += 1
            elif j < len(p) and p[j] == '*':
                pos_s = i
                pos_p = j
                j += 1
            elif pos_p != -1:
                pos_s += 1
                i = pos_s
                j = pos_p
            else:
                return False
        while j < len(p) and p[j] == "*":
            j += 1
        return (j == len(p))

# debug
s = Solution()
print s.isMatch("aa", "a")
print s.isMatch("aa", "*")
print s.isMatch("cb", "?a")
print s.isMatch("adceb", "*a*b")
print s.isMatch("acdcb", "a*c?b")
print s.isMatch("", "*")
