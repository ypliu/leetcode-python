class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """

        if not s or len(s) <= 1:
            return True
        val_tr = ord('a') - ord('A')
        i = 0; j = len(s)-1
        while i < j:
            while i < j:
                ch_h = ord(s[i])
                if (ch_h >= ord('A') and ch_h <= ord('Z')):
                    ch_h += val_tr
                    break
                elif (ch_h >= ord('a') and ch_h <= ord('z')) or (ch_h >= ord('0') and ch_h <= ord('9')):
                    break
                i += 1
            while i < j:
                ch_t = ord(s[j])
                if (ch_t >= ord('A') and ch_t <= ord('Z')):
                    ch_t += val_tr
                    break
                elif (ch_t >= ord('a') and ch_t <= ord('z')) or (ch_t >= ord('0') and ch_t <= ord('9')):
                    break
                j -= 1
            if i < j and (ch_h != ch_t):
                return False
            i += 1; j-= 1
        return True

# debug
s = Solution()
print s.isPalindrome("A man, a plan, a canal: Panama")
print s.isPalindrome("race a car")
