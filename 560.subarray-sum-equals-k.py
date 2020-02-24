#
# @lc app=leetcode id=560 lang=python3
#
# [560] Subarray Sum Equals K
#


# @lc code=start
class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        acc = collections.Counter()
        acc[0] = 1
        a = 0
        ans = 0
        for v in nums:
            a += v
            if a - k in acc:
                ans += acc[a - k]
            acc[a] += 1

        return ans


# @lc code=end
