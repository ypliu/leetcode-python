class Solution(object):
    def calculate(self, s):
        """
        :type s: str
        :rtype: int
        """

        def eval(n1, n2, op):
            if ('+' == op):
                return (n1 + n2)
            if ('-' == op):
                return (n1 - n2)
            if ('*' == op):
                return (n1 * n2)
            if ('/' == op):
                return (n1 / n2)

        stack = []; n = 0
        for ch in (s+'+'):
            if (' ' == ch):
                continue
            elif ('0' <= ch <= '9'):
                n = n * 10 + ord(ch) - ord('0')
            elif ('*' == ch) or ('/' == ch):
                if (len(stack) >= 2) and (stack[-1] in "*/"):
                    op = stack.pop()
                    n1 = stack.pop()
                    n = eval(n1, n, op)
                stack.append(n)
                stack.append(ch)
                n = 0
            elif ('+' == ch) or ('-' == ch):
                while (len(stack) >= 2) and ('(' != stack[-1]):
                    op = stack.pop()
                    n1 = stack.pop()
                    n = eval(n1, n, op)
                stack.append(n)
                stack.append(ch)
                n = 0
            elif ('(' == ch):
                stack.append(ch)
            elif (')' == ch):
                while (len(stack) >= 2) and ('(' != stack[-1]):
                    op = stack.pop()
                    n1 = stack.pop()
                    n = eval(n1, n, op)
                stack.pop()
            else:
                print "Error! Fake char:", ch
        return stack[0]

# debug
s = Solution()
print s.calculate("3+2*2")
print s.calculate(" 2-1 + 2")
print s.calculate("(1+(4+5+2)-3)+(6+8)")
print s.calculate("(1+(4+5+2)-3)+(6+8*(1+10))")
