# Binary Search, Array

# https://www.cnblogs.com/kyoner/p/11080078.html

class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        
        if len(nums) == 0:
            return [-1, -1]

        # search the first appearance of target (left bound)
        left_bound = -1
        l, r = 0, len(nums)
        while l < r:
            mid = l + (r - l) // 2
            if nums[mid] == target:
                r = mid
            elif nums[mid] < target:
                l = mid + 1
            else: # nums[mid] > target
                r = mid
        if l < len(nums) and nums[l] == target: # make sure target value exists
            left_bound = l
        if left_bound == -1:
            return [-1, -1]

        # search the last appearance of target (right bound)'
        right_bound = -1
        l, r = 0, len(nums)
        while l < r:
            mid = l + (r - l) // 2
            if nums[mid] == target:
                l = mid + 1
            elif nums[mid] < target:
                l = mid + 1
            else: # nums[mid] > target
                r = mid

        # unnecessary to check if target value exists in nums
        # if l > 0 and nums[l] == target:
        right_bound = l - 1
        return [left_bound, right_bound]
