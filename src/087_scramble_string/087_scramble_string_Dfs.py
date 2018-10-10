class Solution(object):
    def isScramble(self, s1, s2):
        """
        :type s1: str
        :type s2: str
        :rtype: bool
        """

        if not s1:
            return not s2
        elif len(s1) != len(s2):
            return False
        elif not self.isSameCharSet(s1, s2):
            return False
        elif len(s1) <= 3:
            return True
        elif s1 == s2:
            return True

        for i in range(1, len(s1)):
            if self.isScramble(s1[:i], s2[:i]) and self.isScramble(s1[i:], s2[i:]):
                return True
            if self.isScramble(s1[:i], s2[-i:]) and self.isScramble(s1[i:], s2[:-i]):
                return True
        return False

    def isSameCharSet(self, s1, s2):
        counts_ch = [0 for i in range(26)]
        for i in range(len(s1)):
            counts_ch[ord(s1[i])-ord('a')] += 1
            counts_ch[ord(s2[i])-ord('a')] -= 1
        for i in range(26):
            if 0 != counts_ch[i]:
                return False
        return True

# debug
s = Solution()
print s.isScramble("great", "rgeat")
print s.isScramble("abcde", "caebd")
