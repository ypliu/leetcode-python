class Solution(object):
    def getSkyline(self, buildings):
        """
        :type buildings: List[List[int]]
        :rtype: List[List[int]]
        """

        if (not buildings) or (len(buildings) < 1):
            return []
        return self.getSkylineHeap(buildings)

    def getSkylineHeap(self, buildings):
        #https://leetcode.com/problems/the-skyline-problem/discuss/61192/Once-for-all-explanation-with-clean-Java-code(O(n2)time-O(n)-space)
        #https://leetcode.com/problems/the-skyline-problem/discuss/61261/10-line-Python-solution-104-ms
        #https://briangordon.github.io/2014/08/the-skyline-problem.html
        import heapq
        events = sorted([(l, -h, r) for l,r,h in buildings] + list({(r, 0, None) for l,r,h in buildings}))
        res, min_heap = [[0, 0]], [(0, float("inf"))]
        for l,neg_h,r in events:
            while l >= min_heap[0][1]:
                heapq.heappop(min_heap)
            if (neg_h != 0):
                heapq.heappush(min_heap, (neg_h, r))
            if (res[-1][1] != -min_heap[0][0]):
                res.append([l, -min_heap[0][0]])
        return res[1:]

# debug
s = Solution()
print s.getSkyline([ [2, 9, 10], [3, 7, 15], [5, 12, 12], [15, 20, 10], [19, 24, 8] ])
# [ [2 10], [3 15], [7 12], [12 0], [15 10], [20 8], [24, 0] ]
