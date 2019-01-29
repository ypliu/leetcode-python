class Solution(object):
    def gameOfLife(self, board):
        """
        :type board: List[List[int]]
        :rtype: void Do not return anything, modify board in-place instead.
        """

        if (not board) or (len(board) == 0) or (len(board[0]) == 0):
            return
        neighbors = [(-1,-1), (0,-1), (1,-1), (1,0), (1,1), (0,1), (-1,1), (-1,0)]
        m,n = len(board),len(board[0])
        for i in range(m):
            for j in range(n):
                count_live = 0
                for x,y in neighbors:
                    ii,jj = i+x,j+y
                    if (0 <= ii < m) and (0 <= jj < n):
                        count_live += board[ii][jj] & 1
                if (3 == count_live) or (board[i][j]+count_live == 3):
                    board[i][j] |= 2
        for i in range(m):
            for j in range(n):
                board[i][j] >>= 1

# debug
s = Solution()
board = [ [0,1,0], [0,0,1], [1,1,1], [0,0,0] ]
s.gameOfLife(board)
print board
