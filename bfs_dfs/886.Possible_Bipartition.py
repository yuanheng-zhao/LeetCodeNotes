# DFS, BFS, Bipartite
# Same as 785. Is Graph Bipartite?

class Solution:
    def possibleBipartition(self, n: int, dislikes: List[List[int]]) -> bool:       
        # Bipartite

        # build the graph first
        graph = [[] for _ in range(n + 1)]  # 1-indexed
        for dislike in dislikes:
            u, v = dislike[0], dislike[1]
            graph[u].append(v)
            graph[v].append(u)
        
        visited = [False for _ in range(n + 1)] # 1-indexed
        colors = [False for _ in range(n + 1)]  # 1-indexed
        
        for node in range(n):
            if not visited[node] and not self.bfs(node, graph, visited, colors):
                return False
        return True


    # dfs in 785, let's do bfs this time
    def bfs(self, v: int, graph: List[List[int]], visited: List[bool], colors: List[bool]) -> bool:
        visited[v] = True
        queue = [v]
        while queue:
            node = queue.pop(0)
            for neighbor in graph[node]:
                if not visited[neighbor]:
                    visited[neighbor] = True
                    colors[neighbor] = not colors[node]
                    queue.append(neighbor)
                else:
                    if colors[neighbor] == colors[node]:
                        return False
        return True
