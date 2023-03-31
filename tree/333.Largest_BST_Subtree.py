from typing import Optional
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def largestBSTSubtree(self, root: Optional[TreeNode]) -> int:

        def helper(node: Optional[TreeNode]) -> List[int]:
            """
            Returns: 
            List[int]: [minimum value of subtree, maximum value of subtree, largest number of nodes for subtree]
            """
            if node is None:
                return [float('inf'), float('-inf'), 0]
            if node.left is None and node.right is None:
                return [node.val, node.val, 1]

            l = helper(node.left)
            r = helper(node.right)
            min_val = float('-inf')
            max_val = float('inf')
            num = 0
            if l[1] < node.val and node.val < r[0]:
                # min and max are used here because of we have infinity values at leaves
                min_val = min(l[0], node.val)
                max_val = max(r[1], node.val)
                num = l[2] + r[2] + 1
            else: # subtree of the node as root is not a BST
                num = max(l[2], r[2])
            return [min_val, max_val, num]
        
        res = helper(root)
        return res[2]
