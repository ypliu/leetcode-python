class Solution(object):
    def myAtoi(self, str):
        """
        :type str: str
        :rtype: int
        """

        if not str:
            return 0
        str = str.lstrip()

        MAX_INT = 2147483647
        ABS_MIN_INT = 2147483648
        res = 0
        start = 0
        nchar = len(str)
        if nchar == 0:
            return 0

        minus = False
        if str[0] == '+':
            start = 1
        elif str[0] == '-':
            start = 1
            minus = True

        for i in range(start, nchar):
            temp = ord(str[i]) - ord('0')
            if temp > 9 or temp < 0:
                break
            res = res * 10 + temp

            if minus:
                if res >= ABS_MIN_INT:
                    return -1 * ABS_MIN_INT
            else:
                if res >= MAX_INT:
                    return MAX_INT
        if minus:
            res = -res
        return res

# debug
s = Solution()
print s.myAtoi(' -6ab 1324')
