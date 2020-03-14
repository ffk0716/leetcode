#
# @lc app=leetcode id=322 lang=python3
#
# [322] Coin Change
#


# @lc code=start
class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        inf = amount + 1
        dp = [0] + [inf] * amount
        for c in coins:
            for a in range(c, amount + 1):
                dp[a] = min(dp[a - c] + 1, dp[a])
        return dp[-1] if dp[-1] != inf else -1


# @lc code=end
