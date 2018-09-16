class Solution(object):
    def jump(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        jumps, max_cur, max_next = 0, 0, 0
        i, last = 0, len(nums)-1
        while max_cur < last:
            while i <= max_cur:
                max_next = max(max_next, i+nums[i])
                i += 1
            # it means itorator can not walk farther if max_cur == max_next, unconnected-graph
            if max_cur >= max_next:
                return -1
            else:
                jumps += 1
                max_cur = max_next
        return jumps

# debug
s = Solution()
print s.jump([2,3,1,1,4])
print s.jump([2,3,1,1,0,0,0,0,4])
