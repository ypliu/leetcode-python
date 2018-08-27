class Solution(object):
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """

        step = numRows * 2 - 2
        subincrement = step
        lastrow = numRows - 1
        numchr = len(s)
        res = ""

        if numRows == 1:
            return s

        res = s[::step] # 1st row
        for i in range(1, lastrow):
            subincrement -= 2
            for j in range(i, numchr, step):
                res += s[j]
                # there exist 2 characters per segment except 1st and last rows
                j2 = j + subincrement
                if j2 < numchr:
                    res += s[j2]
        res += s[lastrow::step] # last row

        return res

print Solution().convert("PAYPALISHIRING", 4)
