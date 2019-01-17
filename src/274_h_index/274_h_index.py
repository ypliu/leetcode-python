class Solution(object):
    def hIndex(self, citations):
        """
        :type citations: List[int]
        :rtype: int
        """

        if (not citations) or (len(citations) < 1):
            return 0
        return self.hIndexBasedCounting(citations)
        # return self.hIndexBasedSorting(citations)

    def hIndexBasedCounting(self, citations):
        n = len(citations)
        n_citations = [0 for _ in range(n+1)]
        for c in citations:
            if (c >= n):
                n_citations[n] += 1
            else:
                n_citations[c] += 1
        for i in range(n, 0, -1):
            if (n_citations[i] >= i):
                return i
            n_citations[i-1] += n_citations[i]
        return 0

    def hIndexBasedSorting(self, citations):
        citations.sort()
        h = len(citations)
        for i in range(len(citations)):
            if (citations[i] >= h):
                return h
            h -= 1
        return 0

# debug
s = Solution()
print s.hIndex([3,0,6,1,5])
