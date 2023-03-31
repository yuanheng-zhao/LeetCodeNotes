# Backtracking

class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:

        def bt(left_bound: int, right_bound: int, ans: List[int], res: List[List[int]]) -> None:
            if len(ans) == k:
                res.append(ans.copy())
                return 
            for i in range(left_bound, right_bound + 1):
                ans.append(i)
                bt(i + 1, right_bound, ans, res)
                ans.pop()

        res = []
        bt(1, n, [], res)
        return res
