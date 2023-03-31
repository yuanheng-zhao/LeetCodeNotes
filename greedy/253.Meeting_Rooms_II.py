# Array, Two Pointers, Greedy, Sorting
from typing import List

class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:

        starts = []
        ends = []
        for interval in intervals:
            starts.append(interval[0])
            ends.append(interval[1])
        starts.sort()
        ends.sort()
        ans = 0
        end_idx = 0

        for i in range(len(starts)):
            if starts[i] < ends[end_idx]:
                ans += 1
            else:
                end_idx += 1
        
        return ans
