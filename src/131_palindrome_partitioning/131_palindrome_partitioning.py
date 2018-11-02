class Solution(object):
    def partition(self, s):
        """
        :type s: str
        :rtype: List[List[str]]
        """

        if not s or 0 == len(s):
            return []
        elif 1 == len(s):
            return [ [s] ]
        # return self.partitionIteration(s)
        res = []
        self.partitionDfs(s, 0, [], res)
        return res

    def partitionDfs(self, s, start, sol, res):
        def isPalindrome(subs):
            i = 0; j = len(subs)-1
            while i < j:
                if subs[i] != subs[j]:
                    return False
                i += 1; j -= 1
            return True

        if start == len(s):
            res.append(sol)
            return
        elif (start+1) == len(s):
            res.append(sol + [s[-1]])
            return
        for i in range(start+1, len(s)+1):
            pre = s[start:i]
            if isPalindrome(pre):
                self.partitionDfs(s, i, sol+[pre], res)

    def partitionIteration(self, s):
        res = [[]]
        for i in range(len(s)):
            res_temp = []
            for item in res:
                if len(item) > 0 and item[-1] == s[i]:
                    p = item[:]
                    p[-1] += s[i]
                    res_temp.append(p)
                if len(item) > 1 and item[-2] == s[i]:
                    p = item[:]
                    tmp = p[-2:]
                    p = p[:-2]
                    p.append("".join(tmp + [s[i]]))
                    res_temp.append(p)
                res_temp.append(item + [s[i]])
            res = res_temp
        return res

# debug
s = Solution()
print s.partition("aab")
