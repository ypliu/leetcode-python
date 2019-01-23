class Solution(object):
    def addOperators(self, num, target):
        """
        :type num: str
        :type target: int
        :rtype: List[str]
        """

        if (not num) or (len(num) == 0):
            return []
        elif (str(target) == num):
            return [num]
        len_num = len(num); ord_0 = ord('0')
        res = []
        def dfs(index, val_cur, operand_last, sol):
            if (index == len(num)):
                if (val_cur == target):
                    res.append(sol)
                return
            ub = len_num if ('0' != num[index]) else (index+1)
            n = 0
            for i in range(index, ub):
                n = n * 10 + ord(num[i]) - ord_0
                if (0 == index):
                    dfs(i+1, n, n, num[:i+1])
                else:
                    str_n = num[index:i+1]
                    operand_next = operand_last * n
                    dfs(i + 1, val_cur + n, n, sol + '+' + str_n)
                    dfs(i + 1, val_cur - n, -n, sol + '-' + str_n)
                    dfs(i + 1, val_cur - operand_last + operand_next, operand_next, sol + '*' + str_n)
        dfs(0, 0, 0, "")
        return res

# debug
s = Solution()
print s.addOperators("123", 6)
print s.addOperators("232", 8)
print s.addOperators("105", 5)
print s.addOperators("00", 0)
