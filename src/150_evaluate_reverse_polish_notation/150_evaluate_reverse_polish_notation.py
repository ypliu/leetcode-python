class Solution(object):
    def evalRPN(self, tokens):
        """
        :type tokens: List[str]
        :rtype: int
        """

        if not tokens:
            return
        rpn_stack = []
        operators = set(['+', '-', '*', '/'])
        for str in tokens:
            if str in operators:
                operand2 = rpn_stack.pop()
                operand1 = rpn_stack.pop()
                if "+" == str:
                    res = operand1 + operand2
                elif "-" == str:
                    res = operand1 - operand2
                elif "*" == str:
                    res = operand1 * operand2
                elif "/" == str:
                    res = (int)((float)(operand1) / operand2)
            else:
                res = self.strToI(str)
            rpn_stack.append(res)
        return rpn_stack[-1]

    def strToI(self, s):
        res = 0
        if '-' == s[0]:
            sign = -1
            start = 1
        elif '+' == s[0]:
            sign = 1
            start = 1
        else:
            sign = 1
            start = 0
        for i in range(start, len(s)):
            res = res * 10 + ord(s[i]) - ord('0')
        return (sign * res)

# debug
s = Solution()
print s.evalRPN(["2", "1", "+", "3", "*"])
print s.evalRPN(["4", "13", "5", "/", "+"])
print s.evalRPN(["10", "6", "9", "3", "+", "-11", "*", "/", "*", "17", "+", "5", "+"])
