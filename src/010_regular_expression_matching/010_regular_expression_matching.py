class Solution(object):
    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """

        # 1. just only 1 line if using re lib
        # return re.match('^'+p+'$', s) != None

        # 2. using DP
        # dp[i][j] record whether or not s[0:i+1] and p[0:j+1] match
        # NOTE: dp[0][*] is necessary, e.g. dp[0][2n]=True if p[0:2n] equals ".*" or "a*" or "b*c*" ...

        if not p:
            return not s

        len_s = len(s) + 1
        len_p = len(p) + 1
        dp = [[False] * (len_p) for _ in range(len_s)]
        dp[0][0] = True
        dp[0][1] = False
        for i in range(1, len_s):
            dp[i][0] = False
        for j in range(2, len_p):
            dp[0][j] = p[j-1] == '*' and dp[0][j-2]

        for i in range(len(s)):
            for j in range(len(p)):
                if p[j] == s[i] or p[j] == '.':
                    dp[i+1][j+1] = dp[i][j]
                elif p[j] == '*':
                    # for current 2 characters '-*': ignoring wildcard-matching or first matching or N(>2)th matching or matching any characters cased by '.*'
                    dp[i+1][j+1] = dp[i+1][j-1] or dp[i+1][j] or (s[i] == s[i-1] and s[i] == p[j-1] and dp[i][j+1]) or ('.' == p[j-1] and dp[i][j+1])

        return dp[-1][-1]

#
s = Solution()
print s.isMatch("aab", "c*a*b")
