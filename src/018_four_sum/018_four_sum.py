class Solution(object):
    def fourSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[List[int]]
        """

        res = []
        num_last = len(nums) - 1
        if num_last < 3:
            return []
        nums.sort()

        for i in range(num_last - 2):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            start_j = i + 1
            for j in range(start_j, num_last-1):
                if j > start_j and nums[j] == nums[j-1]:
                    continue
                cur_diff = target - nums[i] - nums[j]
                k, l = j+1, num_last
                # if the sum of array element i and 3 consecutive array elements start at j is greater than target, the following triples will be much greater
                sub_sum = nums[k] + nums[k+1]
                if sub_sum >= cur_diff:
                    if sub_sum == cur_diff:
                        res.append([nums[i], nums[j], nums[k], nums[k+1]])
                    break
                # if the sum of 4 array elements whose id are i, j and the last two is smaller than target, the forward triples include array element j will be much smaller
                sub_sum = nums[l] + nums[l-1]
                if sub_sum <= cur_diff:
                    if sub_sum == cur_diff:
                        res.append([nums[i], nums[j], nums[l-1], nums[l]])
                    continue

                while k < l:
                    sub_sum = nums[k] + nums[l]
                    if sub_sum > cur_diff:
                        l -= 1
                    elif sub_sum < cur_diff:
                        k += 1
                    else:
                        res.append([nums[i], nums[j], nums[k], nums[l]])
                        k += 1
                        while k < l and nums[k] == nums[k-1]:
                            k += 1
                        l -= 1
                        while k < l and nums[l] == nums[l+1]:
                            l -= 1
        return res

# debug
s = Solution()
print s.fourSum([1, 0, -1, 0, -2, 2], 0)
