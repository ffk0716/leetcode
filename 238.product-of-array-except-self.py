#
# @lc app=leetcode id=238 lang=python3
#
# [238] Product of Array Except Self
#


# @lc code=start
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        c = 1
        r = []
        for n in nums:
            r.append(c)
            c *= n
        c = 1
        for i in reversed(range(len(nums))):
            r[i] *= c
            c *= nums[i]
        return r


# @lc code=end
