# DFS, Backtracking
class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:

        m = len(board)
        n = len(board[0])
        
        def dfs(i: int, j: int, idx:int, visiting: List[List[bool]]) -> bool:
            if idx == len(word):
                return True
            if i < 0 or j < 0 or i >= m or j >= n:
                return False
            if visiting[i][j] or board[i][j] != word[idx]:
                return False
            
            res = False
            visiting[i][j] = True
            res = dfs(i-1, j, idx+1, visiting) or dfs(i+1, j, idx+1, visiting) or dfs(i, j-1, idx+1, visiting) or dfs(i, j+1, idx+1, visiting)
            visiting[i][j] = False
            return res

        # visiting instead of visited
        # visiting indicating specific cells have been visited, or have been visiting during the current search on current
        # chain of characters, and so that we should not use it twice
        visiting_mat = [[False for _ in range(n)] for _ in range(m)]
        for i in range(m):
            for j in range(n):
                if dfs(i, j, 0, visiting_mat):
                    return True

        return False
