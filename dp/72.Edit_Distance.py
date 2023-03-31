class Solution:
    def minDistance(self, word1: str, word2: str) -> int:

        if len(word1) == 0:
            return len(word2)
        if len(word2) == 0:
            return len(word1)

        dp = [[None for _ in range(len(word2) + 1)] for _ in range(len(word1) + 1)]
        for i in range(len(dp)):
            dp[i][0] = i
        for j in range(len(dp[0])):
            dp[0][j] = j
        for i in range(1, len(word1) + 1):
            for j in range(1, len(word2) + 1):
                if word1[i-1] == word2[j-1]:
                    dp[i][j] = dp[i-1][j-1]
                else:
                    # dp[i][j] = dp[i-1][j-1] + 1  # replace
                    # dp[i][j] = min(dp[i][j], dp[i][j-1] + 1)  # insert
                    # dp[i][j] = min(dp[i][j], dp[i-1][j] + 1)  # delete
                    dp[i][j] = min(dp[i-1][j-1], min(dp[i][j-1], dp[i-1][j])) + 1

        return dp[-1][-1]
