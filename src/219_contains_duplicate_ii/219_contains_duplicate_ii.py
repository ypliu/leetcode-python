class Solution(object):
    def containsNearbyDuplicate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """

        if (not nums) or (len(nums) <= 1) or (k <= 0):
            return False
        dict_n2i = {}
        for i,n in enumerate(nums):
            if (n in dict_n2i) and (i - dict_n2i[n] <= k):
                return True
            dict_n2i[n] = i
        return False

# debug
s = Solution()
print s.containsNearbyDuplicate([1,2,3,1], 3)
print s.containsNearbyDuplicate([1,0,1,1], 1)
print s.containsNearbyDuplicate([1,2,3,1,2,3], 2)
