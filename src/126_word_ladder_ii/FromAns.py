from collections import defaultdict
import string
class Solution:
    def findLadders(self, beginWord, endWord, wordList):
        """
        :type beginWord: str
        :type endWord: str
        :type wordList: List[str]
        :rtype: List[List[str]]
        """
        if endWord not in wordList or not endWord or not beginWord:
            return []
        word_list = set(wordList)
        forward, backward = {beginWord}, {endWord}
        direction = 1
        parents = defaultdict(set)
        while forward and backward:
            if len(forward) > len(backward):
                forward, backward = backward, forward
                direction *= -1

            foward_next = set()
            word_list -= forward
            for word in forward:
                for i in range(len(word)):
                    first, second = word[:i], word[i+1:]
                    for ch in string.ascii_lowercase:
                        combined_word = first + ch + second
                        if combined_word in word_list:
                            foward_next.add(combined_word)
                            if direction == 1:
                                parents[combined_word].add(word)
                            else:
                                parents[word].add(combined_word)

            if foward_next & backward:
                results = [[endWord]]
                while results[0][0] != beginWord:
                    results = [ [parent] + result for result in results for parent in parents[result[0]] ]
                return results
            forward = foward_next
        return []
