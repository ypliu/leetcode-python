class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """

        if (not s) or (not t):
            return (s == t)
        elif (len(s) != len(t)):
            return False
        return self.isAnagramBasedSorting(s, t)
        return self.isAnagramBasedCounting(s, t)

    def isAnagramBasedSorting(self, s, t):
        return (sorted(s) == sorted(t))

    def isAnagramBasedCounting(self, s, t):
        count_ch = [0 for _ in range(26)]
        ord_a = ord('a')
        for i in range(len(s)):
            count_ch[ord(s[i]) - ord_a] += 1
            count_ch[ord(t[i]) - ord_a] -= 1
        for n in count_ch:
            if (0 != n):
                return False
        return True

# debug
s = Solution()
print s.isAnagram("anagram", "nagaram")
print s.isAnagram("rat", "car")
