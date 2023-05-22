# DFS, BFS

class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        max_area = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                max_area = max(max_area, self.dfs(grid, i, j))

        return max_area


    def dfs(self, grid: List[List[int]], i: int, j: int) -> int:
        # instead of using visited[][], draw the island visited (grid in-place)
        if i < 0 or i > len(grid) - 1 or j < 0 or j > len(grid[0]) - 1:
            return 0
        if grid[i][j] == 0:
            return 0
        grid[i][j] = 0  # draw the current cell
        area = 1
        area += self.dfs(grid, i-1, j)
        area += self.dfs(grid, i+1, j)
        area += self.dfs(grid, i, j-1)
        area += self.dfs(grid, i, j+1)
        return area
