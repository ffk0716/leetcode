#
# @lc app=leetcode id=312 lang=python3
#
# [312] Burst Balloons
#


# @lc code=start
class Solution:
    def maxCoins(self, nums: List[int]) -> int:
        nums = [1] + nums + [1]
        n = len(nums)
        dp = [[0] * n for x in range(n)]
        for offset in range(2, n):
            for i in range(0, n - offset):
                l = i
                r = i + offset
                for m in range(l + 1, r):
                    dp[l][r] = max(
                        dp[l][r],
                        dp[l][m] + dp[m][r] + nums[l] * nums[m] * nums[r])
        return dp[0][-1]


# @lc code=end
