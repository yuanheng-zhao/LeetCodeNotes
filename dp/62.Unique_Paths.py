# DP, Combination

class Solution:
    def uniquePaths(self, m: int, n: int) -> int:

        visited = [[False for _ in range(n)] for _ in range(m)]
        dp = [[-1 for _ in range(n)] for _ in range(m)]
        dp[-1][-1] = 1
        return self.traverse(0, 0, visited, dp)


    def traverse(self, x: int, y: int, visited: List[List[bool]], mem: List[List[int]]) -> int:
        m = len(visited)
        n = len(visited[0])
        # no change to move up (x-1) or left (y-1) so unnecessary to check x < 0 or y < 0
        # if x < 0 or x >= m or y < 0 or y >= n or visited[x][y]:
        if x >= m or y >= n or visited[x][y]:
            return 0
        if mem[x][y] >= 0:
            return mem[x][y]
        count = 0
        visited[x][y] = True
        count += self.traverse(x+1, y, visited, mem)  # move down
        count += self.traverse(x, y+1, visited, mem)  # move right
        visited[x][y] = False
        mem[x][y] = count
        return count
