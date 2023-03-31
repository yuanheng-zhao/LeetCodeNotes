from typing import Optional, Tuple
from util.TreeNode import TreeNode

class Solution:
    def findDistance(self, root: Optional[TreeNode], p: int, q: int) -> int:

        def helper(node: Optional[TreeNode], p: int, q: int) -> Tuple[int, int, bool]:
            """
            Returns:
            Tuple[int, int, bool]: (p distance, q distance, finished)
            """
            if node is None:
                return (-1, -1, False)
            
            l = helper(node.left, p, q)
            r = helper(node.right, p, q)

            # finished in left or right subtree
            if l[2]:
                return l
            if r[2]:
                return r

            finished = False
            p_dist = max(l[0], r[0])
            q_dist = max(l[1], r[1])
            # print(node.val, ", p_dist=", p_dist, ", q_dist=", q_dist, ", finished=", finished)
            if node.val == p:
                p_dist = 0
            elif node.val == q:
                q_dist = 0
            if p_dist >= 0 and q_dist >= 0:
                finished = True
            if not finished:
                if p_dist >= 0:
                    p_dist += 1
                if q_dist >= 0:
                    q_dist += 1
            # print(node.val, ", p_dist=", p_dist, ", q_dist=", q_dist, ", finished=", finished)
            return [p_dist, q_dist, finished]

        if p == q:
            return 0
        res = helper(root, p, q)
        return res[0] + res[1]
