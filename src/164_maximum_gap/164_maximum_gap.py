class Solution(object):
    def maximumGap(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        if (not nums) or (len(nums) < 2):
            return 0
        elif (2 == len(nums)):
            return abs(nums[0] - nums[1])
        max_val = min_val = nums[0]
        for n in nums[1:]:
            if max_val < n:
                max_val = n
            elif min_val > n:
                min_val = n
        if max_val == min_val:
            return 0
        interval = (max_val - min_val + len(nums) - 2) // (len(nums) - 1)
        len_bucket = (max_val - min_val) // interval + 1
        bucket = [None for i in range(len_bucket)]
        for n in nums:
            ind = (n - min_val) // interval
            if not bucket[ind]:
                bucket[ind] = [n, n]
            else:
                if bucket[ind][0] > n:
                    bucket[ind][0] = n
                elif bucket[ind][1] < n:
                    bucket[ind][1] = n
        max_gap = interval; pre_max = bucket[0][1]
        for b in bucket[1:]:
            if not b:
                continue
            max_gap = max(max_gap, b[0]-pre_max)
            pre_max = b[1]
        return max_gap

# debug
s = Solution()
print s.maximumGap([3,6,9,1])
print s.maximumGap([10])
