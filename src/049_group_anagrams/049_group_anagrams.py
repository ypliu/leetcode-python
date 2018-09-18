class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """

        ans = {}
        for string in strs:
            count = [0] * 26
            for ch in string:
                count[ord(ch) - ord('a')] += 1
            count = tuple(count)
            val = ans.get(count)
            if not val:
                ans[count] = [string]
            else:
                val.append(string)
        return ans.values()

# debug
s = Solution()
print s.groupAnagrams(["eat", "tea", "tan", "ate", "nat", "bat"])
