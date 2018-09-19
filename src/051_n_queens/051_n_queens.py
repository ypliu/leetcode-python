class Solution(object):
    def solveNQueens(self, n):
        """
        :type n: int
        :rtype: List[List[str]]
        """

        if 0 == n:
            return []
        res = []
        self.dfs(n, [], [], [], res)
        return res

    def dfs(self, num_queens, col_occupied, diag_sub_occupied, diag_add_occupied, res):
        row_th = len(col_occupied)
        if num_queens == row_th:
            sol = ['.'*col_th + 'Q' + '.'*(num_queens-1-col_th) for col_th in col_occupied]
            res.append(sol)
            return

        for col_th in range(num_queens):
            rc_sub, rc_add = row_th - col_th, row_th + col_th
            if (col_th in col_occupied) or (rc_sub in diag_sub_occupied) or (rc_add in diag_add_occupied):
                continue
            self.dfs(num_queens, col_occupied+[col_th], diag_sub_occupied+[rc_sub], diag_add_occupied+[rc_add], res)

# debug
s = Solution()
print s.solveNQueens(4)
