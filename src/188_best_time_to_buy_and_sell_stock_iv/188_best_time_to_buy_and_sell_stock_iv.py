class Solution(object):
    def maxProfit(self, k, prices):
        """
        :type k: int
        :type prices: List[int]
        :rtype: int
        """
        return self.maxProfitKTransactionsDp(prices, k)

    def maxProfitKTransactionsDpTLE(self, prices, k):
        if not prices or len(prices) <= 1 or k < 1:
            return 0
        dp_table = [0 for j in range(len(prices))]
        i = 0
        while i < k:
            max_temp = dp_table[0] - prices[0]
            for j in range(1, len(prices)):
                max_temp = max(max_temp, dp_table[j] - prices[j])
                dp_table[j] = max(dp_table[j-1], max_temp+prices[j])
            i += 1
        return dp_table[-1]

    def maxProfitKTransactionsDp(self, prices, k):
        if not prices or len(prices) <= 1 or k < 1:
            return 0
        n = len(prices)
        if k >= n/2:
            res = 0
            for i in range(1, n):
                res += max(prices[i]-prices[i-1], 0)
            return res
        local_max = [0 for i in range(k+1)]
        global_max = [0 for i in range(k+1)]
        for i in range(1,n):
            diff = prices[i] - prices[i-1]
            for j in range(k, 0, -1):
                local_max[j] = max(local_max[j], global_max[j-1]) + diff
                global_max[j] = max(local_max[j], global_max[j])
        return global_max[k]

# debug
s = Solution()
print s.maxProfit(2, [2,4,1])
print s.maxProfit(2, [3,2,6,5,0,3])
