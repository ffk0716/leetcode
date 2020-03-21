#
# @lc app=leetcode id=300 lang=python3
#
# [300] Longest Increasing Subsequence
#


# @lc code=start
class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        # dp solution, time O(n2)
        if len(nums) == 0:
            return 0
        dp = [1] * len(nums)
        for i in range(len(nums)):
            v = nums[i]
            for j in range(i):
                if nums[j] < nums[i]:
                    dp[i] = max(dp[i], dp[j] + 1)
        return max(dp)


# @lc code=end
