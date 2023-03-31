# 0-1 Knapsack Problem
class Solution:
    def canPartition(self, nums: List[int]) -> bool:

        total = sum(nums)
        if total % 2 != 0:
            return False

        half = total // 2
        dp = [False for _ in range(half + 1)]
        dp[0] = True
        for num in nums:
            if num > half:
                continue
            for i in range(half, 0, -1):  # dp[0] should always be True
                if num <= i:
                    dp[i] = dp[i] or dp[i - num]

        return dp[-1]
