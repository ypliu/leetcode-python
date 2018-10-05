class Solution(object):
    def exist(self, board, word):
        """
        :type board: List[List[str]]
        :type word: str
        :rtype: bool
        """

        if not board or 0 == len(board) or 0 == len(board[0]) or len(word) > len(board)*len(board[0]):
            return False
        elif not word or 0 == len(word):
            return True
        for r in range(len(board)):
            for l in range(len(board[r])):
                if self.dfs(board, r, l, word, 0):
                    return True
        return False

    def dfs(self, board, row, col, word, i):
        if i == len(word):
            return True
        if row < 0 or row >= len(board) or col < 0 or col >= len(board[row]) or board[row][col] != word[i]:
            return False
        next_position = [ [-1,0], [1,0], [0,-1],[0,1] ]
        board[row][col] = None
        for j in range(4):
            if self.dfs(board, row+next_position[j][0], col+next_position[j][1], word, i+1):
                board[row][col] = word[i]
                return True
        board[row][col] = word[i]
        return False

# debug
s = Solution()
board = [ ['A','B','C','E'], ['S','F','C','S'], ['A','D','E','E'] ]
print s.exist(board, "ABCCED")
print s.exist(board, "SEE")
print s.exist(board, "ABCB")
