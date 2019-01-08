class Solution(object):
    def diffWaysToCompute(self, input):
        """
        :type input: str
        :rtype: List[int]
        """

        if (not input):
            return []
        ord_0,ord_9 = ord('0'),ord('9'); n = 0
        arr_num,arr_op = [],[]
        for ch in input:
            ord_ch = ord(ch)
            if (ord_0 <= ord_ch <= ord_9):
                n = n * 10 + ord_ch - ord_0
            elif (ch in ['+','-','*']):
                arr_num.append(n)
                n = 0
                arr_op.append(ch)
            else:
                print "Error! Invalid char:", ch
        arr_num.append(n)
        dp_t = [[None for j in range(len(arr_num))] for i in range(len(arr_num))]
        for r in range(len(arr_num)):
            dp_t[r][r] = [arr_num[r]]
        # compute the i-th layer of diagonal of dp_t[][]
        for i in range(1, len(arr_num)):
            for r in range(len(arr_num)-i):
                c = r + i
                dp_t[r][c] = []
                # Catalan Number corresponding to the number of operators
                for k in range(r,c):
                    op = arr_op[k]
                    dp_t[r][c] += [self.compute(n1, n2, op) for n1 in dp_t[r][k] for n2 in dp_t[k+1][c]]
        return dp_t[0][-1]

    def compute(self, n1, n2, op):
        if ('+' == op):
            return (n1 + n2)
        elif ('-' == op):
            return (n1 - n2)
        elif ('*' == op):
            return (n1 * n2)

# debug
s = Solution()
print s.diffWaysToCompute("2-1-1")
print s.diffWaysToCompute("2*3-4*5")
