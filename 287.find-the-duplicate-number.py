#
# @lc app=leetcode id=287 lang=python3
#
# [287] Find the Duplicate Number
#


# @lc code=start
class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        t = 0
        r = 0
        while True:
            t = nums[t]
            r = nums[nums[r]]
            if t == r:
                break
        t2 = 0
        while True:
            t = nums[t]
            t2 = nums[t2]
            if t == t2:
                return t


# @lc code=end
