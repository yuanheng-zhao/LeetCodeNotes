# DFS, BFS, Hash
from typing import List

class Solution:
    def numDistinctIslands(self, grid: List[List[int]]) -> int:

        m = len(grid)
        n = len(grid[0])

        def dfs(i: int, j: int, grid_mat: List[List[int]], visited: List[List[int]], dir_sequence: List[str], dir: int) -> None:
            if i < 0 or j < 0 or i >= m or j >= n:
                return
            if visited[i][j] or grid_mat[i][j] != 1:
                return

            visited[i][j] = True
            dir_sequence.append(str(dir))
            dfs(i-1, j, grid_mat, visited, dir_sequence, 1)  # up
            dfs(i+1, j, grid_mat, visited, dir_sequence, 2)  # down
            dfs(i, j-1, grid_mat, visited, dir_sequence, 3)  # left
            dfs(i, j+1, grid_mat, visited, dir_sequence, 4)  # right
            dir_sequence.append(str(-dir))

        visited = [[False for _ in range(n)] for _ in range(m)]
        res = set()
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    seq = []
                    dfs(i, j, grid, visited, seq, 0)
                    res.add(','.join(seq))
        
        res.discard('')
        return len(res)
