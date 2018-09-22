# Definition for an interval.
class Interval(object):
    def __init__(self, s=0, e=0):
        self.start = s
        self.end = e

class Solution(object):
    def insert(self, intervals, newInterval):
        """
        :type intervals: List[Interval]
        :type newInterval: Interval
        :rtype: List[Interval]
        """

        if not newInterval:
            return intervals
        elif not intervals or 0 == len(intervals):
            return [newInterval]

        i = 0
        while i < len(intervals):
            if newInterval.end < intervals[i].start:
                intervals.insert(i, newInterval)
                return intervals
            elif newInterval.start > intervals[i].end:
                i += 1
                continue
            elif newInterval.start >= intervals[i].start and newInterval.end <= intervals[i].end:
                return intervals
            else:
                newInterval.start = min(newInterval.start, intervals[i].start)
                newInterval.end = max(newInterval.end, intervals[i].end)
                del(intervals[i])
        intervals.append(newInterval)
        return intervals

# debug
    def print_intervals(self, intervals):
        print '[ ',
        for it in intervals:
            print '[', it.start, ',', it.end, ']',
        print ' ]'

s = Solution()
intervals = []
intervals.append(Interval(1,3))
intervals.append(Interval(6,9))
s.print_intervals(s.insert(intervals, Interval(2,5)))
intervals = []
intervals.append(Interval(1,2))
intervals.append(Interval(3,5))
intervals.append(Interval(6,7))
intervals.append(Interval(8,10))
intervals.append(Interval(12,16))
s.print_intervals(s.insert(intervals, Interval(4,8)))
intervals = []
# intervals.append(Interval(1,4))
s.print_intervals(s.insert(intervals, Interval(4,8)))
