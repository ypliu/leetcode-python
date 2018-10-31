class Solution(object):
    def ladderLength(self, beginWord, endWord, wordList):
        """
        :type beginWord: str
        :type endWord: str
        :type wordList: List[str]
        :rtype: int
        """

        wordList = set(wordList)
        layer_cur = set([beginWord])
        res = 0

        while layer_cur:
            res += 1
            layer_next = set()
            for word in layer_cur:
                if word == endWord:
                    return res
                else:
                    for i in range(len(word)):
                        for ch in 'abcdefghijklmnopqrstuvwxyz':
                            word_changed = word[:i] + ch + word[i+1:]
                            if word_changed in wordList:
                                layer_next.add(word_changed)
                                wordList.discard(word_changed)
            layer_cur = layer_next

        return 0

# debug
s = Solution()
print s.ladderLength("hit", "cog", ["hot","dot","dog","lot","log","cog"])
print s.ladderLength("hit", "cog", ["hot","dot","dog","lot","log"])
print s.ladderLength("red", "tax", ["ted","tex","red","tax","tad","den","rex","pee"])
