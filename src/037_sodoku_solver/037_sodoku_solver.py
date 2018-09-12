class Solution(object):
    def solveSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: void Do not return anything, modify board in-place instead.
        """

        row = set()
        col = set()
        box = set()
        blanks = []

        for i in range(9):
            for j in range(9):
                ch = board[i][j]
                if '.' == ch:
                    blanks.append((i,j))
                elif ch >= '1' and ch <= '9':
                    seq = (i // 3) * 3 + (j // 3)
                    row.add((i, ch))
                    col.add((j, ch))
                    box.add((seq, ch))
                else:
                    print 'Error, invalid character: %d, %d!' %(i,j)
                    return

        if not self.fillBlanksDfs(board, row, col, box, blanks, 0):
            print "No Solution!!!"

    def fillBlanksDfs(self, board, row, col, box, blanks, ith):
        if len(blanks) <= ith:
            return True

        (i, j) = blanks[ith]
        seq = (i // 3) * 3 + (j // 3)
        nums_string = '123456789'
        for ch in nums_string:
            if (i, ch) in row or (j, ch) in col or (seq, ch) in box:
                continue
            board[i][j] = ch
            row.add((i, ch))
            col.add((j, ch))
            box.add((seq, ch))
            if self.fillBlanksDfs(board, row, col, box, blanks, ith+1):
                return True
            # board[i][j] = '.'
            row.remove((i, ch))
            col.remove((j, ch))
            box.remove((seq, ch))
        return False

#debug
s = Solution()
board = [["5","3",".",".","7",".",".",".","."],["6",".",".","1","9","5",".",".","."],[".","9","8",".",".",".",".","6","."],["8",".",".",".","6",".",".",".","3"],["4",".",".","8",".","3",".",".","1"],["7",".",".",".","2",".",".",".","6"],[".","6",".",".",".",".","2","8","."],[".",".",".","4","1","9",".",".","5"],[".",".",".",".","8",".",".","7","9"]]
s.solveSudoku(board)
print board
