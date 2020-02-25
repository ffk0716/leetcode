#
# @lc app=leetcode id=543 lang=python3
#
# [543] Diameter of Binary Tree
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution:
    def diameterOfBinaryTree(self, root: TreeNode) -> int:
        def get_height(node) -> int:
            if node == None:
                return 0
            lv = get_height(node.left)
            rv = get_height(node.right)
            self.max_path = max(self.max_path, lv + rv)
            return max(lv, rv) + 1

        self.max_path = 0
        get_height(root)
        return self.max_path


# @lc code=end
