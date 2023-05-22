# Array, Greedy, Sorting
# Recall 253. Meeting Rooms II
# Similar to 452. Minimum Number of Arrows to Burst Balloons

class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        # # LIS ver
        # # O(n^2), will exceed time limits for some tests!
        # if len(intervals) <= 1:
        #     return 0

        # intervals.sort()
        
        # dp = [1 for _ in range(len(intervals))]
        # for i in range(1, len(intervals)):
        #     for j in range(i):
        #         if intervals[j][1] <= intervals[i][0]:
        #             dp[i] = max(dp[i], dp[j] + 1)

        # return len(intervals) - max(dp)

        # Greedy ver
        if len(intervals) <= 1:
            return 0

        non_overlapping_count = 1
        intervals.sort(key=lambda x : x[1])
        prev_end = intervals[0][1]
        for i in range(1, len(intervals)):
            curr_start = intervals[i][0]
            if curr_start >= prev_end:
                non_overlapping_count += 1
                prev_end = intervals[i][1]

        return len(intervals) - non_overlapping_count
