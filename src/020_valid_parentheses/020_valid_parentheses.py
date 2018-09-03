class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """

        map_parentheses = {")":"(", "]":"[", "}":"{"}
        stack_parentheses = []

        for ch in s:
            if ch in "([{":
                stack_parentheses.append(ch)
            elif ch in ")]}":
                if not stack_parentheses or stack_parentheses[-1] != map_parentheses[ch]:
                    return False
                stack_parentheses.pop()

        return not stack_parentheses

#
s = Solution()
print s.isValid("{[]}")
