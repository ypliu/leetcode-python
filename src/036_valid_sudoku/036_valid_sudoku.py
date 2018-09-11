class Solution(object):
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """

        row = set()
        col = set()
        box = set()

        for i in xrange(0,9):
            for j in xrange(0,9):
                ch = board[i][j]
                if '.' == ch:
                    continue
                elif ch >= '1' and ch <= '9':
                    seq = (i // 3) * 3 + (j // 3)
                    if (i, ch) in row or (j, ch) in col or (seq, ch) in box:
                        return False
                    row.add((i, ch))
                    col.add((j, ch))
                    box.add((seq, ch))
                else:
                    print 'Error, invalid character: %d, %d!' %(i,j)
                    return False

        return True

# debug
s = Solution()
board = [["5","3",".",".","7",".",".",".","."],["6",".",".","1","9","5",".",".","."],[".","9","8",".",".",".",".","6","."],["8",".",".",".","6",".",".",".","3"],["4",".",".","8",".","3",".",".","1"],["7",".",".",".","2",".",".",".","6"],[".","6",".",".",".",".","2","8","."],[".",".",".","4","1","9",".",".","5"],[".",".",".",".","8",".",".","7","9"]]
print s.isValidSudoku(board)
