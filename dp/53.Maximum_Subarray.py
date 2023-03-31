class Solution:

    # dp
    def maxSubArray(self, nums: List[int]) -> int:

        dp = [nums[i] for i in range(len(nums))]
        for i in range(1, len(nums)):
            dp[i] = max(dp[i], dp[i - 1] + nums[i])
        return max(dp)


    # simulation
    def maxSubArray(self, nums: List[int]) -> int:
        pass
    