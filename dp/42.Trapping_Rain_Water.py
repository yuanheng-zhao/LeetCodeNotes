# DP, Memo, Two Pointers
# Related: 11
class Solution:

    # Time: O(N), Space: O(N)
    def trap(self, height: List[int]) -> int:

        l_max = [0 for _ in range(len(height))]  # inclusive, maximum height to the left of current position
        r_max = [0 for _ in range(len(height))]  # inclusive, .. ..                 right .. ..
        l_max[0] = height[0]
        for i in range(1, len(height)):
            l_max[i] = max(l_max[i - 1], height[i])
        r_max[-1] = height[-1]
        for i in range(len(height) - 2, -1, -1):
            r_max[i] = max(r_max[i + 1], height[i])
        
        total = 0
        for i in range(len(height)):
            total += min(l_max[i], r_max[i]) - height[i]
        return total


    # Time: O(N), Space: O(1)
    def trap(self, height: List[int]) -> int:

        res = 0
        l_max = r_max = 0
        l, r = 0, len(height) - 1
        while l <= r:
            l_max = max(l_max, height[l])
            r_max = max(r_max, height[r])
            if l_max < r_max:
                res += l_max - height[l]
                l += 1
            else:  # l_max >= r_max
                res += r_max - height[r]
                r -= 1
        
        return res
