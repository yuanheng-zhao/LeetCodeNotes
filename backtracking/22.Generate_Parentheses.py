# Backtracking, DP

class Solution:
    def generateParenthesis(self, n: int) -> List[str]:

        # it's not really a backtracking I think (since it just go into, but not revert its status), and neither dfs?
        def helper(l_remaining: int, r_remaining: int, ans: str, res: List[str]) -> None:
            if l_remaining == 0 and r_remaining == 0:
                res.append(ans)
                return
            if l_remaining > 0:
                helper(l_remaining - 1, r_remaining, ans + '(', res)
            if r_remaining > 0 and r_remaining > l_remaining:
                helper(l_remaining, r_remaining - 1, ans + ')', res)
        
        res = []
        helper(n, n, '', res)
        return res
