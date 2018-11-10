class Solution(object):
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: List[str]
        """

        return self.wordBreakRecursionWithMemo(s, wordDict)
        #TLE return self.wordBreakBfs(s, wordDict)

    def wordBreakRecursionWithMemo(self, s, wordDict):
        def sentencesFromIToEnd(i):
            if i not in sols_i_to_end:
                sols = []
                for j in range(i+1, len(s)+1):
                    w = s[i:j]
                    if w in words_set:
                        for tail in sentencesFromIToEnd(j):
                            sols += [w + (tail and ' ' + tail)]
                sols_i_to_end[i] = sols
            return sols_i_to_end[i]
        words_set = set(wordDict)
        sols_i_to_end = {len(s): ['']}
        return sentencesFromIToEnd(0)

    def wordBreakBfs(self, s, wordDict):
        words_set = set(wordDict)
        initials_set = set(w[0] for w in wordDict)
        lengths_set = set(len(w) for w in wordDict)

        res = []
        queue = [ ([], 0) ]
        while queue:
            queue_temp = []
            for comb_words,i in queue:
                if s[i] not in initials_set:
                    continue
                for l in lengths_set:
                    i2 = i + l
                    w = s[i:i2]
                    if (i2 <= len(s)) and (w in words_set):
                        if len(s) == i2:
                            res.append(comb_words+[w])
                        else:
                            queue_temp.append((comb_words+[w], i2))
            queue = queue_temp
        for i in range(len(res)):
            res[i] = ' '.join(res[i])
        return res

# debug
s = Solution()
print s.wordBreak("catsanddog", ["cat", "cats", "and", "sand", "dog"])
print s.wordBreak("pineapplepenapple", ["apple", "pen", "applepen", "pine", "pineapple"])
print s.wordBreak("catsandog", ["cats", "dog", "sand", "and", "cat"])
print s.wordBreak("aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaabaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa", ["a","aa","aaa","aaaa","aaaaa","aaaaaa","aaaaaaa","aaaaaaaa","aaaaaaaaa","aaaaaaaaaa"])
