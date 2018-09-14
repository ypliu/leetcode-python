class Solution(object):
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """

        max_left = max_right = 0
        highest_left = []
        highest_right = []
        num_elevation = len(height)
        l, r = 0, num_elevation-1
        while l < num_elevation:
            max_left = max(max_left, height[l])
            highest_left.append(max_left)
            max_right = max(max_right, height[r])
            highest_right.append(max_right)
            l += 1
            r -= 1
        highest_right.reverse()

        l, sum = 0, 0
        while l < num_elevation:
            sum += min(highest_left[l], highest_right[l]) - height[l]
            l += 1

        return sum

# debug
s = Solution()
print s.trap([0,1,0,2,1,0,1,3,2,1,2,1])
