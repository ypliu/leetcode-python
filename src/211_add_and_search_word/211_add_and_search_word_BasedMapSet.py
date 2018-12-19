class WordDictionary(object):
    def __init__(self):
        """
        Initialize your data structure here.
        """
        import collections
        self.map_length2words = collections.defaultdict(set)

    def addWord(self, word):
        """
        Adds a word into the data structure.
        :type word: str
        :rtype: void
        """
        self.map_length2words[len(word)].add(word)

    def search(self, word):
        """
        Returns if the word is in the data structure. A word could contain the dot character '.' to represent any one letter.
        :type word: str
        :rtype: bool
        """
        if not word:
            return None
        elif (len(word) not in self.map_length2words):
            return False
        words = self.map_length2words[len(word)]
        if ('.' not in word):
            return (word in words)
        for i,ch in enumerate(word):
            if ('.' != ch):
                words = {w for w in words if (w[i] == ch)}
                if (0 == len(words)):
                    return False
        return True

# debug
# Your WordDictionary object will be instantiated and called as such:
obj = WordDictionary()
obj.addWord("a")
obj.addWord("ab")
print obj.search("a")
print obj.search("a.")
print obj.search("ab")
print obj.search(".a")
print obj.search(".a")
print obj.search(".b")
print obj.search("ab.")
print obj.search(".")
print obj.search("..")
