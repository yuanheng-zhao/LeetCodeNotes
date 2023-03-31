# Two Pointers, Greedy
# Related: 42
class Solution:
    def maxArea(self, height: List[int]) -> int:

        res = 0
        l, r = 0, len(height) - 1
        while l < r:
            curr = min(height[l], height[r]) * (r - l)
            res = max(res, curr)
            if height[l] < height[r]:
                l += 1
            else: # height[l] >= height[r]
                r -= 1

        return res
