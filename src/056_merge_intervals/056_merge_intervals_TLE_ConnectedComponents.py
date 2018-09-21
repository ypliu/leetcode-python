# Definition for an interval.
class Interval(object):
    def __init__(self, s=0, e=0):
        self.start = s
        self.end = e

import collections
class Solution(object):
    def merge(self, intervals):
        """
        :type intervals: List[Interval]
        :rtype: List[Interval]
        """

        if not intervals or 0 == len(intervals):
            return []
        elif 1 == len(intervals):
            return intervals
        graph = self.buildGraph(intervals)
        nodes_in_comp, num_comps = self.getComponents(graph, intervals)
        res = [self.mergeNodes(nodes_in_comp[i]) for i in range(num_comps)]
        return res


    def buildGraph(self, intervals):
        graph = collections.defaultdict(list)
        for i in xrange(len(intervals)-1):
            interval_i = intervals[i]
            for j in xrange(i+1, len(intervals)):
                interval_j = intervals[j]
                if self.overlap(interval_i, interval_j):
                    graph[interval_i].append(interval_j)
                    graph[interval_j].append(interval_i)
        return graph

    def overlap(self, interval_i, interval_j):
        return interval_i.end >= interval_j.start and interval_j.end >= interval_i.start

    def getComponents(self, graph, intervals):
        nodes_visited = set()
        num_comps = 0
        nodes_in_comp = collections.defaultdict(list)

        def markComponentDfs(start):
            stack = [start]
            while stack:
                node = stack.pop()
                nodes_visited.add(node)
                nodes_in_comp[num_comps].append(node)
                for interval in graph[node]:
                    if interval not in nodes_visited:
                        stack.append(interval)

        for interval in intervals:
            if interval not in nodes_visited:
                markComponentDfs(interval)
                num_comps += 1
        return nodes_in_comp, num_comps

    def mergeNodes(self, nodes):
        min_start, max_end = nodes[0].start, nodes[0].end
        for i in xrange(1, len(nodes)):
            if min_start > nodes[i].start:
                min_start = nodes[i].start
            if max_end < nodes[i].end:
                max_end = nodes[i].end
        return Interval(min_start, max_end)

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
