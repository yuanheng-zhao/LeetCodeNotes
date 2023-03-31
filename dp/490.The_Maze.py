# DFS, BFS, Matrix
# Similar to Island Problem

class Solution:
    def hasPath(self, maze: List[List[int]], start: List[int], destination: List[int]) -> bool:

        m = len(maze)
        n = len(maze[0])

        def dfs(maz: List[List[int]], i: int, j: int, visited: List[List[bool]]) -> None:
            if visited[i][j]:
                return
            visited[i][j] = True
            l = j - 1
            r = j + 1
            u = i - 1
            d = i + 1
            while l >= 0 and maz[i][l] == 0:
                l -= 1
            l += 1
            while r < n and maz[i][r] == 0:
                r += 1
            r -= 1
            while u >= 0 and maz[u][j] == 0:
                u -= 1
            u += 1
            while d < m and maz[d][j] == 0:
                d += 1
            d -= 1
            dfs(maz, i, l, visited)
            dfs(maz, i, r, visited)
            dfs(maz, u, j, visited)
            dfs(maz, d, j, visited)

        visited = [[False for _ in range(n)] for _ in range(m)]
        dfs(maze, start[0], start[1], visited)
        
        return visited[destination[0]][destination[1]]
