class Solution(object):
    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """

        if None == s:
            return None == p
        elif None == p:
            return False
        if 0 == len(p):
            return 0 == len(s)
        return self.checkDp(s, p)

    def checkDp(self, s, p):
        table_dp = [[False for j in xrange(len(p)+1)] for i in xrange(len(s)+1)]
        table_dp[0][0] = True
        for j in xrange(len(p)):
            table_dp[0][j+1] = ('*' == p[j] and table_dp[0][j])
        for i in xrange(len(s)):
            for j in xrange(len(p)):
                if '?' == p[j] or s[i] == p[j]:
                    table_dp[i+1][j+1] = table_dp[i][j]
                elif '*' == p[j]:
                    table_dp[i+1][j+1] = table_dp[i+1][j] or table_dp[i][j+1]

        return table_dp[len(s)][len(p)]

# debug
s = Solution()
print s.isMatch("aa", "a")
print s.isMatch("aa", "*")
print s.isMatch("cb", "?a")
print s.isMatch("adceb", "*a*b")
print s.isMatch("acdcb", "a*c?b")
print s.isMatch("", "*")
