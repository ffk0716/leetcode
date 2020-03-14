#
# @lc app=leetcode id=337 lang=python3
#
# [337] House Robber III
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution:
    def rob(self, root: TreeNode) -> int:
        def get_value(n: TreeNode) -> int:
            if n == None:
                return 0, 0
            lp, lnp = get_value(n.left)
            rp, rnp = get_value(n.right)
            return lnp + rnp + n.val, max(lp, lnp) + max(rp, rnp)
            # pick, not_pick

        return max(get_value(root))


# @lc code=end
