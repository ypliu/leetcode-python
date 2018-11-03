class Solution(object):
    def canCompleteCircuit(self, gas, cost):
        """
        :type gas: List[int]
        :type cost: List[int]
        :rtype: int
        """

        if (not gas) or (not cost) or (len(gas) != len(cost)):
            return -1
        elif 1 == len(cost):
            return 0 if gas[0] >= cost[0] else -1

        start = 0; remainder = gas[0] - cost[0]; next = 1
        while start != next:
            if remainder >= 0:
                remainder += gas[next] - cost[next]
                next = (next+1) % len(gas)
            else:
                start = (start - 1 + len(gas)) % len(gas)
                remainder += gas[start] - cost[start]
        return start if (remainder >= 0) else -1

# debug
s = Solution()
print s.canCompleteCircuit([1,2,3,4,5], [3,4,5,1,2])
print s.canCompleteCircuit([2,3,4], [3,4,3])
