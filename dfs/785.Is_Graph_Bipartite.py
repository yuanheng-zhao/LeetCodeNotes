# DFS, BFS, Bipartite

class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:

        n = len(graph)  # n nodes

        visited = [False for _ in range(n)]
        colors = [False for _ in range(n)]  # just use true/false to represent two colors

        # graph[u] is an array of nodes that node u is adjacent to
        for node in range(n):
            if not visited[node] and not self.traverse(node, graph, visited, colors):
                return False
        return True



    def traverse(self, v: int, graph: List[List[int]], visited: List[bool], colors: List[int]) -> bool:

        visited[v] = True
        res = True
        for neighbor in graph[v]:
            if visited[neighbor]:
                # compare colors
                if colors[neighbor] == colors[v]:
                    return False
            else: 
                # haven't visited before, color the neighbor node
                colors[neighbor] = not colors[v]
                res = res and self.traverse(neighbor, graph, visited, colors)
        return res
