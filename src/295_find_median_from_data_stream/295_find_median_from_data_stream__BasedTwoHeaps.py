import heapq
class MedianFinder(object):

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.count = 0
        self.max_heap_for_smaller = []
        self.min_heap_for_larger = []

    def addNum(self, num):
        """
        :type num: int
        :rtype: void
        """
        self.count += 1
        if (self.count & 1):
            if (len(self.min_heap_for_larger) > 0) and (num > self.min_heap_for_larger[0]):
                num = heapq.heapreplace(self.min_heap_for_larger, num)
            heapq.heappush(self.max_heap_for_smaller, -num)
        else:
            if (len(self.max_heap_for_smaller) > 0) and (num < -self.max_heap_for_smaller[0]):
                num = -heapq.heapreplace(self.max_heap_for_smaller, -num)
            heapq.heappush(self.min_heap_for_larger, num)

    def findMedian(self):
        """
        :rtype: float
        """
        if (self.count & 1):
            return -self.max_heap_for_smaller[0]
        else:
            return (-self.max_heap_for_smaller[0] + self.min_heap_for_larger[0]) * 0.5

# Your MedianFinder object will be instantiated and called as such:
obj = MedianFinder()
obj.addNum(1)
obj.addNum(2)
print obj.findMedian()
obj.addNum(3)
print obj.findMedian()
