class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """

        rmost = len(s) - 1
        maxlen = 1
        indx = 0

        for i in range(0, rmost):
            # centre exclude and include s[i] for j=0,1, that is, # of palindromic substring is even or odd
            for j in range(2):
                l, r = i - j, i + 1
                while l >= 0 and r <= rmost and s[l] == s[r]:
                    l -= 1; r += 1
                curlen = r - l - 1
                if curlen > maxlen:
                    maxlen = curlen
                    indx = l + 1

        return s[indx : indx + maxlen]
#
print Solution().longestPalindrome('babad')
