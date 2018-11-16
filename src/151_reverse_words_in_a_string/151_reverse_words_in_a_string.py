class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """

        # return ' '.join(s.split()[::-1])
        if not s:
            return ""
        res = ""; i = 0
        while i < len(s):
            if (' ' == s[i]):
                i += 1
                continue
            word = s[i]; i += 1
            while (i < len(s)) and (' ' != s[i]):
                word += s[i]
                i += 1
            res = word + ' ' + res
            i += 1
        return res[:-1]

# debug
s = Solution()
print s.reverseWords(" the sky   is blue   ")
