class Solution(object):
    def longestValidParentheses(self, s):
        """
        :type s: str
        :rtype: int
        """

        max_len = 0
        left = right = 0
        start, end = 0, len(s) - 1
        while start <= end:
            if '(' == s[start]:
                left += 1
            elif ')' == s[start]:
                right += 1
                if left < right:
                    left = right = 0
                elif left == right and max_len < left:
                    max_len = left
            start += 1

        left = right = 0
        start, end = 0, len(s) - 1
        while start <= end:
            if '(' == s[end]:
                left += 1
                if left > right:
                    left = right = 0
                elif left == right and max_len < left:
                    max_len = left
            elif ')' == s[end]:
                right += 1
            end -= 1

        return (max_len << 1)

# debug
s = Solution()
str = "()((())"
print s.longestValidParentheses(str)
