# Shortest Path, BFS, Dijkstra

import heapq
from typing import List

class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:

        adj_graph = [[] for _ in range(n + 1)]  # 1-indexed
        for time in times:
            u, v, w = time[0], time[1], time[2]
            adj_graph[u].append((v, w))
        dist_to = [float('inf') for _ in range(n + 1)]  # 1-indexed (it's awkward here)
        dist_to[0] = 0
        dist_to[k] = 0
        
        pq = []
        pq.append((0, k))
        while pq:
            dist, node = heapq.heappop(pq)
            for neighbor, w in adj_graph[node]:
                if dist + w < dist_to[neighbor]:
                    dist_to[neighbor] = dist + w
                    heapq.heappush(pq, (dist_to[neighbor], neighbor))

        if float('inf') in dist_to:
            return -1
        
        return max(dist_to)
