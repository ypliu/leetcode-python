# Definition for an interval.
class Interval(object):
    def __init__(self, s=0, e=0):
        self.start = s
        self.end = e

class Solution(object):
    def merge(self, intervals):
        """
        :type intervals: List[Interval]
        :rtype: List[Interval]
        """

        if not intervals:
            return []
        elif len(intervals) <= 1:
            return intervals

        intervals.sort(key=lambda x: x.start)
        res = [intervals[0]]
        for i in xrange(1, len(intervals)):
            if res[-1].end >= intervals[i].start:
                res[-1].end = max(res[-1].end, intervals[i].end)
            else:
                res.append(intervals[i])
        return res

# debug
    def print_intervals(self, intervals):
        print '[ ',
        for it in intervals:
            print '[', it.start, ',', it.end, ']',
        print ' ]'

s = Solution()
intervals = []
intervals.append(Interval(1,3))
intervals.append(Interval(2,6))
intervals.append(Interval(8,10))
intervals.append(Interval(15,18))
s.print_intervals(s.merge(intervals))
intervals = []
intervals.append(Interval(1,4))
intervals.append(Interval(4,5))
s.print_intervals(s.merge(intervals))
intervals = []
# intervals.append(Interval(1,4))
s.print_intervals(s.merge(intervals))
