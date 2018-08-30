class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """

        max_area = -1
        left, right = 0, len(height) - 1
        while left < right:
            width = right - left
            if height[left] <= height[right]:
                min_height = height[left]
                left += 1
            else:
                min_height = height[right]
                right -= 1
            cur_area = width * min_height
            if max_area < cur_area:
                max_area = cur_area

        return max_area

#
print Solution().maxArea([1,8,6,2,5,4,8,3,7])
