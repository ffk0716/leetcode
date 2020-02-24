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
        for i in range(1, len(nums)):
            if nums[i - 1] > nums[i]:
                min_v = min(nums[i:])
                break
        else:
            return 0
        for i in range(0, len(nums)):
            if min_v < nums[i]:
                subset_start = i
                break

        for i in reversed(range(1, len(nums))):
            if nums[i - 1] > nums[i]:
                max_v = max(nums[:i])
                break
        else:
            assert False
        for i in reversed(range(0, len(nums))):
            if max_v > nums[i]:
                subset_end = i + 1
                break
        return subset_end - subset_start


# @lc code=end
