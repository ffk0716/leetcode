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
        self.sum_list = collections.Counter([0])
        self.ans = 0
        self.test(root, sum)
        return self.ans

    def test(self, n: TreeNode, sum: int, cur_sum: int = 0) -> int:
        if n == None:
            return
        cur_sum += n.val

        self.ans += self.sum_list[cur_sum - sum]

        self.sum_list[cur_sum] += 1
        self.test(n.left, sum, cur_sum)
        self.test(n.right, sum, cur_sum)
        self.sum_list[cur_sum] -= 1


# @lc code=end
