#
# @lc app=leetcode id=448 lang=python3
#
# [448] Find All Numbers Disappeared in an Array
#


# @lc code=start
class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        for i in range(len(nums)):
            while nums[nums[i] - 1] != nums[i]:
                v = nums[i]
                nums[i], nums[v - 1] = nums[v - 1], nums[i]
        ans = []
        for i in range(len(nums)):
            if nums[i] != (i + 1):
                ans.append(i + 1)
        return ans


# @lc code=end
