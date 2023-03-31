class Solution:
    def minimumEffortPath(self, heights: List[List[int]]) -> int:

        dirs = [[-1, 0], [1, 0], [0, -1], [0, 1]]

        rows = len(heights)
        cols = len(heights[0])
        efforts = [[float('inf') for _ in range(cols)] for _ in range(rows)]
        efforts[0][0] = 0
        pq = []
        pq.append((0, 0, 0))  # (min effort from start point, start_i, start_j)
        while pq:
            effort, i, j = heapq.heappop(pq)
            for dir in dirs:
                next_i = i + dir[0]
                next_j = j + dir[1]
                if next_i < 0 or next_j < 0 or next_i >= rows or next_j >= cols:
                    continue
                new_effort = max(effort, abs(heights[i][j] - heights[next_i][next_j]))
                if efforts[next_i][next_j] > new_effort:
                    efforts[next_i][next_j] = new_effort
                    heapq.heappush(pq, (new_effort, next_i, next_j))

        return efforts[-1][-1]
