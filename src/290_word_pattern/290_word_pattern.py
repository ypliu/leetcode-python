class Solution(object):
    def wordPattern(self, pattern, str):
        """
        :type pattern: str
        :type str: str
        :rtype: bool
        """

        if (not pattern) or (not str):
            return (pattern == str)
        words_str = str.split()
        if (len(pattern) != len(words_str)):
            return False
        dict_p2s = {}
        for i in range(len(pattern)):
            ch,word = pattern[i],words_str[i]
            if (ch in dict_p2s):
                if (dict_p2s[ch] != word):
                    return False
            else:
                if (word in dict_p2s.values()):
                    return False
                dict_p2s[ch] = word
        return True

# debug
s = Solution()
print s.wordPattern("abba", "dog cat cat dog")
print s.wordPattern("abba", "dog cat cat fish")
print s.wordPattern("aaaa", "dog cat cat dog")
print s.wordPattern("abba", "dog dog dog dog")
