# DFS, BFS, BST, Hash

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def verticalOrder(self, root: Optional[TreeNode]) -> List[List[int]]:

        queue = []
        if root is None:
            return queue
        queue.append((0, root))
        col2vals = {}
        while queue:
            col_idx, node = queue.pop(0)
            if node is None:
                continue
            if col_idx not in col2vals:
                col2vals[col_idx] = []
            col2vals[col_idx].append(node.val)
            queue.append((col_idx - 1, node.left))
            queue.append((col_idx + 1, node.right))

        res = []
        for col_idx in sorted(col2vals.keys()):
            res.append(col2vals[col_idx])
        return res
