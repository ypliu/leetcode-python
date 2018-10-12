class Solution(object):
    def numDecodings(self, s):
        """
        :type s: str
        :rtype: int
        """

        if not s or 0 == len(s) or '0' == s[0]:
            return 0
        elif 1 == len(s):
            return 1
        #return self.dpLinearSpace(s)
        return self.dpConstSpace(s)

    def dpLinearSpace(self, s):
        n = len(s)
        dp = [0 for i in xrange(n+1)]
        dp[n] = 1
        if s[n-1] != '0':
            dp[n-1] = 1
        for i in xrange(n-2, -1, -1):
            if '0' == s[i]:
                continue
            val = (ord(s[i]) - ord('0')) * 10 + (ord(s[i+1]) - ord('0'))
            if val <= 26:
                dp[i] = dp[i+1] + dp[i+2]
            else:
                dp[i] = dp[i+1]
        return dp[0]

    def dpConstSpace(self, s):
        last2 = 1
        last1 = 1 if s[-1] != '0' else 0
        for i in xrange(len(s)-2, -1, -1):
            if '0' == s[i]:
                res = 0
            else:
                val = (ord(s[i]) - ord('0')) * 10 + (ord(s[i+1]) - ord('0'))
                if val <= 26:
                    res = last1 + last2
                else:
                    res = last1
            last2 = last1
            last1 = res
        return res

# debug
s = Solution()
print s.numDecodings("12")
print s.numDecodings("226")
