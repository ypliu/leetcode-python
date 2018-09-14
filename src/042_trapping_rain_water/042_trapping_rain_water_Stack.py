class Solution(object):
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """

        height_stack = []
        i, res = 0, 0
        # it is equivalent to accumulate gradually the water  while the water falling from the top (or horizontal partitioning)
        while i < len(height):
            while len(height_stack) > 0 and height[i] > height[height_stack[-1]]:
                top = height_stack[-1]
                height_stack.pop()
                if not len(height_stack):
                    break
                distance = i - height_stack[-1] - 1
                bounded_height = min(height[i], height[height_stack[-1]]) - height[top]
                res += distance * bounded_height
            height_stack.append(i)
            i += 1

        return res

# debug
s = Solution()
print s.trap([0,1,0,2,1,0,1,3,2,1,2,1])
