#
# @lc app=leetcode id=236 lang=python3
#
# [236] Lowest Common Ancestor of a Binary Tree
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode',
                             q: 'TreeNode') -> 'TreeNode':
        p_visit = False
        q_visit = False
        self.LCA = None

        def find_node(n):
            if n == None:
                return False, False
            l = find_node(n.left)
            r = find_node(n.right)
            rp, rq = l[0] or r[0] or (n == p), l[1] or r[1] or (n == q)
            if self.LCA == None:
                if rp and rq:
                    self.LCA = n
            return rp, rq

        find_node(root)
        return self.LCA


# @lc code=end
