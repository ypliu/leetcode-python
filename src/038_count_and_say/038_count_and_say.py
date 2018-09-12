class Solution(object):
    def countAndSay(self, n):
        """
        :type n: int
        :rtype: str
        """

        if n < 1 or n > 30:
            return None

        res = "1"
        for _ in range(1, n):
            temp = res + '$'
            res = ""
            ch_res, count, i = temp[0], 1, 1
            while i < len(temp):
                if temp[i] != ch_res:
                    res += str(count) + ch_res
                    ch_res = temp[i]
                    count = 1
                else:
                    count += 1
                i += 1

        return res

# debug
s = Solution()
print s.countAndSay(20)
