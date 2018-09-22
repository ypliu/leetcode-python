class Solution(object):
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """

        if not s or 0 == len(s):
            return 0
        counts, words = self.mySplit(s)
        if 0 == counts:
            return 0
        return len(words[counts-1])

    def mySplit(self, s):
        words = []; word = ''; counts = 0
        s += ' '
        for ch in s:
            if ' ' == ch or '\t' == ch:
                if '' == word:
                    continue
                else:
                    counts += 1
                    words.append(word)
                    word = ''
            else:
                word += ch
        return counts, words

# debug
s = Solution()
print s.lengthOfLastWord("Hello World")
print s.lengthOfLastWord("a	b")
print s.lengthOfLastWord("a    ")
print s.lengthOfLastWord("    b")
print s.lengthOfLastWord("  ")
print s.lengthOfLastWord("")
print s.lengthOfLastWord(None)
