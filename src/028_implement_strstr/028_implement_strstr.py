class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """

        # if needle in haystack: return haystack.find(needle)
        # return -1
        len_needle = len(needle)
        res = -1
        if 0 == len_needle:
            return 0
        for i in range(len(haystack) - len_needle + 1):
            if haystack[i:i+len_needle] == needle:
                res = i
                break

        return res

# debug
s = Solution()
print s.strStr("hello", "ll")
print s.strStr("aaaaa", "bba")
