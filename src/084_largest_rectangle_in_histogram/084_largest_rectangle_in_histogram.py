class Solution(object):
    def largestRectangleArea(self, heights):
        """
        :type heights: List[int]
        :rtype: int
        """

        heights.append(0)
        stack = []; stack.append(-1)
        res = 0
        for i in xrange(len(heights)):
            while heights[i] < heights[stack[-1]]:
                h = heights[stack.pop()]
                w = i - stack[-1] - 1
                res = max(res, h*w)
            stack.append(i)
        heights.pop()
        return res

# debug
s = Solution()
print s.largestRectangleArea([2,1,5,6,2,3])
