class Solution(object):
    def minCut(self, s):
        """
        :type s: str
        :rtype: int
        """

        if not s or len(s) <= 1:
            return 0
        return self.minCutDp(s)

    def minCutDp(self, s):
        if s == s[::-1]: return 0
        for i in range(1, len(s)):
            if s[:i] == s[:i][::-1] and s[i:] == s[i:][::-1]:
                return 1
        # DP
        cut = [n for n in range(-1,len(s))]
        for i in range(len(s)):
            r1, r2 = 0, 0
            # odd
            while i-r1 >= 0 and i+r1 < len(s) and s[i-r1] == s[i+r1]:
                cut[i+r1+1] = min(cut[i+r1+1], cut[i-r1]+1)
                r1 += 1
            # even
            while i-r2 >= 0 and i+r2+1 < len(s) and s[i-r2] == s[i+r2+1]:
                cut[i+r2+2] = min(cut[i+r2+2], cut[i-r2]+1)
                r2 += 1
        return cut[-1]

# debug
s = Solution()
print s.minCut("aab")
print s.minCut("abcba")
print s.minCut("cabababcbc")
