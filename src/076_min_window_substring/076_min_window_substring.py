from collections import Counter
class Solution(object):
    def minWindow(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """

        if not s or not t or len(t) > len(s):
            return ""

        dict_t = Counter(t)
        num_characters_t = len(dict_t)
        filtered_s = []
        for i, ch in enumerate(s):
            if ch in dict_t:
                filtered_s.append((i, ch))

        left = right = 0
        num_characters_curr = 0
        window_counts = {}
        res = (len(s) + 1), None, None
        while right < len(filtered_s):
            ch = filtered_s[right][1]
            window_counts[ch] = window_counts.get(ch, 0) + 1
            if window_counts[ch] == dict_t[ch]:
                num_characters_curr += 1
            while left <= right and num_characters_t == num_characters_curr:
                start = filtered_s[left][0]
                end = filtered_s[right][0]
                if end - start + 1 < res[0]:
                    res = (end - start + 1, start, end)
                ch = filtered_s[left][1]
                window_counts[ch] -= 1
                if window_counts[ch] < dict_t[ch]:
                    num_characters_curr -= 1
                left += 1
            right += 1

        if len(s) < res[0]:
            return ""
        else:
            return s[res[1]:res[2]+1]

# debug
s = Solution()
print s.minWindow("ADOBECODEBANC", "ABC")
