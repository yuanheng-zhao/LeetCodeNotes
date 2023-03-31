# Dijkstra
class Solution:
    def minimumCosts(self, regular: List[int], express: List[int], expressCost: int) -> List[int]:

        num_of_stops = len(regular) + 1

        V = (num_of_stops) * 2
        graph = [[] for _ in range(V)]
        for i in range(len(regular)):
            graph[i].append((i+1, regular[i]))  # e.g. 0 -> (1, 1)
            graph[i].append((i + num_of_stops, expressCost))
        for i in range(len(express)):
            express_idx = i + num_of_stops
            graph[express_idx].append((express_idx + 1, express[i]))  # e.g. 3(express) -> (4(express), 10)
            graph[express_idx].append((i, 0))
        
        dist_to = [float('inf') for _ in range(V)]
        dist_to[0] = 0
        pq = []
        pq.append((0, 0))
        while pq:
            distance, node = heapq.heappop(pq)
            for neighbor, w in graph[node]:
                if distance + w < dist_to[neighbor]:
                    dist_to[neighbor] = distance + w
                    heapq.heappush(pq, (dist_to[neighbor], neighbor))

        # decode
        res = []
        for i in range(num_of_stops):
            res.append(min(dist_to[i], dist_to[i + num_of_stops]))
        res.pop(0)  # remove min distance to stop #0 (always 0)

        return res
