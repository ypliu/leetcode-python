class Solution(object):
    def containsNearbyAlmostDuplicate(self, nums, k, t):
        """
        :type nums: List[int]
        :type k: int
        :type t: int
        :rtype: bool
        """

        if (not nums) or (len(nums) <= 1) or (k <= 0) or (t < 0):
            return False
        buckets = {}; length = t + 1
        for i,n in enumerate(nums):
            idx = n / length
            if (idx in buckets) or ((idx-1 in buckets) and ((n-buckets[idx-1]) < length)) or ((idx+1 in buckets) and ((buckets[idx+1]-n) < length)):
                return True
            buckets[idx] = n
            if (i >= k):
                del buckets[nums[i-k] / length]
        return False

# debug
s = Solution()
print s.containsNearbyAlmostDuplicate([1,2,3,1], 3, 0)
print s.containsNearbyAlmostDuplicate([1,0,1,1], 1, 2)
print s.containsNearbyAlmostDuplicate([1,5,9,1,5,9], 2, 3)
