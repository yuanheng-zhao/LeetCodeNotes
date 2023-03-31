# Template to solve all the buy stock questions
class Solution:
    def maxProfit(self, k: int, prices: List[int]) -> int:

        if len(prices) <= 1:
            return 0

        # equivalent to no limit on number of transactions
        if k > len(prices) // 2:
            ans = 0
            for i in range(1, len(prices)):
                if prices[i] > prices[i - 1]:
                    ans += prices[i] - prices[i - 1]
            return ans

        # dp[i: ith day][max_k: maximum number of transactions allowed][1 or 0: holding a stock or not]
        dp = [[[0, 0] for _ in range(k + 1)] for _ in range(len(prices))]
        for i in range(len(prices)):
            dp[i][0][1] = float('-inf')
        
        for i in range(len(prices)):
            for max_k in range(k, 0, -1):
                if i == 0:
                    dp[i][max_k][1] = -prices[i]
                    continue
                dp[i][max_k][0] = max(dp[i-1][max_k][0], dp[i-1][max_k][1] + prices[i])
                dp[i][max_k][1] = max(dp[i-1][max_k][1], dp[i-1][max_k-1][0] - prices[i])
                
        return dp[-1][-1][0]
