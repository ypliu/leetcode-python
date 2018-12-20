class Solution(object):
    def shortestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """

        if (not s) or (len(s) <= 1) or (s[::-1] == s):
            return s
        # return self.shortestPalindromeBruteForce(s)
        # return self.shortestPalindrome2PointersRecursion(s)
        return self.shortestPalindromeKMP(s)

    def shortestPalindromeBruteForce(self, s): # TLE
        s_rev = s[::-1]
        for i in range(len(s)):
            if (s[:len(s)-i] == s_rev[i:]):
                return (s_rev[:i] + s)

    def shortestPalindrome2PointersRecursion(self, s):
        i = 0
        for j in range(len(s)-1, -1, -1):
            if (s[i] == s[j]):
                i += 1
        if (i == len(s)):
            return s
        return s[:i-1:-1] + self.shortestPalindrome2PointersRecursion(s[:i]) + s[i:]

    def shortestPalindromeKMP(self, s):
        s_new = s + '#' + s[::-1]
        n_table = [0 for _ in range(len(s_new))]
        for i in range(1, len(s_new)):
            v = n_table[i-1]
            while (v > 0) and (s_new[i] != s_new[v]):
                v = n_table[v-1]
            if (s_new[i] == s_new[v]):
                v += 1
            n_table[i] = v
        return (s[:n_table[-1]-1:-1] + s)

# debug
s = Solution()
print s.shortestPalindrome("aacecaaa")
print s.shortestPalindrome("abcd")
print s.shortestPalindrome("")
