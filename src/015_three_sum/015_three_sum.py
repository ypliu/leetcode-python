class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """

        res = []
        i, thr_while = 0, len(nums)-2
        if thr_while <= 0:
            return res

        nums.sort()
        while i < thr_while:
            if nums[i] > 0:
                break
            target = -nums[i]
            j, k = i+1, thr_while+1
            while j < k:
                ht_sum = nums[j] + nums[k]
                if ht_sum < target:
                    j += 1
                elif ht_sum > target:
                    k -= 1
                else:
                    res.append([nums[i], nums[j], nums[k]])
                    j += 1
                    while j < k and nums[j] == nums[j-1]:
                        j += 1
                    k -= 1
                    while j < k and nums[k] == nums[k+1]:
                        k -= 1
            i += 1
            while i < thr_while and nums[i] == nums[i-1]:
                i += 1

        return res

# debug
s = Solution()
print s.threeSum([-1, 0, 1, 2, -1, -4])
print s.threeSum([-1,0,1,2,-1,-4, -1, -1, -2, -3, -4])
