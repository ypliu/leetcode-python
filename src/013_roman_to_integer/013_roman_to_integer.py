class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """

        high_priority = {'IV':4, 'IX':9, 'XL':40, 'XC':90, 'CD':400, 'CM':900}
        low_priority = {'I':1, 'V':5, 'X':10, 'L':50, 'C':100, 'D':500, 'M':1000}
        res = 0
        i, nchar = 0, len(s)

        # Firstly convert the string s to uppercase if necessarys
        while i < nchar:
            fist_2ch = s[i:i+2]
            if fist_2ch in high_priority:
                res += high_priority[fist_2ch]
                i += 2
            else:
                res += low_priority[s[i]]
                i += 1

        return res

#
s = Solution()
print s.romanToInt("MCMXCIV")
