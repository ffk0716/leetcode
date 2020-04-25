#
# @lc app=leetcode id=152 lang=python3
#
# [152] Maximum Product Subarray
#


# @lc code=start
class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
        cur_min = nums[0]
        cur_max = nums[0]
        glo_max = nums[0]
        for i in range(1, len(nums)):
            next_min = min(nums[i] * cur_min, nums[i] * cur_max, nums[i])
            next_max = max(nums[i] * cur_min, nums[i] * cur_max, nums[i])
            cur_min, cur_max = next_min, next_max
            glo_max = max(cur_max, glo_max)
        return glo_max


# @lc code=end
