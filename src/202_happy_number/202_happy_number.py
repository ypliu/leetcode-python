class Solution(object):
    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """

        return self.isHappyConstSpace(n)
        return self.isHappyBasedSet(n)

    def sumOfDigitSquare(self, num):
        s = 0
        while num != 0:
            r = num % 10
            s += r * r
            num //= 10
        return s

    def isHappyConstSpace(self, n):
        slow = fast = n
        while True:
            slow = self.sumOfDigitSquare(slow)
            fast = self.sumOfDigitSquare(self.sumOfDigitSquare(fast))
            if (1 == fast):
                return True
            elif (slow == fast):
                return False

    def isHappyBasedSet(self, n):
        sum_set = set()
        while (n != 1):
            n = self.sumOfDigitSquare(n)
            if n in sum_set:
                return False
            sum_set.add(n)
        return True

# debug
s = Solution()
print s.isHappy(18)
print s.isHappy(19)
