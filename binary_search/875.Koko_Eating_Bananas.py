# Binary Search, Array

class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:

        def feasible(k: int) -> bool:
            total_h_used = 0
            for pile in piles:
                total_h_used += pile // k
                if pile % k != 0:
                    total_h_used += 1
                if total_h_used > h:
                    return False
            return True

        l, r = 1, max(piles)
        while l < r:
            mid = l + (r - l) // 2
            if feasible(mid): # hours required to finish eating all the bananas <= h
                r = mid
            else:
                l = mid + 1
        return l
