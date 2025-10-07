class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        n = len(prices)
        memo = {}

        def dp(i, holding):

            if i >= n:
                return 0

            if (i, holding) in memo:
                return memo[(i, holding)]

            profit = dp(i+1,holding)

            if holding:
                profit = max(profit, prices[i] + dp(i+2, 0))
            else:
                profit = max(profit,-prices[i] + dp(i+1, 1))

            memo[(i, holding)] = profit

            return profit

        return dp(0,0)