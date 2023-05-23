class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:

        # Similar to 435. Non-overlapping Intervals
        # Greedy
        # find the # of non-overlapping intervals
        if len(points) <= 1:
            return len(points)
        non_overlapping_count = 1  # inclusive
        points.sort(key=lambda x : x[1])
        prev_end = points[0][1]
        for i in range(1, len(points)):
            curr_start = points[i][0]
            if curr_start > prev_end:
                non_overlapping_count += 1
                prev_end = points[i][1]
        
        return non_overlapping_count
