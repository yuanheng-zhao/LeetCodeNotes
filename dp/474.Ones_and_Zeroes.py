# 0-1 Knapsack Problem with 2d weights

class Solution:
    def findMaxForm(self, strs: List[str], m: int, n: int) -> int:

        dp = [[0 for _ in range(n + 1)] for _ in range(m + 1)]
        for s in strs:
            zeros = s.count("0")
            ones = len(s) - zeros
            if zeros > m or ones > n:
                continue

            # reversed order so that not pollute previous state going to be used
            for i in range(m, zeros - 1, -1):
                for j in range(n, ones - 1, -1):
                    dp[i][j] = max(dp[i][j], dp[i - zeros][j - ones] + 1)
                
        return dp[-1][-1]
