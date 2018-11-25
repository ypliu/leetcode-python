class MinStack(object):

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.stack_t = []

    def push(self, x):
        """
        :type x: int
        :rtype: void
        """
        if (not self.stack_t) or (0 == len(self.stack_t)):
            min_val = x
        else:
            min_val = min(self.stack_t[-1][1], x)
        self.stack_t.append((x,min_val))

    def pop(self):
        """
        :rtype: void
        """
        if (not self.stack_t) or (0 == len(self.stack_t)):
            return None
        return self.stack_t.pop()[0]

    def top(self):
        """
        :rtype: int
        """
        if (not self.stack_t) or (0 == len(self.stack_t)):
            return None
        return self.stack_t[-1][0]

    def getMin(self):
        """
        :rtype: int
        """
        if (not self.stack_t) or (0 == len(self.stack_t)):
            return None
        return self.stack_t[-1][1]

# Your MinStack object will be instantiated and called as such:
obj = MinStack()
obj.push(-2)
obj.push(0)
obj.push(-3)
print obj.getMin()
obj.pop()
print obj.top()
print obj.getMin()
