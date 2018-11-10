class Solution(object):
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: bool
        """

        wordDict = set(wordDict)
        segmented_lt_i = [False for i in range(len(s)+1)]; segmented_lt_i[0] = [True]
        for i in range(1, len(s)+1):
            for j in range(i):
                if segmented_lt_i[j] and (s[j:i] in wordDict):
                    segmented_lt_i[i] = True
                    break
        return segmented_lt_i[-1]

# debug
s = Solution()
print s.wordBreak("leetcode", ["leet", "code"])
print s.wordBreak("applepenapple", ["apple", "pen"])
print s.wordBreak("catsandog", ["cats", "dog", "sand", "and", "cat"])
