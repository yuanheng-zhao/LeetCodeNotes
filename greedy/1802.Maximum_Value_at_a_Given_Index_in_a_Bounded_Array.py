# Binary Search, Greedy

# Holy Trickyyyy this one
class Solution:

    def maxValue(self, n: int, index: int, maxSum: int) -> int:

        if n == 1:
            return maxSum
        
        maxSum -= n  # Note
        l, r = 0, maxSum
        total_sum = 0
        while l <= r:
            mid = l + (r - l) // 2
            l_width = min(mid, index + 1)  # or l_length, inclusive target x at index
            r_width = min(mid, n - index)  # inclusive x at index
            left_sum = mid if l_width <= 1 else (mid + mid - l_width + 1) * l_width // 2
            right_sum = mid if r_width <= 1 else (mid + mid - r_width + 1) * r_width // 2
            total_sum = left_sum + right_sum - mid

            # Note, +1 because we minus one for all the positions in the array (maxSum -= n)
            # And to convert it back, +1 is necessary; that's why we return l finally instead of l - 1
            if total_sum == maxSum:
                return mid + 1
            if total_sum < maxSum:
                l = mid + 1
            elif total_sum > maxSum:
                r = mid - 1
                
        return l

    

    # I don't fully understand why this version work
    # def maxValue(self, n: int, index: int, maxSum: int) -> int:

    #     # x = n - 1                    # value we are looking for, e.g. nums[index]
    #     # l_width = min(x, index + 1)  # or l_length, inclusive target x at index
    #     # r_width = min(x, n - index)  # inclusive x at index
    #     # left_sum = x if l_width <= 1 else x * (x - l_width + 1) * (l_width + 1) / 2
    #     # right_sum = x if r_width <= 1 else x * (x + r_width - 1) * r_width / 2
    #     # total_sum = left_sum + right_sum - x

    #     if n == 1:
    #         return maxSum

    #     l, r = 0, maxSum
    #     maxSum -= n  # Note
    #     while l < r:
    #         mid = l + (r - l) // 2
    #         l_width = min(mid, index + 1)  # or l_length, inclusive target x at index
    #         r_width = min(mid, n - index)  # inclusive x at index
    #         left_sum = mid if l_width <= 1 else (mid + mid - l_width + 1) * l_width // 2
    #         right_sum = mid if r_width <= 1 else (mid + mid - r_width + 1) * r_width // 2
    #         total_sum = left_sum + right_sum - mid

    #         if total_sum <= maxSum:
    #             l = mid + 1
    #         elif total_sum > maxSum:
    #             r = mid

    #     return l
