class Solution(object):
    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """

        num_last = len(nums) - 1
        if num_last < 2:
            return
        nums.sort()
        res = nums[0] + nums[1] + nums[2]
        min_diff = abs(res - target)

        for i in range(num_last - 1):
            j, k = i+1, num_last
            # if the sum of 3 consecutive array elements start at i is greater than target, the following triples will be much greater
            cur_sum = nums[i] + nums[j] + nums[j+1]
            if cur_sum >= target:
                cur_diff = cur_sum - target
                if min_diff > cur_diff:
                    res = cur_sum
                break
            # if the sum of 3 array elements whose id are i and the last two is smaller than target, the forward triples include array element i will be much smaller
            cur_sum = nums[i] + nums[k] + nums[k-1]
            if cur_sum <= target:
                cur_diff = target - cur_sum
                if min_diff > cur_diff:
                    res = cur_sum
                    min_diff = cur_diff
                continue

            while j < k:
                cur_sum = nums[i] + nums[j] + nums[k]
                cur_diff = abs(cur_sum - target)
                if min_diff > cur_diff:
                    res = cur_sum
                    min_diff = cur_diff
                if cur_sum > target:
                    k -= 1
                elif cur_sum < target:
                    j += 1
                else:
                    return target
            i += 1

        return res

# debug
s = Solution()
print s.threeSumClosest([1,2,4,8,16,32,64,128], 82)
