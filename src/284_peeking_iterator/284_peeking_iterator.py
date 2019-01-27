# Below is the interface for Iterator, which is already defined for you.
#
class Iterator(object):
    def __init__(self, nums):
        """
        Initializes an iterator object to the beginning of a list.
        :type nums: List[int]
        """
        self.l = nums[:]

    def hasNext(self):
        """
        Returns true if the iteration has more elements.
        :rtype: bool
        """
        return (len(self.l) > 0)

    def next(self):
        """
        Returns the next element in the iteration.
        :rtype: int
        """
        return self.l.pop(0)

class PeekingIterator(object):
    def __init__(self, iterator):
        """
        Initialize your data structure here.
        :type iterator: Iterator
        """
        self.it = iterator
        self.cur = self.it.next() if self.it.hasNext() else None

    def peek(self):
        """
        Returns the next element in the iteration without advancing the iterator.
        :rtype: int
        """
        return self.cur

    def next(self):
        """
        :rtype: int
        """
        val = self.cur
        self.cur = self.it.next() if self.it.hasNext() else None
        return val

    def hasNext(self):
        """
        :rtype: bool
        """
        return (self.cur != None)

# debug
# Your PeekingIterator object will be instantiated and called as such:
nums = [0,1,2]
iter = PeekingIterator(Iterator(nums))
while iter.hasNext():
    val = iter.peek()   # Get the next element but not advance the iterator.
    print iter.next(),  # Should return the same value as [val].
    print val
