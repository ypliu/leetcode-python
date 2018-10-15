class Solution(object):
    def isInterleave(self, s1, s2, s3):
        """
        :type s1: str
        :type s2: str
        :type s3: str
        :rtype: bool
        """

        if not s1:
            return s2 == s3
        elif not s2:
            return s1 == s3
        elif (len(s1) + len(s2) != len(s3)) or (s3[-1] != s1[-1] and s3[-1] != s2[-1]) or (s3[0] != s1[0] and s3[0] != s2[0]):
            return False

        dp_table = [False for j in range(len(s1)+1)]
        dp_table[0] = True
        for j in range(len(s1)):
            dp_table[j+1] = dp_table[j] and (s1[j] == s3[j])
        for i in range(len(s2)):
            flag_fail = True
            dp_table[0] = dp_table[0] and (s2[i] == s3[i])
            for j in range(len(s1)):
                ch = s3[i + j + 1]
                if (s1[j] == ch and dp_table[j]) or (s2[i] == ch and dp_table[j+1]):
                    dp_table[j+1] = True
                    flag_fail = False
                else:
                    dp_table[j+1] = False
            if not dp_table[0] and flag_fail:
                return False
        return dp_table[-1]

# debug
s = Solution()
print s.isInterleave("aabcc", "dbbca", "aadbbcbcac")
print s.isInterleave("aabcc", "dbbca", "aadbbbaccc")
print s.isInterleave("aa", "ab", "abaa")
