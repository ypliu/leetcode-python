class Solution(object):
    def isNumber(self, s):
        """
        :type s: str
        :rtype: bool
        """

        # return re.match("^\s*[+-]?(\d*\.\d+|\d+\.\d*|\d+)(e[+-]?\d+)?\s*$", s) != None
        set_states = { 0:'initial', 1:'space_start', 2:'mantissa_sign', 3:'mantissa_0', 4:'mantissa_integer', 5:'mantissa_point', 6:'mantissa_decimal', 7:'exponent_start', 8:'exponent_sign', 9:'exponent_0', 10:'exponent_integer', 11:'space_end', 12:'just_point' }

        cur_state = 0
        for ch in s:
            if '+' == ch or '-' == ch:
                if 0 == cur_state or 1 == cur_state:
                    cur_state = 2
                elif 7 == cur_state:
                    cur_state = 8
                else:
                    return False
            elif '0' == ch:
                if 0 == cur_state or 1 == cur_state or 2 == cur_state:
                    cur_state = 3
                elif 3 == cur_state or 4 == cur_state or 6 == cur_state:
                    continue
                elif 5 == cur_state or 12 == cur_state:
                    cur_state = 6
                elif 7 == cur_state or 8 == cur_state:
                    cur_state = 9
                elif 9 == cur_state or 10 == cur_state:
                    continue
                else:
                    return False
            elif ch >= '1' and ch <= '9':
                if 0 == cur_state or 1 == cur_state or 2 == cur_state or 3 == cur_state or 4 == cur_state:
                   cur_state = 4
                elif 5 == cur_state or 6 == cur_state or 12 == cur_state:
                    cur_state = 6
                elif 7 == cur_state or 8 == cur_state or 9 == cur_state or 10 == cur_state:
                    cur_state = 10
                else:
                    return False
            elif 'e' == ch or 'E' == ch:
                if 3 == cur_state or 4 == cur_state or 5 == cur_state or 6 == cur_state:
                    cur_state = 7
                else:
                    return False
            elif '.' == ch:
                if 3 == cur_state or 4 == cur_state:
                    cur_state = 5
                elif 0 == cur_state or 1 == cur_state or 2 == cur_state:
                    cur_state = 12
                else:
                    return False
            elif ' ' == ch or '\t' == ch:
                if 0 == cur_state or 1 == cur_state:
                    cur_state = 1
                elif 3 == cur_state or 4 == cur_state or 5 == cur_state or 6 == cur_state or 9 == cur_state or 10 == cur_state or 11 == cur_state:
                    cur_state = 11
                else:
                    return False
            else:
                return False
        if 0 == cur_state or 1 == cur_state or 2 == cur_state or 7 == cur_state or 8 == cur_state or 12 == cur_state:
            return False
        return True

# debug
s = Solution()
arr_s = [ "0", " 0.1 ", "abc", "1 a", "2e10", " -90e3   ", " 1e", "e3", " 6e-1", " 99e2.5 ", "53.5e93", " --6 ", "-+3", "95a54e53", ".1", "01", "3.", " 3. ", ".", "00", "3.5e+3.5e+3.5", "+.8", "46.e3", "256523.e02", "378510e004" ]
for string in arr_s:
    print string, '=>', s.isNumber(string)
