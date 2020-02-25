#
# @lc app=leetcode id=494 lang=python3
#
# [494] Target Sum
#


# @lc code=start
class Solution:
    def findTargetSumWays(self, nums: List[int], S: int) -> int:
        dp = collections.defaultdict(int)
        dp[nums[0]] += 1
        dp[-nums[0]] += 1
        for i in range(1, len(nums)):
            ndp = collections.defaultdict(int)
            for k in dp:
                ndp[k + nums[i]] += dp[k]
                ndp[k - nums[i]] += dp[k]
            dp = ndp
        if S in dp:
            return dp[S]
        return 0


# @lc code=end
