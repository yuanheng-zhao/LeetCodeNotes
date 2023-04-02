# DFS, BFS, Matrix
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:

        dirs = [[-1, 0], [1, 0], [0, -1], [0, 1]]

        def dfs_mark_visited(x: int, y:int, grid: List[List[str]], visited: List[List[bool]]) -> None:
            if x < 0 or x >= len(visited) or y < 0 or y >= len(visited[0]):
                return
            if visited[x][y]:
                return
            visited[x][y] = True
            if grid[x][y] == "1":
                for dir in dirs:
                    next_x = x + dir[0]
                    next_y = y + dir[1]
                    dfs_mark_visited(next_x, next_y, grid, visited)

        visited_mat = [[False for _ in range(len(grid[0]))] for _ in range(len(grid))]
        res = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if not visited_mat[i][j] and grid[i][j] == "1":
                    res += 1
                    dfs_mark_visited(i, j, grid, visited_mat)

        return res


    # Note: Another way without using a visited matrix,
    # drown the islands whenever we encounter one. That is, modify in-place on grid to save space of visited matrix
