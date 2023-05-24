class Solution:
    def minIncrementForUnique(self, nums: List[int]) -> int:

        if nums is None or len(nums) == 0:
            return 0
        
        nums.sort()

        step = 0
        need = 0

        for i in range(1, len(nums)):
            need = max(nums[i-1] + 1, nums[i])
            step += need - nums[i]
            nums[i] = need
        
        return step


