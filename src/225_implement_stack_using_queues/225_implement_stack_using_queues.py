class MyStack(object):
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.q_d = []
        self.q_t = []

    def push(self, x):
        """
        Push element x onto stack.
        :type x: int
        :rtype: void
        """
        if (not self.q_t):
            self.q_t.insert(0, x)
        else:
            self.q_d.insert(0, self.q_t.pop())
            self.q_t.insert(0, x)

    def pop(self):
        """
        Removes the element on top of the stack and returns that element.
        :rtype: int
        """
        if (self.q_t):
            return self.q_t.pop()
        elif (not self.q_d):
            return None
        while (len(self.q_d) > 1):
            self.q_t.insert(0, self.q_d.pop())
        self.q_t,self.q_d = self.q_d,self.q_t
        return self.q_t.pop()

    def top(self):
        """
        Get the top element.
        :rtype: int
        """
        n = self.pop()
        self.push(n)
        return n

    def empty(self):
        """
        Returns whether the stack is empty.
        :rtype: bool
        """
        return (not self.q_t) and (not self.q_d)

# debug
# Your MyStack object will be instantiated and called as such:
obj = MyStack()
obj.push(1)
obj.push(2)
print obj.top()
print obj.pop()
print obj.empty()
