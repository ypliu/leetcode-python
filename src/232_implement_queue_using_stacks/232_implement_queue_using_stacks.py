class MyQueue(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.f_stack = []
        self.r_stack = []

    def push(self, x):
        """
        Push element x to the back of queue.
        :type x: int
        :rtype: void
        """
        self.f_stack.append(x)

    def pop(self):
        """
        Removes the element from in front of queue and returns that element.
        :rtype: int
        """
        if (not self.r_stack):
            while self.f_stack:
                self.r_stack.append(self.f_stack.pop())
        return self.r_stack.pop()

    def peek(self):
        """
        Get the front element.
        :rtype: int
        """
        if (not self.r_stack):
            while self.f_stack:
                self.r_stack.append(self.f_stack.pop())
        return self.r_stack[-1]

    def empty(self):
        """
        Returns whether the queue is empty.
        :rtype: bool
        """
        return (self.f_stack == []) and (self.r_stack == [])

# Your MyQueue object will be instantiated and called as such:
obj = MyQueue()
obj.push(1)
obj.push(2)
print obj.peek()
print obj.pop()
print obj.empty()
