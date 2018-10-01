class Solution(object):
    def minDistance(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: int
        """

        if not word1 or not word2:
            return len(word1)+len(word2)

        len1 = len(word1) + 1
        len2 = len(word2) + 1
        dp_table = [[0 for j in xrange(len2)] for i in xrange(len1)]
        for i in xrange(1, len1):
            dp_table[i][0] = i
        for j in xrange(1, len2):
            dp_table[0][j] = j
        for i in xrange(len(word1)):
            ch1 = word1[i]
            for j in xrange(len(word2)):
                if ch1 == word2[j]:
                    dp_table[i+1][j+1] = dp_table[i][j]
                else:
                    dp_table[i+1][j+1] = min(dp_table[i][j+1], dp_table[i+1][j], dp_table[i][j]) + 1
        return dp_table[len(word1)][len(word2)]

# debug
s = Solution()
print s.minDistance("horse", "ros")
print s.minDistance("intention", "execution")
