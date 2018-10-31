class Solution(object):
    def ladderLength(self, beginWord, endWord, wordList):
        """
        :type beginWord: str
        :type endWord: str
        :type wordList: List[str]
        :rtype: int
        """

        # bi-directional bfs
        word_list = set(wordList)
        if endWord not in word_list:
            return 0

        word_list.remove(endWord)
        forward, backward = set([beginWord]), set([endWord])
        step = 1
        while len(forward) > 0 and len(backward) > 0:
            step += 1
            if len(forward) > len(backward):
                forward, backward = backward, forward

            forward_next = set()
            for s in forward:
                for i in range(len(s)):
                    for ch in "abcdefghijklmnopqrstuvwxyz":
                        temp = s[:i]+ch+s[i+1:]
                        if temp in backward:
                            return step
                        elif temp in word_list:
                            word_list.remove(temp)
                            forward_next.add(temp)
            forward = forward_next
        
        return 0
