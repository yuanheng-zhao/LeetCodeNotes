# Backtracking
from typing import List

class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:

        # best to change change names of params
        def feasible(board: List[List[str]], i: int, j: int) -> bool:
            """
            :param i: row index going to place the Queen 
            :param j: col index going to place the Queen
            :return: true if placing a Queen on board[i][j] is feasible, otherwise false
            """
            # direction: up
            for k in range(i - 1, -1, -1):
                if board[k][j] == 'Q':
                    return False
            # direction: left-up
            k, l = i - 1, j - 1
            while k >= 0 and l >= 0:
                if board[k][l] == 'Q':
                    return False
                k -= 1
                l -= 1
            # direction: right-up
            k, l = i - 1, j + 1
            while k >= 0 and l < n:
                if board[k][l] == 'Q':
                    return False
                k -= 1
                l += 1
            return True
            

        def bt(board: List[List[str]], row_idx: int, res: List[List[str]]) -> None:
            # n: the length of board and board[0]
            if row_idx == n:
                curr_res = []
                for row in board:
                    curr_res.append(''.join(row))
                res.append(curr_res)
                return
            for col_idx in range(n):
                if not feasible(board, row_idx, col_idx):
                    continue
                # Good, position passed the rule
                board[row_idx][col_idx] = 'Q'
                bt(board, row_idx + 1, res)
                board[row_idx][col_idx] = '.'

        board = [["." for _ in range(n)] for _ in range(n)]
        res = []
        bt(board, 0, res)
        return res
