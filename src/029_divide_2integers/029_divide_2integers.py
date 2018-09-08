class Solution(object):
    def divide(self, dividend, divisor):
        """
        :type dividend: int
        :type divisor: int
        :rtype: int
        """

        sign = (dividend < 0 and divisor > 0) or (dividend > 0 and divisor < 0)
        abs_dividend, abs_divisor = abs(dividend), abs(divisor)
        if abs_dividend < abs_divisor:
            return 0

        # With the help of shifting, it is equivalent to fetch quotient the in binary format
        base = abs_divisor << 1
        factor = 2
        while abs_dividend >= base:
            base <<= 1
            factor <<= 1
        res = 0
        while abs_dividend >= abs_divisor:
            base >>= 1
            factor >>= 1
            if abs_dividend >= base:
                res += factor
                abs_dividend -= base
        if sign:
            res = -res

        return min(max(-2147483648, res), 2147483647)

# debug
s = Solution()
print s.divide(10, 3)
