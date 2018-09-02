class Solution(object):
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """

        alpha = { '0':" ", '1':"", '2':"abc", '3':"def", '4':"ghi", '5':"jkl", '6':"mno", '7':"pqrs", '8':"tuv", '9':"wxyz" }
        res = [ '' ]
        if not digits:
            return []

        for i in range(len(digits)):
            temp = res
            res = []
            # BFS
            for pre in temp:
                for ch in alpha[digits[i]]:
                    res.append(pre + ch)

        return res

# debug
s = Solution()
print s.letterCombinations('23')
