#
# @lc app=leetcode id=198 lang=python3
#
# [198] House Robber
#


# @lc code=start
class Solution:
    def rob(self, nums: List[int]) -> int:
        p1 = p2 = 0
        for n in nums:
            p2, p1 = p1, max(n + p2, p1)
        return p1


# @lc code=end
