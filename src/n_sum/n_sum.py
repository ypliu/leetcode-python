class Solution(object):
    def nSum(self, nums, target, N, result, results):
        if N == 2:
            l, r = 0, len(nums) - 1
            while l < r:
                sum = nums[l] + nums[r]
                if sum < target:
                    l += 1
                elif sum > target:
                    r -= 1
                else:
                    results.append(result + [nums[l], nums[r]])
                    l += 1
                    while l < r and nums[l] == nums[l - 1]:
                        l += 1
                    # it will be faster as the following 3 lines, it also works if omitting
                    r -= 1
                    while l < r and nums[r] == nums[r + 1]:
                        r -= 1
        else:
            # recursion by DFS
            for i in xrange(len(nums) - N + 1):
                if i > 0 and nums[i - 1] == nums[i]:
                    continue
                self.nSum(nums[i+1:], target - nums[i], N - 1, result + [nums[i]], results)

    def start_nSum(self, nums, target, N):
        results = []
        nums.sort()
        if len(nums) < N or N < 2 or target < nums[0] * N or target > nums[-1] * N:
            return []
        self.nSum(nums, target, N, [], results)
        return results

    def fourSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[List[int]]
        """

        results = self.start_nSum(nums, target, 4)
        return results

# debug
s = Solution()
print s.fourSum([1, 0, -1, 0, -2, 2], 0)
print s.start_nSum([1, 0, -1, 0, -2, 2], 0, 4)
