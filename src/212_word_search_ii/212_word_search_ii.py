class Trie(object):
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.root = {}

    def insert(self, word):
        """
        Inserts a word into the trie.
        :type word: str
        :rtype: void
        """
        node = self.root
        for ch in word:
            if (ch not in node):
                node[ch] = {}
            node = node[ch]
        node['$'] = word

    def search(self, word):
        """
        Returns if the word is in the trie.
        :type word: str
        :rtype: bool
        """
        node = self.root
        for ch in word:
            if (ch not in node):
                return False
            node = node[ch]
        return ('$' in node)

    def startsAtRowCol(self, board, rth, cth, res):
        """
        Returns if there is any word in the trie that starts at rth row and cth column of board.
        :type prefix: array of characters, row and column of location, result
        :rtype: void
        """
        n_r,n_c = len(board),len(board[0])
        directions = [[-1,0], [1,0], [0,-1], [0,1]]
        ch = board[rth][cth]; board[rth][cth] = '#'
        stack = [[rth, cth, ch, self.root[ch], 0]]
        while stack:
            prev = stack[-1]
            if (prev[4] >= 4):
                board[prev[0]][prev[1]] = prev[2]
                stack.pop()
                continue
            r,c,node = prev[0]+directions[prev[4]][0],prev[1]+directions[prev[4]][1],prev[3]
            stack[-1][4] += 1
            if (0 <= r < n_r) and (0 <= c < n_c) and (board[r][c] != '#'):
                ch = board[r][c]
                if (ch not in node):
                    continue
                board[r][c] = '#'
                node = node[ch]
                stack.append([r, c, ch, node, 0])
                if ('$' in node):
                    res.add(node['$'])

class Solution(object):
    def findWords(self, board, words):
        """
        :type board: List[List[str]]
        :type words: List[str]
        :rtype: List[str]
        """

        if (not board) or (len(board) < 1) or (len(board[0]) < 1) or (not words) or (len(words) < 1):
            return []
        board_trie = Trie()
        for w in words:
            board_trie.insert(w)
        initials_set = set(w[0] for w in words)
        res = set()
        for i in range(len(board)):
            for j in range(len(board[i])):
                if (board[i][j] not in initials_set):
                    continue
                elif (board[i][j] in words):
                    res.add(board[i][j])
                    continue
                board_trie.startsAtRowCol(board, i, j, res)
        return list(res)

# debug
s = Solution()
print s.findWords([ ['o','a','a','n'], ['e','t','a','e'], ['i','h','k','r'], ['i','f','l','v'] ], ["oath","pea","eat","rain"])
