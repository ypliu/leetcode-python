class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """

        # return list(str(int(''.join(map(str, digits)))+1))
        if not digits or 0 == len(digits):
            return [1]
        res = []; num = 0
        for n in digits:
            num = num * 10 + n
        num += 1
        while num:
            res.insert(0, num % 10)
            num /= 10
        return res

# debug
s = Solution()
print s.plusOne([1,2,3])
print s.plusOne([4,3,2,1])
