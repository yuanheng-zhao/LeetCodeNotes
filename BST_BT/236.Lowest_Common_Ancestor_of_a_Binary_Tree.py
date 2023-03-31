# Binary Tree, DFS

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':

        # *This only works with this constraint:
        #   p and q will exist in the tree

        if root is None or root == p or root == q:
            return root
        
        l = self.lowestCommonAncestor(root.left, p, q)
        r = self.lowestCommonAncestor(root.right, p, q)
        if l is not None and r is not None:
            return root
        if l is not None:
            return l
        elif r is not None:
            return r
        return None
    

# 1644. Lowest Common Ancestor of a Binary Tree II
# p or q might not exist in the tree
class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':

        lca, num = self.dfs(root, p, q)
        if num < 2:
            return None
        return lca

    def dfs(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> Tuple['TreeNode', int]:
        if root is None:
            return root, 0
        
        l, nl = self.dfs(root.left, p, q)
        r, nr = self.dfs(root.right, p, q)
        if nl == 2 or nr == 2:
            return l or r, 2
        if l and r:
            return root, 2
        n = 0
        if (root == p or root == q):
            n += 1
        if l or r:
            n += 1
        if n > 0:
            return root, n
        return None, 0