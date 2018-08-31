class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
	
        if len(strs) == 0:
            return ''
        res = strs[0]
        for i in range(1, len(strs)):
            j, min_len = 0, min(len(res), len(strs[i]))
            while j < min_len:
                if res[j] != strs[i][j]:
                    break
                j += 1
            res = res[:j]

        return res

#
s = Solution()
print s.longestCommonPrefix(["flower","flow","flight"])
