class Solution(object):
    def fractionToDecimal(self, numerator, denominator):
        """
        :type numerator: int
        :type denominator: int
        :rtype: str
        """

        if 0 == numerator:
            return "0"
        res = "-" if ((numerator < 0) ^ (denominator < 0)) else ""
        n,d = abs(numerator),abs(denominator)
        res += str(n // d)
        r = n % d
        if 0 == r:
            return res
        res += '.'
        dict_r = {}
        while r != 0:
            if r in dict_r:
                res = res[:dict_r[r]] + '(' + res[dict_r[r]:] + ')'
                break
            dict_r[r] = len(res)
            r *= 10
            res += str(r // d)
            r %= d
        return res

# debug
s = Solution()
print s.fractionToDecimal(1,2)
print s.fractionToDecimal(2,1)
print s.fractionToDecimal(2,3)
