class Solution(object):
    def restoreIpAddresses(self, s):
        """
        :type s: str
        :rtype: List[str]
        """

        if not s or len(s) < 4:
            return []
        elif 4 == len(s):
            return ['.'.join(s)]
        res = []
        self.partitonIthSegment(s, 0, 1, "", res)
        return res

    def partitonIthSegment(self, s, start, i, sol, res):
        if len(s) <= start:
            return
        if 4 == i:
            max_pos = start + 3
            if len(s) > max_pos:
                return
            elif len(s) == max_pos:
                val = (ord(s[start])-ord('0'))*100 + (ord(s[start+1])-ord('0'))*10 + (ord(s[start+2])-ord('0'))
                if val >= 100 and val <= 255:
                    res.append(sol + s[start:])
            elif len(s) == start + 1 or s[start] != '0':
                res.append(sol + s[start:])
            return
        self.partitonIthSegment(s, start+1, i+1, sol+s[start]+'.', res)
        if '0' != s[start] and start + 1 < len(s):
            self.partitonIthSegment(s, start+2, i+1, sol+s[start:start+2]+'.', res)
            if start + 2 < len(s):
                val = (ord(s[start])-ord('0'))*100 + (ord(s[start+1])-ord('0'))*10 + (ord(s[start+2])-ord('0'))
                if val < 256:
                    self.partitonIthSegment(s, start+3, i+1, sol+s[start:start+3]+'.', res)

# debug
s = Solution()
print s.restoreIpAddresses("25525511135")
print s.restoreIpAddresses("010010")
print s.restoreIpAddresses("2222")
