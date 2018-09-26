class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """

        # return list(str(int(''.join(map(str, digits)))+1))
        if not digits or 0 == len(digits):
            return [1]

        for i in xrange(len(digits)-1, -1, -1):
            if 9 == digits[i]:
                digits[i] = 0
            else:
                digits[i] += 1
                break
        else:
            digits.insert(0, 1)
        return digits

# debug
s = Solution()
print s.plusOne([1,2,3])
print s.plusOne([1,8,9,9])
print s.plusOne([9,9])
