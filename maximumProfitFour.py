class Solution:
    def maximumProfit(self, prices: list[int], k: int) -> int:
        n = len(prices)
        if n < 2 or k <= 0:
            return 0
        dp = [[0, float('-inf'), float('-inf')] for _ in range(k+1)]
        for price in prices:
            for c in range(k+1):
                dp[c][1] = max(dp[c][1], dp[c][0] - price)
                dp[c][2] = max(dp[c][2], dp[c][0] + price)
            for c in range(k-1, -1, -1):
                dp[c+1][0] = max(dp[c+1][0], dp[c][1] + price, dp[c][2] - price)
        return max(dp[c][0] for c in range(k+1))
