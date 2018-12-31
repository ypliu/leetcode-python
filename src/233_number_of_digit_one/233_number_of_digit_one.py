class Solution(object):
    def countDigitOne(self, n):
        """
        :type n: int
        :rtype: int
        """

        if (not n) or (n < 1):
            return 0
        counts = 0; digit = 1
        while (digit <= n):
            quotient = n // digit
            n_digit = quotient % 10
            counts += (quotient // 10) * digit
            if (n_digit > 1):
                counts += digit
            elif (n_digit > 0):
                counts += n % digit + 1
            digit *= 10
        return counts

# debug
s = Solution()
print s.countDigitOne(13)
print s.countDigitOne(213)
print s.countDigitOne(333)
