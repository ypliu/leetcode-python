class Solution(object):
    def solve(self, board):
        """
        :type board: List[List[str]]
        :rtype: void Do not return anything, modify board in-place instead.
        """

        if not board or 0 == len(board) or 0 == len(board[0]):
            return
        for i in range(len(board)):
            self.solveDfs(board, i, 0)
            self.solveDfs(board, i, len(board[0])-1)
        for j in range(len(board[0])):
            self.solveDfs(board, 0, j)
            self.solveDfs(board, len(board)-1, j)
        for i in range(len(board)):
            for j in range(len(board[0])):
                if 'T' == board[i][j]:
                    board[i][j] = 'O'
                else:
                    board[i][j] = 'X'

    def solveDfs(self, board, i, j):
        if i < 0 or i >= len(board) or j < 0 or j >= len(board[0]):
            return
        if 'T' == board[i][j] or 'X' == board[i][j]:
            return
        board[i][j] = 'T'
        self.solveDfs(board, i-1, j)
        self.solveDfs(board, i+1, j)
        self.solveDfs(board, i, j-1)
        self.solveDfs(board, i, j+1)

# debug
board = [ ['X', 'X', 'X', 'X'], ['X', 'O', 'O', 'X'], ['X', 'X', 'O', 'X'], ['X', 'O', 'X', 'X'] ]
print board
s = Solution()
s.solve(board)
print board
