#
# @lc app=leetcode id=437 lang=python3
#
# [437] Path Sum III
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution:
    def pathSum(self, root: TreeNode, sum: int) -> int:
        # Brute Force: O(nlogn)
        if root == None:
            return 0
        if not hasattr(self, "parent"):
            self.parent = {}

        # find all possible combinations
        cur_node = root
        ans = 0
        s = 0
        while True:
            s += cur_node.val
            if s == sum:
                ans += 1
            if cur_node in self.parent:
                cur_node = self.parent[cur_node]
            else:
                break

        # lookup for child
        self.parent[root.left] = root
        self.parent[root.right] = root
        return ans + self.pathSum(root.left, sum) + self.pathSum(
            root.right, sum)


# @lc code=end
