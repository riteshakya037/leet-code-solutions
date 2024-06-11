class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices) < 2:
            return 0
        dp = [[0] * 2 for _ in range(len(prices))]
        dp[0][0] = -prices[0]
        dp[1][1] = max(prices[1] - prices[0], 0)
        dp[1][0] = max(-prices[1], -prices[0])
        for i in range(2, len(dp)):
            dp[i][0] = max(dp[i - 2][1] - prices[i], dp[i - 1][0])
            dp[i][1] = max(dp[i - 1][0] + prices[i], dp[i - 1][1])
        return dp[-1][1]
