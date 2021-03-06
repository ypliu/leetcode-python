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

        # intervals.append(newInterval)
        # intervals.sort(key=lambda x: x.start)
        for i, interval in enumerate(intervals):
            if newInterval.start <= interval.start:
                intervals.insert(i, newInterval)
                break
        else:
            intervals.append(newInterval)

        res, interval_temp = [], intervals[0]
        for i in xrange(1, len(intervals)):
            if interval_temp.end >= intervals[i].start:
                interval_temp.end = max(interval_temp.end, intervals[i].end)
            else:
                res.append(interval_temp)
                interval_temp = intervals[i]
        return (res + [interval_temp])

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
