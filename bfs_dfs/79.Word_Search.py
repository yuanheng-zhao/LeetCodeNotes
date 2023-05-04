# DFS, Backtracking
class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:

        m = len(board)
        n = len(board[0])
        self.word = word  # 小偷一手
        self.board = board
        
        # visiting instead of visited
        # visiting indicating specific cells have been visited, or have been visiting during the current search on current
        # chain of characters, and so that we should not use it twice
        visiting_mat = [[False for _ in range(n)] for _ in range(m)]
        for i in range(m):
            for j in range(n):
                if self.dfs(visiting_mat, i, j, 0):
                    return True
        
        return False


    def dfs(self, visiting: List[List[bool]], i: int, j: int, idx: int) -> bool:
        if idx == len(self.word):
            return True
        if i < 0 or i >= len(visiting) or j < 0 or j >= len(visiting[0]):
            return False
        if visiting[i][j] or self.board[i][j] != self.word[idx]:
            return False
        
        visiting[i][j] = True
        idx += 1
        res = (self.dfs(visiting, i-1, j, idx) 
               or self.dfs(visiting, i+1, j, idx)
               or self.dfs(visiting, i, j-1, idx)
               or self.dfs(visiting, i, j+1, idx))
        visiting[i][j] = False
        return res
