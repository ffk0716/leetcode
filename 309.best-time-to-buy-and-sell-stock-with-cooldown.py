#
# @lc app=leetcode id=309 lang=python3
#
# [309] Best Time to Buy and Sell Stock with Cooldown
#


# @lc code=start
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices) < 2:
            return 0
        p = prices[0]
        S = 0
        B = -p
        H = -p  # hold stock
        R = 0  # rest, no stock
        for p in prices[1:]:
            n_S = max(B + p, H + p)
            n_B = R - p
            n_H = max(B, H)
            n_R = max(R, S)
            S, B, H, R = n_S, n_B, n_H, n_R

        return max(S, B, H, R)


# @lc code=end
