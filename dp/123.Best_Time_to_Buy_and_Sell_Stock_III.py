class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        if len(prices) <= 1:
            return 0
        
        max_k = 2
        dp = [[[0, 0] for _ in range(max_k + 1)] for _ in range(len(prices))]
        for i in range(len(prices)):  # this could be skipped and all the tests passed. I don't yet know why.
            dp[i][0][1] = float('-inf')
        for i in range(len(prices)):
            for k in range(1, max_k + 1):
                if i == 0:
                    dp[i][k][1] = -prices[i]
                    continue
                dp[i][k][0] = max(dp[i-1][k][0], dp[i-1][k][1] + prices[i])
                dp[i][k][1] = max(dp[i-1][k][1], dp[i-1][k-1][0] - prices[i])

        return dp[-1][-1][0]


    def maxProfit(self, prices: List[int]) -> int:

        if len(prices) <= 1:
            return 0
        
        s1 = -prices[0]     # buy 1
        s2 = float('-inf')  # buy 1 sell 1
        s3 = float('-inf')  # buy 1 sell 1 buy 1
        s4 = float('-inf')  # buy 1 sell 1 buy 1 sell 1
        for i in range(1, len(prices)):
            s4 = max(s4, s3 + prices[i])
            s3 = max(s3, s2 - prices[i])
            s2 = max(s2, s1 + prices[i])
            s1 = max(s1, -prices[i])

        return max(0, s2, s4)
