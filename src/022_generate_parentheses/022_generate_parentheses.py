class Solution(object):
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """

        res = []
        if n > 0:
            self.generate_dfs(n, n, "", res)
        return res

    def generate_dfs(self, num_left, num_right, cur_comb, res):
        if num_left == 0:
            cur_comb += ")" * num_right
            res.append(cur_comb)
            return
        self.generate_dfs(num_left-1, num_right, cur_comb+"(", res)
        if num_left < num_right:
            self.generate_dfs(num_left, num_right-1, cur_comb+")", res)

# debug

s = Solution()
print s.generateParenthesis(3)
