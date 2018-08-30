class Solution(object):
    def intToRoman(self, num):
        """
        :type num: int
        :rtype: str
        """

        bases = (('I',1), ('IV',4), ('V',5), ('IX',9), ('X',10), ('XL',40), ('L',50), ('XC',90), ('C',100), ('CD',400), ('D',500), ('CM',900), ('M',1000))
        res = ''

        for itor in range(len(bases)-1, -1 ,-1):
            base = bases[itor][1]
            if num < base:
                continue
            nchar = num / base
            res += bases[itor][0] * nchar
            num %= base

        return res

#
s = Solution()
print s.intToRoman(1994)
