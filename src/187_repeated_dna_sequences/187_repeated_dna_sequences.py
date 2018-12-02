class Solution(object):
    def findRepeatedDnaSequences(self, s):
        """
        :type s: str
        :rtype: List[str]
        """

        temp, res = set(), set()
        for i in range(len(s)-10+1):
            substr = s[i:i+10]
            if substr not in temp:
                temp.add(substr)
            else:
                res.add(substr)
        return list(res)

# debug
s = Solution()
print s.findRepeatedDnaSequences("AAAAACCCCCAAAAACCCCCCAAAAAGGGTTT")
