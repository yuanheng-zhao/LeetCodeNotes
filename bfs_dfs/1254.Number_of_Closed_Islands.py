# DFS, BFS, Matrix
# Similar to 200. Number of Islands
class Solution:
    def closedIsland(self, grid: List[List[int]]) -> int:

        dirs = [[-1, 0], [1, 0], [0, -1], [0, 1]]

        def dfs_mark_visited(x: int, y: int, grid: List[List[int]], visited: List[List[bool]]) -> None:
            if x < 0 or x >= len(visited) or y < 0 or y >= len(visited[0]):
                return
            if visited[x][y]:
                return
            visited[x][y] = True
            if grid[x][y] == 0:
                for dir in dirs:
                    next_x = x + dir[0]
                    next_y = y + dir[1]
                    dfs_mark_visited(next_x, next_y, grid, visited)
        
        res = 0
        visited_mat = [[False for _ in range(len(grid[0]))] for _ in range(len(grid))]
        for i in range(len(grid)):
            dfs_mark_visited(i, 0, grid, visited_mat)
            dfs_mark_visited(i, len(grid[0]) - 1, grid, visited_mat)
        for j in range(len(grid[0])):
            dfs_mark_visited(0, j, grid, visited_mat)
            dfs_mark_visited(len(grid) - 1, j, grid, visited_mat)
        for i in range(1, len(grid) - 1):
            for j in range(1, len(grid[0]) - 1):
                if not visited_mat[i][j] and grid[i][j] == 0:
                    res += 1
                    dfs_mark_visited(i, j, grid, visited_mat)
        
        return res
