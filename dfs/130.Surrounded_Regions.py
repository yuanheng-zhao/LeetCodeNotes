# DFS, BFS, Union Find

# This solution does not practice with Union Find though
class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        m = len(board)
        n = len(board[0])
        def substitute_as(x: int, y: int, board_mat: List[List[str]], to_sub: str, as_char: str) -> None:
            if x < 0 or y < 0 or x >= m or y >= n:
                return
            if board_mat[x][y] != to_sub:
                return
            board_mat[x][y] = as_char
            substitute_as(x-1, y, board_mat, to_sub, as_char)
            substitute_as(x+1, y, board_mat, to_sub, as_char)
            substitute_as(x, y-1, board_mat, to_sub, as_char)
            substitute_as(x, y+1, board_mat, to_sub, as_char)
        
        for j in range(n):
            substitute_as(0, j, board, 'O', 'S')
            substitute_as(m-1, j, board, 'O', 'S')
        for i in range(m):
            substitute_as(i, 0, board, 'O', 'S')
            substitute_as(i, n-1, board, 'O', 'S')

        for i in range(1, m-1):
            for j in range(1, n-1):
                substitute_as(i, j, board, 'O', 'X')
        for j in range(n):
            substitute_as(0, j, board, 'S', 'O')
            substitute_as(m-1, j, board, 'S', 'O')
        for i in range(m):
            substitute_as(i, 0, board, 'S', 'O')
            substitute_as(i, n-1, board, 'S', 'O')
