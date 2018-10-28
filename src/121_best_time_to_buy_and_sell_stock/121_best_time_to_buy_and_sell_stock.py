class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """

        if not prices or len(prices) <= 1:
            return 0
        min_price = prices[0]
        max_profit = 0
        for i in range(1, len(prices)):
            if min_price > prices[i]:
                min_price = prices[i]
            else:
                diff = prices[i] - min_price
                if max_profit < diff:
                    max_profit = diff
        return max_profit

# debug
s = Solution()
print s.maxProfit([7,1,5,3,6,4])
