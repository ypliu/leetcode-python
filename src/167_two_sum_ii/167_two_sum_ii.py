class Solution(object):
    def twoSum(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """

        if (not numbers) or (len(numbers) <= 1):
            return []
        start,end = 0,len(numbers)-1
        while start < end:
            s = numbers[start] + numbers[end]
            if s == target:
                return [start+1, end+1]
            elif s < target:
                start += 1
            else:
                end -= 1
        return []

# debug
s = Solution()
print s.twoSum([2,7,11,15], 9)
