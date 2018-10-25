class Solution(object):
    def numDistinct(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: int
        """

        if not t:
            return 1
        elif len(s) < len(t):
            return 0
        elif len(s) == len(t):
            num = 1 if s == t else 0
            return num
        #return self.numDistinctDFS(s, 0, t, 0)
        return self.numDistinctDp(s, t)

    def numDistinctDFS(self, s, i, t, j):
        if j == len(t):
            return 1
        elif i >= len(s):
            return 0
        remainder_s = len(s) - i; remainder_t = len(t) - j
        if remainder_s < remainder_t:
            return 0
        elif remainder_s == remainder_t:
            num = 1 if s[i:] == t[j:] else 0
            return num
        res = self.numDistinctDFS(s, i+1, t, j)
        if s[i] == t[j]:
            res += self.numDistinctDFS(s, i+1, t, j+1)
        return res

    def numDistinctDp(self, s, t):
        dp_table = [0 for j in range(len(t)+1)]
        dp_table[0] = 1
        for i in range(len(s)):
            for j in range(len(t)-1, -1, -1):
                if s[i] == t[j]:
                    dp_table[j+1] += dp_table[j]
        return dp_table[-1]

# debug
s = Solution()
print s.numDistinct("rabbbit", "rabbit")
print s.numDistinct("babgbag", "bag")
