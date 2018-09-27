class Solution(object):
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """

        # return bin(int(a,2)+int(b,2))[2:]
        if not a or 0 == len(a) or "0" == a:
            return b
        elif not b or 0 == len(b) or "0" == b:
            return a

        addend_1 = 0
        for ch in a:
            addend_1 <<= 1
            if '1' == ch:
                addend_1 += 1
            elif '0' != ch:
                print 'Illegal value of a: ', a
                return
        addend_2 = 0
        for ch in b:
            addend_2 <<= 1
            if '1' == ch:
                addend_2 += 1
            elif '0' != ch:
                print 'Illegal value of b: ', b
                return
        sum = addend_1 + addend_2; res = ""
        while sum > 0:
            res += str(sum & 1)
            sum >>= 1
        return res[::-1]

# debug
s = Solution()
print s.addBinary("11", "1")
print s.addBinary("1010", "1011")
print s.addBinary("", "10")
