class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_word = False

class WordDictionary(object):
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.root = TrieNode()

    def addWord(self, word):
        """
        Adds a word into the data structure.
        :type word: str
        :rtype: void
        """
        node = self.root
        for ch in word:
            if (ch not in node.children):
                node.children[ch] = TrieNode()
            node = node.children[ch]
        node.is_word = True

    def search(self, word):
        """
        Returns if the word is in the data structure. A word could contain the dot character '.' to represent any one letter.
        :type word: str
        :rtype: bool
        """
        def searchDfs(word, ith, node):
            if (ith == len(word)):
                return node.is_word
            ch = word[ith]
            if ('.' != ch):
                if (ch not in node.children):
                    return False
                return searchDfs(word, ith+1, node.children[ch])
            else:
                for it in node.children:
                    if searchDfs(word, ith+1, node.children[it]):
                        return True
                return False
        return searchDfs(word, 0, self.root)

# debug
# Your WordDictionary object will be instantiated and called as such:
obj = WordDictionary()
obj.addWord("bad")
obj.addWord("dad")
obj.addWord("mad")
print obj.search("pad")
print obj.search("bad")
print obj.search(".ad")
print obj.search("b..")
