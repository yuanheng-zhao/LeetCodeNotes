# Two Pointers, Sliding Window
class Solution:
    def countSubarrays(self, nums: List[int], minK: int, maxK: int) -> int:

        nearest_min_idx = nearest_max_idx = -1
        l = -1
        count = 0
        for r, num in enumerate(nums):
            if num < minK or num > maxK:
                l = r
            if num == minK:
                nearest_min_idx = r
            if num == maxK:
                nearest_max_idx = r
            count += max(0, min(nearest_min_idx, nearest_max_idx) - l)
        
        return count
