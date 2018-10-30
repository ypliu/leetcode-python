import collections
class Solution(object):
    def findLadders(self, beginWord, endWord, wordList):
        """
        :type beginWord: str
        :type endWord: str
        :type wordList: List[str]
        :rtype: List[List[str]]
        """

        wordList = set(wordList)
        res = []
        layer_cur = {}
        layer_cur[beginWord] = [[beginWord]]
        not_found = True

        while layer_cur and not_found:
            layer_next = collections.defaultdict(list)
            for word in layer_cur:
                if word == endWord:
                    res.extend(layer_cur[word])
                    not_found = False
                else:
                    for i in range(len(word)):
                        for ch in 'abcdefghijklmnopqrstuvwxyz':
                            word_changed = word[:i] + ch + word[i+1:]
                            if word_changed in wordList:
                                layer_next[word_changed] += [path+[word_changed] for path in layer_cur[word]]
            wordList -= set(layer_next.keys())
            layer_cur = layer_next

        return res

# debug
s = Solution()
print s.findLadders("hit", "cog", ["hot","dot","dog","lot","log","cog"])
print s.findLadders("hit", "cog", ["hot","dot","dog","lot","log"])
print s.findLadders("red", "tax", ["ted","tex","red","tax","tad","den","rex","pee"])
