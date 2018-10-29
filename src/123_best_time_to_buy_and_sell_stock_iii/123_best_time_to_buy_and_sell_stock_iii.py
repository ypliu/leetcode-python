class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """

        return self.maxProfitFromAns(prices)
        # return self.maxProfitKTransactionsDp(prices, 2)

    def maxProfitFromAns(self, prices):
        if not prices or len(prices) <= 1:
            return 0
        buy1 = buy2 = -prices[0]
        sell1 = sell2 = 0
        for i in range(1, len(prices)):
            sell2 = max(sell2, buy2+prices[i])
            buy2 = max(buy2, sell1-prices[i])
            sell1 = max(sell1, buy1+prices[i])
            buy1 = max(buy1, -prices[i])
        return sell2

    def maxProfitKTransactionsDp(self, prices, k):
        if not prices or len(prices) <= 1 or k < 1:
            return 0
        dp_table = [[0 for j in range(len(prices))] for i in range(k+1)]
        for i in range(0, k):
            max_temp = dp_table[i][0] - prices[0]
            for j in range(1, len(prices)):
                dp_table[i+1][j] = max(dp_table[i+1][j-1], max_temp+prices[j])
                max_temp = max(max_temp, dp_table[i][j] - prices[j])
        return dp_table[-1][-1]

# debug
s = Solution()
print s.maxProfit([3,3,5,0,0,3,1,4])
print s.maxProfit([1,2,3,4,5])
print s.maxProfit([7,6,4,3,1])
