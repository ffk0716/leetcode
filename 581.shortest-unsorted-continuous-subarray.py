#
# @lc app=leetcode id=581 lang=python3
#
# [581] Shortest Unsorted Continuous Subarray
#


# @lc code=start
class Solution:
    def findUnsortedSubarray(self, nums: List[int]) -> int:
        pos = len(nums)
        for i in range(0, len(nums) - 1):
            if nums[i] > nums[i + 1]:
                pos = i + 1
                break
        if pos == len(nums):
            return 0
        min_v = min(nums[pos:])
        for i in range(0, len(nums)):
            if min_v < nums[i]:
                l_i = i
                break

        pos = -1
        for i in range(len(nums) - 1, 0, -1):
            if nums[i] < nums[i - 1]:
                pos = i - 1
                break
        max_v = max(nums[:pos + 1])
        print(pos)
        for i in range(len(nums) - 1, -1, -1):
            if max_v > nums[i]:
                r_i = i
                break
        print(l_i, r_i)
        return r_i - l_i + 1


# @lc code=end
