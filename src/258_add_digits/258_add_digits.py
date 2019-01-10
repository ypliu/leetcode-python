class Solution(object):
    def addDigits(self, num):
        """
        :type num: int
        :rtype: int
        """

        if (num < 0):
            print "Error! The input is wrong:", num
            return -1
        elif (num < 10):
            return num
        return ((num - 1) % 9 + 1)

# debug
s = Solution()
print s.addDigits(38)
