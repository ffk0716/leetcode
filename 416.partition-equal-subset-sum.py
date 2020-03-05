#
# @lc app=leetcode id=416 lang=python3
#
# [416] Partition Equal Subset Sum
#


# @lc code=start
class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        total_sum = sum(nums)
        if total_sum & 1:
            return False
        target_sum = total_sum // 2
        dp = [True] + [False] * target_sum  # the combination of size 0 is 1
        for i in range(len(nums)):
            for s in range(target_sum , -1, -1):
                if nums[i] <= s:
                    dp[s] |= dp[s - nums[i]]
            if dp[target_sum ]:
                return True
        return False


# @lc code=end
