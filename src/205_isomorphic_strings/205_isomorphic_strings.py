class Solution(object):
    def isIsomorphic(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """

        if (not s) or (not t):
            return (s == t)
        elif len(s) != len(t):
            return False
        dict_s2t = {}
        for i in range(len(s)):
            ch_s,ch_t = s[i],t[i]
            if (ch_s in dict_s2t):
                if (dict_s2t[ch_s] != ch_t):
                    return False
            else:
                if (ch_t in dict_s2t.values()):
                    return False
                dict_s2t[ch_s] = ch_t
        return True

# debug
s = Solution()
print s.isIsomorphic("egg", "add")
print s.isIsomorphic("foo", "bar")
print s.isIsomorphic("paper", "title")
print s.isIsomorphic("ab", "ee")
