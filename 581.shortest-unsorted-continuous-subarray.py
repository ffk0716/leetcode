#
# @lc app=leetcode id=581 lang=python3
#
# [581] Shortest Unsorted Continuous Subarray
#


# @lc code=start
class Solution:
    def findUnsortedSubarray(self, nums: List[int]) -> int:
        # Time: O(n)
        # Space: O(1)
        #  1 3 8 4 5 6 2 7 9
        # |  L  |  M  |  R  |
        for i in range(0, len(nums) - 1):
            if nums[i] > nums[i + 1]:
                max_L_i = i
                break
        else:
            return 0
        for i in reversed(range(1, len(nums))):
            if nums[i - 1] > nums[i]:
                min_R_i = i
                break
        else:
            assert False
        max_v = max(nums[max_L_i:min_R_i + 1])
        min_v = min(nums[max_L_i:min_R_i + 1])
        for i in range(0, len(nums)):
            if min_v < nums[i]:
                min_M_i = i
                break
        for i in reversed(range(0, len(nums))):
            if max_v > nums[i]:
                max_M_i = i
                break
        return max_M_i - min_M_i + 1


# @lc code=end
